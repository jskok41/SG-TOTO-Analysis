import SwiftUI
import PhotosUI

struct PhotoOCRView: View {
    @StateObject private var photoProcessor = PhotoProcessor()
    @State private var selectedPhotos: [PhotosPickerItem] = []
    @State private var showingImagePicker = false
    @State private var showingCamera = false
    @State private var selectedLanguage = "en"
    @State private var showingLanguageSelector = false
    @State private var showingExportOptions = false
    
    var body: some View {
        NavigationView {
            VStack(spacing: 0) {
                // Header
                VStack(spacing: 12) {
                    HStack {
                        VStack(alignment: .leading, spacing: 4) {
                            Text("Photo OCR")
                                .font(.largeTitle)
                                .fontWeight(.bold)
                            
                            Text("Extract text from photos automatically")
                                .font(.subheadline)
                                .foregroundColor(.secondary)
                        }
                        
                        Spacer()
                        
                        Button(action: {
                            showingLanguageSelector = true
                        }) {
                            HStack(spacing: 4) {
                                Text(LanguageSelector.getLanguageName(for: selectedLanguage))
                                    .font(.caption)
                                    .fontWeight(.medium)
                                Image(systemName: "chevron.down")
                                    .font(.caption)
                            }
                            .foregroundColor(.blue)
                            .padding(.horizontal, 12)
                            .padding(.vertical, 6)
                            .background(Color.blue.opacity(0.1))
                            .cornerRadius(16)
                        }
                    }
                    .padding(.horizontal)
                    
                    // Photo Selection Options
                    HStack(spacing: 16) {
                        // Photos Picker
                        PhotosPicker(
                            selection: $selectedPhotos,
                            maxSelectionCount: 10,
                            matching: .images
                        ) {
                            VStack(spacing: 8) {
                                Image(systemName: "photo.on.rectangle.angled")
                                    .font(.title)
                                    .foregroundColor(.blue)
                                Text("Photos")
                                    .font(.caption)
                                    .fontWeight(.medium)
                            }
                            .frame(maxWidth: .infinity)
                            .padding(.vertical, 16)
                            .background(Color(.systemGray6))
                            .cornerRadius(12)
                        }
                        .onChange(of: selectedPhotos) { newItems in
                            Task {
                                await photoProcessor.processPhotos(from: newItems, language: selectedLanguage)
                            }
                        }
                        
                        // Camera Button
                        Button(action: {
                            showingCamera = true
                        }) {
                            VStack(spacing: 8) {
                                Image(systemName: "camera")
                                    .font(.title)
                                    .foregroundColor(.green)
                                Text("Camera")
                                    .font(.caption)
                                    .fontWeight(.medium)
                            }
                            .frame(maxWidth: .infinity)
                            .padding(.vertical, 16)
                            .background(Color(.systemGray6))
                            .cornerRadius(12)
                        }
                    }
                    .padding(.horizontal)
                }
                .padding(.top, 20)
                .padding(.bottom, 24)
                .background(Color(.systemBackground))
                
                // Content
                if photoProcessor.extractedTexts.isEmpty && !photoProcessor.isProcessing {
                    // Empty State
                    VStack(spacing: 20) {
                        Spacer()
                        
                        Image(systemName: "doc.text.viewfinder")
                            .font(.system(size: 80))
                            .foregroundColor(.secondary)
                        
                        VStack(spacing: 8) {
                            Text("No Photos Selected")
                                .font(.title2)
                                .fontWeight(.semibold)
                            
                            Text("Select photos from your library or take new ones with the camera to extract text")
                                .font(.body)
                                .foregroundColor(.secondary)
                                .multilineTextAlignment(.center)
                        }
                        .padding(.horizontal, 32)
                        
                        Spacer()
                    }
                } else {
                    // Results or Processing
                    ScrollView {
                        LazyVStack(spacing: 16) {
                            if photoProcessor.isProcessing {
                                // Processing Indicator
                                VStack(spacing: 16) {
                                    ProgressView()
                                        .scaleEffect(1.5)
                                    
                                    Text("Processing photos...")
                                        .font(.headline)
                                        .foregroundColor(.primary)
                                    
                                    Text("This may take a few moments depending on the number of photos")
                                        .font(.subheadline)
                                        .foregroundColor(.secondary)
                                        .multilineTextAlignment(.center)
                                }
                                .frame(maxWidth: .infinity)
                                .padding(.vertical, 40)
                            }
                            
                            // Extracted Text Results
                            ForEach(Array(photoProcessor.extractedTexts.enumerated()), id: \.offset) { index, text in
                                ExtractedTextCard(
                                    text: text,
                                    photoIndex: index,
                                    onDelete: {
                                        photoProcessor.removeText(at: index)
                                    },
                                    onEdit: { newText in
                                        // Handle text editing if needed
                                    }
                                )
                            }
                        }
                        .padding(.horizontal)
                        .padding(.bottom, 100) // Space for floating action button
                    }
                }
            }
            .navigationBarHidden(true)
        }
        .sheet(isPresented: $showingLanguageSelector) {
            LanguageSelector(selectedLanguage: $selectedLanguage)
        }
        .sheet(isPresented: $showingExportOptions) {
            ExportOptionsView(extractedTexts: photoProcessor.extractedTexts)
        }
        .alert("Error", isPresented: $photoProcessor.showingError) {
            Button("OK") { }
        } message: {
            Text(photoProcessor.errorMessage)
        }
        .overlay(
            // Floating Action Button
            VStack {
                Spacer()
                
                if !photoProcessor.extractedTexts.isEmpty {
                    HStack {
                        Spacer()
                        
                        Button(action: {
                            showingExportOptions = true
                        }) {
                            HStack(spacing: 8) {
                                Image(systemName: "square.and.arrow.up")
                                    .font(.title2)
                                Text("Export")
                                    .font(.headline)
                            }
                            .foregroundColor(.white)
                            .padding(.horizontal, 24)
                            .padding(.vertical, 16)
                            .background(Color.blue)
                            .cornerRadius(25)
                            .shadow(color: .black.opacity(0.2), radius: 8, x: 0, y: 4)
                        }
                        .padding(.trailing, 20)
                        .padding(.bottom, 20)
                    }
                }
            }
        )
    }
}

