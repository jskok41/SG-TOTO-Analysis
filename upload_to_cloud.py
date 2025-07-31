#!/usr/bin/env python3
"""
SG TOTO Analysis - Cloud Upload Helper
This script provides instructions for uploading files to cloud storage for mobile access
"""

import os
import subprocess
import webbrowser
from datetime import datetime

def check_file_exists(file_path):
    """Check if file exists and return its size"""
    if os.path.exists(file_path):
        size = os.path.getsize(file_path)
        size_mb = size / (1024 * 1024)
        return True, size_mb
    return False, 0

def create_upload_instructions():
    """Create instructions for uploading files to cloud storage"""
    
    instructions = f"""
# 📱 Mobile Access Solutions for SG TOTO Analysis

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 🎯 Available Files for Upload

"""
    
    # List all important files
    files_to_upload = [
        'SG-TOTO-Analysis-Complete-Package.zip',
        'SG-TOTO-Analysis-Complete-Package.tar.gz',
        'shareable_downloads.html',
        'mobile_download.html',
        'download-package/README_DOWNLOAD.md',
        'DOWNLOAD_SUMMARY.md'
    ]
    
    for file_path in files_to_upload:
        exists, size = check_file_exists(file_path)
        if exists:
            instructions += f"- **{file_path}** ({size:.1f} MB)\n"
        else:
            instructions += f"- **{file_path}** (File not found)\n"
    
    instructions += """

## 🌐 Cloud Storage Options

### Option 1: Google Drive
1. Go to https://drive.google.com
2. Click "New" → "File upload"
3. Select the ZIP file (SG-TOTO-Analysis-Complete-Package.zip)
4. Right-click the uploaded file → "Get link"
5. Share the link with your mobile device

### Option 2: Dropbox
1. Go to https://www.dropbox.com
2. Drag and drop the ZIP file
3. Right-click the file → "Share" → "Create a link"
4. Copy the link for mobile access

### Option 3: OneDrive
1. Go to https://onedrive.live.com
2. Upload the ZIP file
3. Right-click → "Share" → "Copy link"
4. Share with your mobile device

### Option 4: WeTransfer (Temporary)
1. Go to https://wetransfer.com
2. Upload the ZIP file
3. Enter your email address
4. Send the link to yourself
5. Access from mobile device

### Option 5: File.io (Temporary)
1. Go to https://file.io
2. Drag and drop the ZIP file
3. Copy the generated link
4. Share with mobile device (link expires after download)

## 📱 Mobile Download Instructions

### For Android:
1. Open the cloud storage link in Chrome/Samsung Internet
2. Tap the download button
3. Wait for download to complete
4. Use a file manager to extract the ZIP file
5. Transfer to computer via USB or email

### For iPhone:
1. Open the cloud storage link in Safari
2. Tap the download button
3. The file will be saved to Files app
4. Share via AirDrop, email, or cloud storage
5. Transfer to computer for extraction

## 🔧 Alternative Methods

### Method 1: Email Transfer
1. Download the ZIP file to your computer
2. Email it to yourself as an attachment
3. Open the email on your mobile device
4. Download the attachment
5. Transfer back to computer

### Method 2: USB Transfer
1. Download the ZIP file to your computer
2. Connect your mobile device via USB
3. Transfer the file to your mobile device
4. Use mobile file manager to access
5. Transfer back to computer when needed

### Method 3: Local Network Transfer
1. Enable file sharing on your computer
2. Connect both devices to the same WiFi network
3. Use apps like "Send Anywhere" or "AirDroid"
4. Transfer the ZIP file between devices

## 📋 File Information

### Complete Package (Recommended):
- **SG-TOTO-Analysis-Complete-Package.zip** (11.3 MB)
  - Contains all 98 project files
  - Includes Python scripts, web apps, data files
  - Ready-to-use with setup scripts

### Individual Components:
- **shareable_downloads.html** - Self-contained download page
- **mobile_download.html** - Mobile-optimized download page
- **README_DOWNLOAD.md** - Complete setup guide
- **requirements.txt** - Python dependencies

## 🚀 Quick Setup After Download

1. **Extract the ZIP file** on your computer
2. **Open terminal/command prompt**
3. **Navigate to the extracted folder**
4. **Install dependencies**: `pip install -r requirements.txt`
5. **Run analysis**: `python main.py`
6. **Launch web app**: `cd toto-web-app && npm run dev`

## 📞 Troubleshooting

### If download fails:
- Try a different cloud storage service
- Check your internet connection
- Ensure you have enough storage space
- Try downloading individual files instead of the complete package

### If extraction fails:
- Ensure you have a ZIP extractor installed
- Try using 7-Zip or WinRAR
- Check if the file downloaded completely
- Verify the file size matches the expected size

### If setup fails:
- Ensure Python 3.8+ is installed
- Check that pip is available
- Install Node.js 16+ for web app
- Follow the README_DOWNLOAD.md instructions

## 🎉 Success!

Once you have the files on your computer, you'll have access to:
- Complete TOTO analysis system
- Web scraping tools
- Statistical modeling
- Interactive web application
- Historical data analysis
- Automated reporting

Happy analyzing! 🎯
"""
    
    # Write instructions to file
    with open('MOBILE_ACCESS_INSTRUCTIONS.md', 'w', encoding='utf-8') as f:
        f.write(instructions)
    
    print("✅ Created MOBILE_ACCESS_INSTRUCTIONS.md")
    print("📱 This file contains detailed instructions for mobile access")
    print("🌐 Includes multiple cloud storage options and transfer methods")

def open_cloud_services():
    """Open popular cloud storage services in browser"""
    services = [
        "https://drive.google.com",
        "https://www.dropbox.com",
        "https://onedrive.live.com",
        "https://wetransfer.com",
        "https://file.io"
    ]
    
    print("🌐 Opening cloud storage services...")
    for service in services:
        try:
            webbrowser.open(service)
            print(f"✅ Opened: {service}")
        except Exception as e:
            print(f"❌ Could not open {service}: {e}")

if __name__ == "__main__":
    create_upload_instructions()
    
    # Ask user if they want to open cloud services
    response = input("🌐 Would you like to open cloud storage services in your browser? (y/n): ")
    if response.lower() in ['y', 'yes']:
        open_cloud_services()
    
    print("\n📱 Mobile access instructions created!")
    print("📄 Check MOBILE_ACCESS_INSTRUCTIONS.md for detailed steps")
    print("🎯 You can now upload files to any cloud service for mobile access")