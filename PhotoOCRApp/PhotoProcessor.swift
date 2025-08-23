import SwiftUI
import PhotosUI
import Vision

@MainActor
class PhotoProcessor: ObservableObject {
    @Published var extractedTexts: [String] = []
    @Published var isProcessing = false
    @Published var showingError = false
    @Published var errorMessage = ""
    
    private let geminiService = GeminiService()
    
    func processPhotos(from items: [PhotosPickerItem], language: String) async {
        guard !items.isEmpty else { return }
        
        isProcessing = true
        extractedTexts.removeAll()
        
        do {
            for item in items {
                if let data = try await item.loadTransferable(type: Data.self),
                   let image = UIImage(data: data) {
                    
                    // First try Vision framework for basic OCR
                    let visionText = await extractTextWithVision(from: image)
                    
                    if !visionText.isEmpty {
                        extractedTexts.append(visionText)
                    } else {
                        // Fallback to Gemini AI for better accuracy
                        let geminiText = await geminiService.extractText(from: image, language: language)
                        extractedTexts.append(geminiText)
                    }
                }
            }
        } catch {
            errorMessage = "Failed to process photos: \(error.localizedDescription)"
            showingError = true
        }
        
        isProcessing = false
    }
    
    private func extractTextWithVision(from image: UIImage) async -> String {
        guard let cgImage = image.cgImage else { return "" }
        
        let request = VNRecognizeTextRequest { request, error in
            // Handle completion
        }
        
        request.recognitionLevel = .accurate
        request.usesLanguageCorrection = true
        
        let handler = VNImageRequestHandler(cgImage: cgImage, options: [:])
        
        do {
            try handler.perform([request])
            
            guard let observations = request.results as? [VNRecognizedTextObservation] else {
                return ""
            }
            
            let recognizedStrings = observations.compactMap { observation in
                observation.topCandidates(1).first?.string
            }
            
            return recognizedStrings.joined(separator: "\n")
        } catch {
            return ""
        }
    }
    
    func removeText(at index: Int) {
        guard index < extractedTexts.count else { return }
        extractedTexts.remove(at: index)
    }
    
    func clearAllTexts() {
        extractedTexts.removeAll()
    }
    
    func getCombinedText() -> String {
        return extractedTexts.enumerated().map { index, text in
            "Photo \(index + 1):\n\(text)"
        }.joined(separator: "\n\n")
    }
}