struct ExtractedTextCard: View {
    let text: String
    let photoIndex: Int
    let onDelete: () -> Void
    let onEdit: (String) -> Void
    
    @State private var isExpanded = false
    @State private var showingDeleteAlert = false
    
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            // Header
            HStack {
                HStack(spacing: 8) {
                    Image(systemName: "photo")
                        .foregroundColor(.blue)
                        .font(.title3)
                    
                    Text("Photo \(photoIndex + 1)")
                        .font(.headline)
                        .fontWeight(.semibold)
                }
                
                Spacer()
                
                HStack(spacing: 8) {
                    Button(action: {
                        isExpanded.toggle()
                    }) {
                        Image(systemName: isExpanded ? "chevron.up" : "chevron.down")
                            .foregroundColor(.blue)
                            .font(.caption)
                    }
                    
                    Button(action: {
                        showingDeleteAlert = true
                    }) {
                        Image(systemName: "trash")
                            .foregroundColor(.red)
                            .font(.caption)
                    }
                }
            }
            
            // Text Content
            VStack(alignment: .leading, spacing: 8) {
                Text(text)
                    .font(.body)
                    .foregroundColor(.primary)
                    .lineLimit(isExpanded ? nil : 3)
                    .textSelection(.enabled)
                
                if text.count > 150 && !isExpanded {
                    Button("Show more") {
                        isExpanded = true
                    }
                    .font(.caption)
                    .foregroundColor(.blue)
                }
            }
            .padding()
            .background(Color(.systemGray6))
            .cornerRadius(8)
        }
        .padding()
        .background(Color(.systemBackground))
        .cornerRadius(16)
        .shadow(color: .black.opacity(0.1), radius: 4, x: 0, y: 2)
        .alert("Delete Text", isPresented: $showingDeleteAlert) {
            Button("Cancel", role: .cancel) { }
            Button("Delete", role: .destructive) {
                onDelete()
            }
        } message: {
            Text("Are you sure you want to delete the extracted text from Photo \(photoIndex + 1)?")
        }
    }
}

#Preview {
    PhotoOCRView()
}