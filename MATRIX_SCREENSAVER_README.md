# Matrix Screensaver for iPhone 15 Pro Max iOS 26 🕶️

A stunning Matrix-style screensaver optimized specifically for iPhone 15 Pro Max running iOS 26. Features authentic falling character effects, customizable settings, and full PWA support for seamless lock screen integration.

## ✨ Features

### 🎬 Matrix Effects
- **Authentic Matrix Rain**: Falling characters with realistic physics
- **Glitch Effects**: Random character changes for authentic Matrix feel
- **Trail Effects**: Character fading and opacity animations
- **Customizable Speed**: Adjustable falling speed (1-10x)
- **Density Control**: Variable character density (10-100%)

### 📱 iPhone 15 Pro Max Optimizations
- **Perfect Resolution**: Optimized for 430x932px display
- **Safe Area Support**: Respects iPhone notch and home indicator
- **Orientation Support**: Works in both portrait and landscape
- **Touch to Wake**: Tap anywhere to wake from pause/lock
- **iOS 26 Features**: Latest iOS optimizations and PWA support

### ⚙️ Customization Options
- **Speed Control**: Adjust falling speed
- **Density Settings**: Control character density
- **Character Size**: Resize characters (8-24px)
- **Color Picker**: Customize Matrix green color
- **Fade Speed**: Control character fade rate
- **Glitch Toggle**: Enable/disable glitch effects
- **Auto-lock**: Automatic lock after 30 seconds

### 🔒 Lock Screen Integration
- **PWA Support**: Install as home screen app
- **Fullscreen Mode**: True fullscreen experience
- **Lock Function**: Manual lock with touch-to-wake
- **Background Sync**: Service worker for offline functionality
- **Status Bar**: iOS-style status bar integration

## 🚀 Installation

### Method 1: Direct Installation
1. Open `matrix-screensaver-ios26.html` in Safari on your iPhone 15 Pro Max
2. Tap the Share button
3. Select "Add to Home Screen"
4. The Matrix Screensaver will be installed as a PWA

### Method 2: Web Server Installation
1. Upload all files to a web server
2. Access via HTTPS (required for PWA)
3. Open in Safari and add to home screen

### Method 3: Local Development
1. Serve files using a local web server:
   ```bash
   # Using Python
   python -m http.server 8000
   
   # Using Node.js
   npx serve .
   
   # Using PHP
   php -S localhost:8000
   ```
2. Access via `http://localhost:8000/matrix-screensaver-ios26.html`

## 📖 Usage

### Basic Controls
- **Tap Screen**: Wake from pause/lock
- **Pause Button**: Pause/resume animation
- **Settings Button**: Open configuration panel
- **Fullscreen Button**: Toggle fullscreen mode
- **Lock Button**: Lock screensaver (tap to unlock)

### Settings Panel
- **Speed**: Adjust falling speed (1-10)
- **Density**: Control character density (10-100)
- **Character Size**: Resize characters (8-24px)
- **Color**: Customize Matrix color
- **Fade Speed**: Control fade rate (1-20)
- **Glitch Effect**: Toggle random character changes
- **Auto-lock**: Enable automatic locking

### Lock Screen Mode
1. Tap the Lock button to enter lock mode
2. Controls will be hidden
3. Tap anywhere on screen to unlock
4. Perfect for true screensaver experience

## 🛠️ Technical Details

### Browser Compatibility
- **Safari**: Full support (recommended)
- **Chrome**: Full support
- **Firefox**: Full support
- **Edge**: Full support

### Performance Optimizations
- **Canvas Rendering**: Hardware-accelerated graphics
- **RequestAnimationFrame**: Smooth 60fps animation
- **Memory Management**: Efficient drop recycling
- **Touch Optimization**: Responsive touch handling

### iOS 26 Specific Features
- **Safe Area Insets**: Proper notch handling
- **Orientation Change**: Smooth rotation support
- **Background App Refresh**: PWA background sync
- **Touch Events**: Optimized touch handling
- **Viewport Meta**: Perfect viewport configuration

## 📁 File Structure

```
matrix-screensaver/
├── matrix-screensaver.html          # Basic version
├── matrix-screensaver-ios26.html    # iOS 26 optimized version
├── manifest.json                    # PWA manifest
├── sw.js                           # Service worker
└── MATRIX_SCREENSAVER_README.md    # This file
```

## 🎨 Customization

### Color Themes
The screensaver supports custom colors via the color picker:
- **Classic Green**: `#00ff00` (default)
- **Neon Blue**: `#0080ff`
- **Purple**: `#8000ff`
- **Red**: `#ff0000`
- **White**: `#ffffff`

### Character Sets
The screensaver includes multiple character sets:
- **Alphanumeric**: A-Z, 0-9
- **Symbols**: @#$%^&*()_+-=[]{}|;:,.<>?
- **Japanese**: アイウエオカキクケコ... (iOS 26 bonus)

### Performance Tuning
For optimal performance on iPhone 15 Pro Max:
- **Density**: 50-70 for smooth performance
- **Speed**: 3-7 for balanced effect
- **Character Size**: 12-16px for clarity
- **Fade Speed**: 8-12 for smooth transitions

## 🔧 Troubleshooting

### Common Issues

**Screensaver not animating:**
- Check if paused (tap to resume)
- Verify JavaScript is enabled
- Try refreshing the page

**Controls not responding:**
- Ensure touch events are working
- Check if in lock mode (tap to unlock)
- Verify PWA installation

**Performance issues:**
- Reduce density setting
- Lower character size
- Disable glitch effects
- Close other apps

**Fullscreen not working:**
- Ensure HTTPS connection
- Check browser permissions
- Try manual fullscreen button

### iOS Specific Issues

**Not installing as PWA:**
- Use Safari browser
- Ensure HTTPS connection
- Check "Add to Home Screen" option

**Safe area issues:**
- Update to iOS 26
- Check viewport settings
- Verify device orientation

## 🚀 Advanced Features

### Service Worker
The included service worker provides:
- **Offline Support**: Works without internet
- **Background Sync**: Updates in background
- **Cache Management**: Efficient resource caching
- **Push Notifications**: Future enhancement support

### PWA Manifest
Full PWA support with:
- **App Icons**: Custom Matrix-themed icons
- **Splash Screen**: Matrix loading screen
- **Shortcuts**: Quick access from home screen
- **Display Mode**: Fullscreen experience

## 📱 iPhone 15 Pro Max Specific

### Display Optimization
- **Resolution**: 430x932px perfect fit
- **Aspect Ratio**: 19.5:9 optimized
- **Safe Areas**: Notch and home indicator support
- **Orientation**: Portrait and landscape support

### Performance
- **A17 Pro Chip**: Optimized for latest processor
- **8GB RAM**: Efficient memory usage
- **120Hz ProMotion**: Smooth animation support
- **iOS 26**: Latest iOS optimizations

## 🔮 Future Enhancements

- **Sound Effects**: Matrix-style audio
- **Multiple Themes**: Different Matrix variations
- **Gesture Controls**: Swipe gestures
- **Time Display**: Clock overlay option
- **Weather Integration**: Weather data display
- **Notifications**: Custom notification styles

## 📄 License

MIT License - Feel free to modify and distribute.

## 🤝 Contributing

Contributions welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📞 Support

For support or questions:
- Open an issue on GitHub
- Check the troubleshooting section
- Review the technical documentation

---

**Enjoy your Matrix Screensaver on iPhone 15 Pro Max iOS 26!** 🕶️✨