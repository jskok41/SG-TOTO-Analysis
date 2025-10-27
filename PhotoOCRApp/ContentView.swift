import SwiftUI
import PhotosUI

struct ContentView: View {
    @StateObject private var photoProcessor = PhotoProcessor()
    @State private var selectedPhotos: [PhotosPickerItem] = []
    @State private var showingLanguageSelector = false
    @State private var showingExportOptions = false
    @State private var selectedLanguage = "en"
    
    var body: some View {
        NavigationView {
            VStack(spacing: 20) {
                // Header
                VStack(spacing: 8) {
                    Image(systemName: "doc.text.viewfinder")
                        .font(.system(size: 60))
                        .foregroundColor(.blue)
                    
                    Text("Photo OCR")
                        .font(.largeTitle)
                        .fontWeight(.bold)
                    
                    Text("Extract text from photos automatically")
                        .font(.subheadline)
                        .foregroundColor(.secondary)
                        .multilineTextAlignment(.center)
                }
                .padding(.top, 20)
                
                // Language Selection
                HStack {
                    Text("Language:")
                        .font(.headline)
                    
                    Button(action: {
                        showingLanguageSelector = true
                    }) {
                        HStack {
                            Text(LanguageSelector.getLanguageName(for: selectedLanguage))
                                .foregroundColor(.primary)
                            Image(systemName: "chevron.down")
                                .foregroundColor(.blue)
                        }
                        .padding(.horizontal, 16)
                        .padding(.vertical, 8)
                        .background(Color(.systemGray6))
                        .cornerRadius(8)
                    }
                }
                .padding(.horizontal)
                
                // Photo Picker
                PhotosPicker(
                    selection: $selectedPhotos,
                    maxSelectionCount: 10,
                    matching: .images
                ) {
                    HStack {
                        Image(systemName: "photo.on.rectangle.angled")
                            .font(.title2)
                        Text("Select Photos")
                            .font(.headline)
                    }
                    .foregroundColor(.white)
                    .frame(maxWidth: .infinity)
                    .padding()
                    .background(Color.blue)
                    .cornerRadius(12)
                }
                .padding(.horizontal)
                .onChange(of: selectedPhotos) { newItems in
                    Task {
                        await photoProcessor.processPhotos(from: newItems, language: selectedLanguage)
                    }
                }
                
                // Processing Status
                if photoProcessor.isProcessing {
                    VStack(spacing: 8) {
                        ProgressView()
                            .scaleEffect(1.2)
                        Text("Processing photos...")
                            .font(.subheadline)
                            .foregroundColor(.secondary)
                    }
                    .padding()
                }
                
                // Results
                if !photoProcessor.extractedTexts.isEmpty {
                    ScrollView {
                        LazyVStack(spacing: 16) {
                            ForEach(Array(photoProcessor.extractedTexts.enumerated()), id: \.offset) { index, text in
                                ExtractedTextView(
                                    text: text,
                                    photoIndex: index,
                                    onDelete: {
                                        photoProcessor.removeText(at: index)
                                    }
                                )
                            }
                        }
                        .padding(.horizontal)
                    }
                    
                    // Export Button
                    Button(action: {
                        showingExportOptions = true
                    }) {
                        HStack {
                            Image(systemName: "square.and.arrow.up")
                                .font(.title2)
                            Text("Export Results")
                                .font(.headline)
                        }
                        .foregroundColor(.white)
                        .frame(maxWidth: .infinity)
                        .padding()
                        .background(Color.green)
                        .cornerRadius(12)
                    }
                    .padding(.horizontal)
                }
                
                Spacer()
            }
            .navigationTitle("")
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
    }
}

struct ExtractedTextView: View {
    let text: String
    let photoIndex: Int
    let onDelete: () -> Void
    
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            HStack {
                Text("Photo \(photoIndex + 1)")
                    .font(.headline)
                    .foregroundColor(.primary)
                
                Spacer()
                
                Button(action: onDelete) {
                    Image(systemName: "trash")
                        .foregroundColor(.red)
                }
            }
            
            Text(text)
                .font(.body)
                .foregroundColor(.primary)
                .padding()
                .background(Color(.systemGray6))
                .cornerRadius(8)
                .textSelection(.enabled)
        }
        .padding()
        .background(Color(.systemBackground))
        .cornerRadius(12)
        .shadow(color: .black.opacity(0.1), radius: 2, x: 0, y: 1)
    }
}

#Preview {
    ContentView()
}