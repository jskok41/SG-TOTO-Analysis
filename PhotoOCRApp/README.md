# Photo OCR App

A professional iOS app for iPhone 15 that automates data entry by extracting text from photos using advanced OCR technology and Gemini AI.

## Features

### 🖼️ Photo Management
- **Batch Photo Upload**: Select multiple photos (up to 10) from Photos Album or Gallery
- **Photo Preview**: View uploaded photos before processing
- **Camera Integration**: Take new photos directly within the app

### 🤖 AI-Powered Text Extraction
- **Gemini AI Integration**: Uses Google's Gemini AI API for high-accuracy text extraction
- **Vision Framework Fallback**: Apple's native OCR as backup for faster processing
- **Multi-language Support**: OCR support for 20+ languages including:
  - English, Spanish, French, German, Italian
  - Portuguese, Russian, Japanese, Korean, Chinese
  - Arabic, Hindi, Dutch, Swedish, Norwegian
  - Danish, Finnish, Polish, Turkish, Hebrew

### 📤 Export Options
- **Copy to Clipboard**: Quick text copying for immediate use
- **Save to Files**: Export as text file to iOS Files app
- **Email Sharing**: Send extracted text via email
- **System Share Sheet**: Use native iOS sharing options

### 🎨 User Experience
- **Apple Human Interface Guidelines**: Follows iOS design principles
- **Responsive Design**: Optimized for iPhone 15 and other iOS devices
- **Dark Mode Support**: Automatic adaptation to system appearance
- **Accessibility**: VoiceOver and Dynamic Type support

## Technical Architecture

### Core Components
- **ContentView**: Main app interface and navigation
- **PhotoProcessor**: Manages photo processing and OCR coordination
- **GeminiService**: Handles AI API communication
- **LanguageSelector**: Language selection interface
- **ExportOptionsView**: Export functionality
- **PhotoOCRView**: Enhanced photo processing interface

### Technologies Used
- **SwiftUI**: Modern declarative UI framework
- **PhotosUI**: Native photo selection and management
- **Vision Framework**: Apple's OCR capabilities
- **Gemini AI API**: Google's advanced text extraction
- **MessageUI**: Email composition
- **UIKit Integration**: Camera and sharing functionality

## Setup Instructions

### Prerequisites
- Xcode 15.0 or later
- iOS 17.0+ deployment target
- iPhone 15 or compatible iOS device
- Gemini AI API key

### Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd PhotoOCRApp
   ```

2. **Open in Xcode**
   - Open `PhotoOCRApp.xcodeproj` in Xcode
   - Select your development team
   - Choose target device (iPhone 15 recommended)

3. **Configure Gemini API**
   - Open `GeminiService.swift`
   - Replace `YOUR_GEMINI_API_KEY` with your actual API key
   - Get API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

4. **Build and Run**
   - Press `Cmd + R` to build and run
   - Grant necessary permissions (Photos, Camera)

### API Key Setup

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key and paste it in `GeminiService.swift`
4. Ensure the key has access to Gemini Pro Vision model

## Usage Guide

### Basic Workflow

1. **Launch the App**
   - App opens to main interface
   - Select language for OCR processing

2. **Select Photos**
   - Tap "Photos" to select from library
   - Tap "Camera" to take new photos
   - Choose up to 10 photos

3. **Process Photos**
   - App automatically processes selected photos
   - Progress indicator shows processing status
   - Results appear as individual text cards

4. **Review and Export**
   - Review extracted text for accuracy
   - Use export options to save or share
   - Delete individual results if needed

### Language Selection

- Tap language selector in header
- Choose from 20+ supported languages
- Language affects OCR accuracy and processing
- Can be changed before processing new photos

### Export Options

- **Copy to Clipboard**: Instant text copying
- **Save to Files**: Creates .txt file in Files app
- **Email**: Opens mail composer with extracted text
- **Share**: Uses iOS native sharing options

## Business Use Cases

### Data Entry Automation
- **Invoice Processing**: Extract data from receipts and invoices
- **Form Digitization**: Convert paper forms to digital text
- **Document Archiving**: Create searchable text from scanned documents
- **Business Card Scanning**: Extract contact information

### Compliance and Records
- **Receipt Management**: Automate expense reporting
- **Contract Review**: Extract key terms from documents
- **Regulatory Compliance**: Process compliance documents
- **Audit Trails**: Create searchable audit records

## Performance Considerations

### Processing Speed
- **Vision Framework**: Fast processing for simple text
- **Gemini AI**: Higher accuracy, moderate processing time
- **Batch Processing**: Efficient handling of multiple photos
- **Background Processing**: Non-blocking UI during OCR

### Accuracy Optimization
- **Image Quality**: Higher resolution improves accuracy
- **Text Clarity**: Clear, well-lit photos work best
- **Language Selection**: Correct language improves results
- **Multiple Attempts**: Retry with different settings if needed

## Privacy and Security

### Data Handling
- **Local Processing**: Photos processed on device when possible
- **Secure API**: HTTPS communication with Gemini AI
- **No Storage**: Photos not permanently stored in app
- **User Control**: Full control over photo selection and deletion

### Permissions
- **Photos**: Access to photo library for selection
- **Camera**: Camera access for new photos
- **Network**: Internet access for AI API calls

## Troubleshooting

### Common Issues

1. **API Key Errors**
   - Verify API key is correct
   - Check API key permissions
   - Ensure internet connectivity

2. **Photo Processing Failures**
   - Check photo format (JPEG/PNG supported)
   - Verify photo quality and clarity
   - Try different language settings

3. **Export Issues**
   - Check app permissions
   - Verify available storage space
   - Ensure email account is configured

### Performance Tips

- Use good lighting for photos
- Ensure text is clearly visible
- Select appropriate language
- Process photos in smaller batches

## Future Enhancements

### Planned Features
- **Cloud Sync**: iCloud integration for results
- **Advanced Export**: PDF and Word document export
- **Batch Renaming**: Automatic file naming
- **OCR History**: Processing history and search
- **Custom Templates**: Business-specific extraction rules

### API Improvements
- **Offline Mode**: Enhanced local processing
- **Multiple AI Providers**: Fallback options
- **Real-time Processing**: Live camera OCR
- **Advanced Analytics**: Processing statistics

## Support and Feedback

### Getting Help
- Check this README for common solutions
- Review Apple's Human Interface Guidelines
- Consult Gemini AI API documentation

### Contributing
- Follow SwiftUI best practices
- Maintain accessibility standards
- Test on multiple device sizes
- Update documentation for changes

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Apple for SwiftUI and Vision Framework
- Google for Gemini AI API
- iOS development community for best practices
- Apple Human Interface Guidelines for design principles

---

**Note**: This app requires an active internet connection for Gemini AI functionality. For offline use, the app falls back to Apple's Vision Framework for basic OCR capabilities.