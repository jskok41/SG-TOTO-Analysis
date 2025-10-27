import SwiftUI
import MessageUI

struct ExportOptionsView: View {
    let extractedTexts: [String]
    @Environment(\.dismiss) private var dismiss
    @State private var showingMailComposer = false
    @State private var showingShareSheet = false
    @State private var showingSaveDialog = false
    @State private var showingSuccessAlert = false
    @State private var successMessage = ""
    
    private var combinedText: String {
        extractedTexts.enumerated().map { index, text in
            "Photo \(index + 1):\n\(text)"
        }.joined(separator: "\n\n")
    }
    
    var body: some View {
        NavigationView {
            List {
                Section {
                    VStack(alignment: .leading, spacing: 8) {
                        Text("Export Options")
                            .font(.headline)
                            .foregroundColor(.primary)
                        
                        Text("\(extractedTexts.count) photos processed")
                            .font(.subheadline)
                            .foregroundColor(.secondary)
                        
                        Text("Total characters: \(combinedText.count)")
                            .font(.caption)
                            .foregroundColor(.secondary)
                    }
                    .padding(.vertical, 8)
                }
                
                Section("Export Methods") {
                    // Copy to Clipboard
                    Button(action: copyToClipboard) {
                        HStack {
                            Image(systemName: "doc.on.clipboard")
                                .foregroundColor(.blue)
                                .font(.title2)
                            
                            VStack(alignment: .leading, spacing: 2) {
                                Text("Copy to Clipboard")
                                    .font(.headline)
                                    .foregroundColor(.primary)
                                Text("Copy all extracted text to clipboard")
                                    .font(.caption)
                                    .foregroundColor(.secondary)
                            }
                            
                            Spacer()
                            
                            Image(systemName: "chevron.right")
                                .foregroundColor(.secondary)
                                .font(.caption)
                        }
                    }
                    .buttonStyle(PlainButtonStyle())
                    
                    // Save to File
                    Button(action: { showingSaveDialog = true }) {
                        HStack {
                            Image(systemName: "folder.badge.plus")
                                .foregroundColor(.green)
                                .font(.title2)
                            
                            VStack(alignment: .leading, spacing: 2) {
                                Text("Save to File")
                                    .font(.headline)
                                    .foregroundColor(.primary)
                                Text("Save as text file to Files app")
                                    .font(.caption)
                                    .foregroundColor(.secondary)
                            }
                            
                            Spacer()
                            
                            Image(systemName: "chevron.right")
                                .foregroundColor(.secondary)
                                .font(.caption)
                        }
                    }
                    .buttonStyle(PlainButtonStyle())
                    
                    // Share via Email
                    Button(action: { showingMailComposer = true }) {
                        HStack {
                            Image(systemName: "envelope")
                                .foregroundColor(.orange)
                                .font(.title2)
                            
                            VStack(alignment: .leading, spacing: 2) {
                                Text("Share via Email")
                                    .font(.headline)
                                    .foregroundColor(.primary)
                                Text("Send extracted text via email")
                                    .font(.caption)
                                    .foregroundColor(.secondary)
                            }
                            
                            Spacer()
                            
                            Image(systemName: "chevron.right")
                                .foregroundColor(.secondary)
                                .font(.caption)
                        }
                    }
                    .buttonStyle(PlainButtonStyle())
                    .disabled(!MFMailComposeViewController.canSendMail())
                    
                    // Share Sheet
                    Button(action: { showingShareSheet = true }) {
                        HStack {
                            Image(systemName: "square.and.arrow.up")
                                .foregroundColor(.purple)
                                .font(.title2)
                            
                            VStack(alignment: .leading, spacing: 2) {
                                Text("Share")
                                    .font(.headline)
                                    .foregroundColor(.primary)
                                Text("Use system share sheet")
                                    .font(.caption)
                                    .foregroundColor(.secondary)
                            }
                            
                            Spacer()
                            
                            Image(systemName: "chevron.right")
                                .foregroundColor(.secondary)
                                .font(.caption)
                        }
                    }
                    .buttonStyle(PlainButtonStyle())
                }
                
                Section("Preview") {
                    ScrollView {
                        Text(combinedText)
                            .font(.caption)
                            .foregroundColor(.primary)
                            .padding()
                            .background(Color(.systemGray6))
                            .cornerRadius(8)
                            .textSelection(.enabled)
                    }
                    .frame(maxHeight: 200)
                }
            }
            .navigationTitle("Export Options")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button("Done") {
                        dismiss()
                    }
                }
            }
        }
        .sheet(isPresented: $showingMailComposer) {
            MailComposeView(
                subject: "Extracted Text from Photos",
                body: combinedText,
                isPresented: $showingMailComposer
            )
        }
        .sheet(isPresented: $showingShareSheet) {
            ShareSheet(activityItems: [combinedText])
        }
        .alert("Success", isPresented: $showingSuccessAlert) {
            Button("OK") { }
        } message: {
            Text(successMessage)
        }
    }
    
    private func copyToClipboard() {
        UIPasteboard.general.string = combinedText
        successMessage = "Text copied to clipboard successfully!"
        showingSuccessAlert = true
    }
}

// MARK: - Mail Compose View

struct MailComposeView: UIViewControllerRepresentable {
    let subject: String
    let body: String
    @Binding var isPresented: Bool
    
    func makeUIViewController(context: Context) -> MFMailComposeViewController {
        let mailComposer = MFMailComposeViewController()
        mailComposer.mailComposeDelegate = context.coordinator
        mailComposer.setSubject(subject)
        mailComposer.setMessageBody(body, isHTML: false)
        return mailComposer
    }
    
    func updateUIViewController(_ uiViewController: MFMailComposeViewController, context: Context) {}
    
    func makeCoordinator() -> Coordinator {
        Coordinator(self)
    }
    
    class Coordinator: NSObject, MFMailComposeViewControllerDelegate {
        let parent: MailComposeView
        
        init(_ parent: MailComposeView) {
            self.parent = parent
        }
        
        func mailComposeController(_ controller: MFMailComposeViewController, didFinishWith result: MFMailComposeResult, error: Error?) {
            parent.isPresented = false
        }
    }
}

// MARK: - Share Sheet

struct ShareSheet: UIViewControllerRepresentable {
    let activityItems: [Any]
    
    func makeUIViewController(context: Context) -> UIActivityViewController {
        let activityViewController = UIActivityViewController(
            activityItems: activityItems,
            applicationActivities: nil
        )
        return activityViewController
    }
    
    func updateUIViewController(_ uiViewController: UIActivityViewController, context: Context) {}
}

#Preview {
    ExportOptionsView(extractedTexts: [
        "Sample text from photo 1",
        "Sample text from photo 2"
    ])
}