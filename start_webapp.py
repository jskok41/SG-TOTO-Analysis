#!/usr/bin/env python3
"""
Startup script for TOTO Analysis Web Application
"""

import os
import sys
import subprocess
import time

def main():
    print("=" * 60)
    print("TOTO Analysis Web Application Startup".center(60))
    print("=" * 60)
    
    # Check if virtual environment exists
    if not os.path.exists('toto_venv'):
        print("❌ Virtual environment not found!")
        print("Please run the setup first:")
        print("python3 -m venv toto_venv")
        print("source toto_venv/bin/activate")
        print("pip install -r requirements.txt")
        return
    
    # Check if required files exist
    required_files = ['app.py', 'templates/index.html', 'simulated_draws.csv']
    missing_files = [f for f in required_files if not os.path.exists(f)]
    
    if missing_files:
        print(f"❌ Missing required files: {missing_files}")
        return
    
    print("✅ All required files found!")
    
    # Start the web application
    print("\n🚀 Starting TOTO Analysis Web Application...")
    print("📊 The application will be available at: http://localhost:5000")
    print("🔄 Press Ctrl+C to stop the application")
    print("-" * 60)
    
    try:
        # Activate virtual environment and run app
        if os.name == 'nt':  # Windows
            cmd = ['toto_venv\\Scripts\\python.exe', 'app.py']
        else:  # Unix/Linux/Mac
            cmd = ['toto_venv/bin/python', 'app.py']
        
        subprocess.run(cmd, check=True)
        
    except KeyboardInterrupt:
        print("\n\n🛑 Application stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error starting application: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()