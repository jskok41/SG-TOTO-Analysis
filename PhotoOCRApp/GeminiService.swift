import Foundation
import UIKit

class GeminiService: ObservableObject {
    private let apiKey = "YOUR_GEMINI_API_KEY" // Replace with actual API key
    private let baseURL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro-vision:generateContent"
    
    func extractText(from image: UIImage, language: String) async -> String {
        guard let imageData = image.jpegData(compressionQuality: 0.8) else {
            return "Failed to process image"
        }
        
        let base64Image = imageData.base64EncodedString()
        
        let prompt = """
        Please extract all the text from this image. 
        Focus on business documents, forms, receipts, or any text content.
        Return only the extracted text without any additional commentary.
        If the image contains text in \(getLanguageName(for: language)), please preserve the original language.
        Format the text in a clean, readable manner.
        """
        
        let requestBody = GeminiRequest(
            contents: [
                GeminiContent(
                    parts: [
                        GeminiPart(text: prompt),
                        GeminiPart(
                            inlineData: GeminiInlineData(
                                mimeType: "image/jpeg",
                                data: base64Image
                            )
                        )
                    ]
                )
            ],
            generationConfig: GeminiGenerationConfig(
                temperature: 0.1,
                topK: 32,
                topP: 1,
                maxOutputTokens: 2048
            )
        )
        
        do {
            let jsonData = try JSONEncoder().encode(requestBody)
            let url = URL(string: "\(baseURL)?key=\(apiKey)")!
            
            var request = URLRequest(url: url)
            request.httpMethod = "POST"
            request.setValue("application/json", forHTTPHeaderField: "Content-Type")
            request.httpBody = jsonData
            
            let (data, response) = try await URLSession.shared.data(for: request)
            
            guard let httpResponse = response as? HTTPURLResponse,
                  httpResponse.statusCode == 200 else {
                return "Failed to get response from Gemini API"
            }
            
            let geminiResponse = try JSONDecoder().decode(GeminiResponse.self, from: data)
            
            if let text = geminiResponse.candidates?.first?.content?.parts?.first?.text {
                return text.trimmingCharacters(in: .whitespacesAndNewlines)
            } else {
                return "No text extracted from image"
            }
            
        } catch {
            return "Error processing image: \(error.localizedDescription)"
        }
    }
    
    private func getLanguageName(for code: String) -> String {
        switch code {
        case "en": return "English"
        case "es": return "Spanish"
        case "fr": return "French"
        case "de": return "German"
        case "it": return "Italian"
        case "pt": return "Portuguese"
        case "ru": return "Russian"
        case "ja": return "Japanese"
        case "ko": return "Korean"
        case "zh": return "Chinese"
        default: return "English"
        }
    }
}

// MARK: - Gemini API Models

struct GeminiRequest: Codable {
    let contents: [GeminiContent]
    let generationConfig: GeminiGenerationConfig
}

struct GeminiContent: Codable {
    let parts: [GeminiPart]
}

struct GeminiPart: Codable {
    let text: String?
    let inlineData: GeminiInlineData?
    
    init(text: String) {
        self.text = text
        self.inlineData = nil
    }
    
    init(inlineData: GeminiInlineData) {
        self.text = nil
        self.inlineData = inlineData
    }
}

struct GeminiInlineData: Codable {
    let mimeType: String
    let data: String
}

struct GeminiGenerationConfig: Codable {
    let temperature: Double
    let topK: Int
    let topP: Double
    let maxOutputTokens: Int
}

struct GeminiResponse: Codable {
    let candidates: [GeminiCandidate]?
}

struct GeminiCandidate: Codable {
    let content: GeminiContent?
}

// MARK: - Mock Service for Development

class MockGeminiService: ObservableObject {
    func extractText(from image: UIImage, language: String) async -> String {
        // Simulate API delay
        try? await Task.sleep(nanoseconds: 2_000_000_000) // 2 seconds
        
        // Return mock extracted text
        return """
        Sample Business Document
        
        Invoice #: INV-2024-001
        Date: January 15, 2024
        Due Date: February 15, 2024
        
        Customer: ABC Company
        Address: 123 Business St, City, State 12345
        
        Items:
        1. Product A - $100.00
        2. Product B - $250.00
        3. Service C - $75.00
        
        Subtotal: $425.00
        Tax (8.5%): $36.13
        Total: $461.13
        
        Payment Terms: Net 30
        """
    }
}