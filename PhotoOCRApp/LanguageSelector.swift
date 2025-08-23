import SwiftUI

struct LanguageSelector: View {
    @Binding var selectedLanguage: String
    @Environment(\.dismiss) private var dismiss
    
    private let languages = [
        ("en", "English", "🇺🇸"),
        ("es", "Spanish", "🇪🇸"),
        ("fr", "French", "🇫🇷"),
        ("de", "German", "🇩🇪"),
        ("it", "Italian", "🇮🇹"),
        ("pt", "Portuguese", "🇵🇹"),
        ("ru", "Russian", "🇷🇺"),
        ("ja", "Japanese", "🇯🇵"),
        ("ko", "Korean", "🇰🇷"),
        ("zh", "Chinese", "🇨🇳"),
        ("ar", "Arabic", "🇸🇦"),
        ("hi", "Hindi", "🇮🇳"),
        ("nl", "Dutch", "🇳🇱"),
        ("sv", "Swedish", "🇸🇪"),
        ("no", "Norwegian", "🇳🇴"),
        ("da", "Danish", "🇩🇰"),
        ("fi", "Finnish", "🇫🇮"),
        ("pl", "Polish", "🇵🇱"),
        ("tr", "Turkish", "🇹🇷"),
        ("he", "Hebrew", "🇮🇱")
    ]
    
    var body: some View {
        NavigationView {
            List {
                Section {
                    ForEach(languages, id: \.0) { language in
                        Button(action: {
                            selectedLanguage = language.0
                            dismiss()
                        }) {
                            HStack {
                                Text(language.2)
                                    .font(.title2)
                                
                                VStack(alignment: .leading, spacing: 2) {
                                    Text(language.1)
                                        .font(.headline)
                                        .foregroundColor(.primary)
                                    
                                    Text(language.0.uppercased())
                                        .font(.caption)
                                        .foregroundColor(.secondary)
                                }
                                
                                Spacer()
                                
                                if selectedLanguage == language.0 {
                                    Image(systemName: "checkmark")
                                        .foregroundColor(.blue)
                                        .font(.headline)
                                }
                            }
                            .contentShape(Rectangle())
                        }
                        .buttonStyle(PlainButtonStyle())
                    }
                } header: {
                    Text("Select OCR Language")
                        .font(.headline)
                        .foregroundColor(.primary)
                        .textCase(nil)
                } footer: {
                    Text("Choose the language of the text in your photos for better OCR accuracy.")
                        .font(.caption)
                        .foregroundColor(.secondary)
                }
            }
            .navigationTitle("Language")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button("Done") {
                        dismiss()
                    }
                }
            }
        }
    }
    
    static func getLanguageName(for code: String) -> String {
        let languages = [
            "en": "English",
            "es": "Spanish",
            "fr": "French",
            "de": "German",
            "it": "Italian",
            "pt": "Portuguese",
            "ru": "Russian",
            "ja": "Japanese",
            "ko": "Korean",
            "zh": "Chinese",
            "ar": "Arabic",
            "hi": "Hindi",
            "nl": "Dutch",
            "sv": "Swedish",
            "no": "Norwegian",
            "da": "Danish",
            "fi": "Finnish",
            "pl": "Polish",
            "tr": "Turkish",
            "he": "Hebrew"
        ]
        
        return languages[code] ?? "English"
    }
}

#Preview {
    LanguageSelector(selectedLanguage: .constant("en"))
}