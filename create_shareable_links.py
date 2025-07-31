#!/usr/bin/env python3
"""
SG TOTO Analysis - Shareable Links Generator
This script creates shareable download links for mobile access
"""

import os
import base64
import json
from datetime import datetime

def create_data_uri(file_path):
    """Create a data URI for small files"""
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
            mime_type = get_mime_type(file_path)
            encoded = base64.b64encode(data).decode('utf-8')
            return f"data:{mime_type};base64,{encoded}"
    except Exception as e:
        return f"Error reading file: {e}"

def get_mime_type(file_path):
    """Get MIME type based on file extension"""
    ext = os.path.splitext(file_path)[1].lower()
    mime_types = {
        '.txt': 'text/plain',
        '.md': 'text/markdown',
        '.py': 'text/plain',
        '.json': 'application/json',
        '.html': 'text/html',
        '.css': 'text/css',
        '.js': 'application/javascript',
        '.zip': 'application/zip',
        '.tar.gz': 'application/gzip',
        '.csv': 'text/csv',
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg'
    }
    return mime_types.get(ext, 'application/octet-stream')

def create_shareable_page():
    """Create a shareable HTML page with all download links"""
    
    # List of important files to include
    important_files = [
        'SG-TOTO-Analysis-Complete-Package.zip',
        'SG-TOTO-Analysis-Complete-Package.tar.gz',
        'download-package/README_DOWNLOAD.md',
        'download-package/requirements.txt',
        'download-package/setup.sh',
        'download-package/setup.bat',
        'DOWNLOAD_SUMMARY.md'
    ]
    
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SG TOTO Analysis - Shareable Downloads</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: white;
            padding: 20px;
            margin: 0;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }}
        h1 {{
            text-align: center;
            margin-bottom: 30px;
            font-size: 2.5em;
        }}
        .download-section {{
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 20px;
            margin: 20px 0;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }}
        .download-item {{
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 15px;
            margin: 15px 0;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}
        .file-name {{
            font-weight: bold;
            font-size: 1.1em;
        }}
        .file-size {{
            font-size: 0.9em;
            opacity: 0.8;
        }}
        .download-btn {{
            background: linear-gradient(45deg, #ff6b6b, #ee5a24);
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 25px;
            cursor: pointer;
            font-weight: bold;
            text-decoration: none;
            display: block;
            text-align: center;
            margin: 10px 0;
            transition: all 0.3s ease;
        }}
        .download-btn:hover {{
            transform: scale(1.02);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        }}
        .info-box {{
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 15px;
            margin: 15px 0;
            border-left: 4px solid #00d2d3;
        }}
        .instructions {{
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 15px;
            margin: 15px 0;
        }}
        .instructions ol {{
            margin-left: 20px;
        }}
        .instructions li {{
            margin: 8px 0;
        }}
        .file-content {{
            background: rgba(0, 0, 0, 0.3);
            border-radius: 8px;
            padding: 15px;
            margin: 10px 0;
            font-family: monospace;
            font-size: 0.9em;
            max-height: 300px;
            overflow-y: auto;
            white-space: pre-wrap;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🎯 SG TOTO Analysis</h1>
        <h2 style="text-align: center; margin-bottom: 30px;">Shareable Download Links</h2>
        
        <div class="info-box">
            <h3>📦 Package Information</h3>
            <p>This page contains all the files from the SG TOTO Analysis project. Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.</p>
        </div>

        <div class="download-section">
            <h3>📥 Complete Packages</h3>
            <p>Download the entire project in your preferred format:</p>
    """
    
    # Add download links for each file
    for file_path in important_files:
        if os.path.exists(file_path):
            file_size = os.path.getsize(file_path)
            file_size_mb = file_size / (1024 * 1024)
            
            # Create download link
            if file_path.endswith('.zip') or file_path.endswith('.tar.gz'):
                html_content += f"""
            <div class="download-item">
                <div class="file-name">{file_path}</div>
                <div class="file-size">{file_size_mb:.1f} MB • Complete project package</div>
                <a href="data:application/zip;base64,{base64.b64encode(open(file_path, 'rb').read()).decode('utf-8')}" 
                   class="download-btn" download="{file_path}">
                    📦 Download {file_path.split('.')[-1].upper()}
                </a>
            </div>
                """
            else:
                # For text files, include content directly
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    html_content += f"""
            <div class="download-item">
                <div class="file-name">{file_path}</div>
                <div class="file-size">{file_size_mb:.2f} MB • Text file</div>
                <a href="data:text/plain;base64,{base64.b64encode(content.encode('utf-8')).decode('utf-8')}" 
                   class="download-btn" download="{file_path}">
                    📄 Download {os.path.basename(file_path)}
                </a>
                <details>
                    <summary>View Content</summary>
                    <div class="file-content">{content}</div>
                </details>
            </div>
                    """
                except Exception as e:
                    html_content += f"""
            <div class="download-item">
                <div class="file-name">{file_path}</div>
                <div class="file-size">Error reading file: {e}</div>
            </div>
                    """
    
    # Add instructions
    html_content += """
        </div>

        <div class="download-section">
            <h3>🚀 Setup Instructions</h3>
            <div class="instructions">
                <h4>After downloading:</h4>
                <ol>
                    <li>Extract the ZIP or TAR.GZ file to your computer</li>
                    <li>Open terminal/command prompt</li>
                    <li>Navigate to the extracted folder</li>
                    <li>Install Python dependencies: <code>pip install -r requirements.txt</code></li>
                    <li>Run the analysis: <code>python main.py</code></li>
                    <li>For web app: <code>cd toto-web-app && npm install && npm run dev</code></li>
                </ol>
            </div>
        </div>

        <div class="info-box">
            <h3>📋 Package Contents</h3>
            <p>The complete package includes:</p>
            <ul style="margin-left: 20px;">
                <li>9 Python analysis scripts</li>
                <li>Complete Next.js web application</li>
                <li>Standalone HTML application</li>
                <li>Historical TOTO data files</li>
                <li>Comprehensive documentation</li>
                <li>Automated setup scripts</li>
                <li>98 total files</li>
            </ul>
        </div>

        <div class="info-box">
            <h3>📞 System Requirements</h3>
            <ul style="margin-left: 20px;">
                <li>Python 3.8+ with pip</li>
                <li>4GB RAM for data processing</li>
                <li>2GB disk space</li>
                <li>Node.js 16+ (for web app)</li>
                <li>Modern web browser</li>
            </ul>
        </div>
    </div>
</body>
</html>
    """
    
    # Write the HTML file
    with open('shareable_downloads.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✅ Created shareable_downloads.html")
    print("📱 You can now open this file in any browser and share it with your mobile device")
    print("🔗 The file contains embedded download links that work on mobile devices")

if __name__ == "__main__":
    create_shareable_page()