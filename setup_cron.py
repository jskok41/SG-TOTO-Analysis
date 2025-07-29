#!/usr/bin/env python3
"""
Setup script for automated TOTO data updates
This script helps configure cron jobs for regular data updates
"""

import os
import sys
import subprocess
from datetime import datetime

def get_project_path():
    """
    Get the absolute path to the project directory
    """
    return os.path.abspath(os.path.dirname(__file__))

def setup_cron_job():
    """
    Set up a cron job for automated TOTO updates
    """
    print("=" * 60)
    print("TOTO Automated Update Setup".center(60))
    print("=" * 60)
    
    project_path = get_project_path()
    python_path = sys.executable
    auto_update_script = os.path.join(project_path, "auto_update.py")
    
    print(f"📁 Project path: {project_path}")
    print(f"🐍 Python path: {python_path}")
    print(f"📜 Script path: {auto_update_script}")
    
    # Check if script exists
    if not os.path.exists(auto_update_script):
        print("❌ auto_update.py not found!")
        return False
    
    print("\n🕐 Choose update frequency:")
    print("1. Daily (recommended)")
    print("2. Weekly")
    print("3. Custom schedule")
    print("0. Cancel")
    
    choice = input("Choice: ")
    
    if choice == "0":
        print("Setup cancelled.")
        return False
    
    # Define cron schedules
    schedules = {
        "1": "0 9 * * *",  # Daily at 9 AM
        "2": "0 9 * * 0",  # Weekly on Sunday at 9 AM
        "3": None  # Custom
    }
    
    if choice == "3":
        print("\n📅 Enter custom cron schedule (e.g., '0 9 * * *' for daily at 9 AM):")
        custom_schedule = input("Schedule: ").strip()
        if not custom_schedule:
            print("❌ Invalid schedule")
            return False
        cron_schedule = custom_schedule
    else:
        cron_schedule = schedules.get(choice)
        if not cron_schedule:
            print("❌ Invalid choice")
            return False
    
    # Create cron command
    cron_command = f"{cron_schedule} cd {project_path} && {python_path} {auto_update_script} update >> {project_path}/toto_update.log 2>&1"
    
    print(f"\n📋 Cron command to be added:")
    print(cron_command)
    
    # Ask for confirmation
    confirm = input("\n❓ Add this cron job? (y/n): ").lower().strip()
    
    if confirm != 'y':
        print("Setup cancelled.")
        return False
    
    try:
        # Add cron job
        result = subprocess.run(['crontab', '-l'], capture_output=True, text=True)
        current_crontab = result.stdout
        
        # Check if job already exists
        if cron_command in current_crontab:
            print("⚠️  Cron job already exists!")
            return True
        
        # Add new job
        new_crontab = current_crontab + "\n" + cron_command + "\n"
        
        # Write new crontab
        result = subprocess.run(['crontab', '-'], input=new_crontab, text=True, capture_output=True)
        
        if result.returncode == 0:
            print("✅ Cron job added successfully!")
            print(f"📅 Schedule: {cron_schedule}")
            print(f"📝 Log file: {project_path}/toto_update.log")
            return True
        else:
            print(f"❌ Failed to add cron job: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error setting up cron job: {e}")
        return False

def remove_cron_job():
    """
    Remove existing TOTO cron jobs
    """
    print("🗑️  Removing TOTO cron jobs...")
    
    try:
        result = subprocess.run(['crontab', '-l'], capture_output=True, text=True)
        current_crontab = result.stdout
        
        # Remove lines containing auto_update.py
        lines = current_crontab.split('\n')
        filtered_lines = [line for line in lines if 'auto_update.py' not in line]
        
        new_crontab = '\n'.join(filtered_lines)
        
        result = subprocess.run(['crontab', '-'], input=new_crontab, text=True, capture_output=True)
        
        if result.returncode == 0:
            print("✅ Cron jobs removed successfully!")
            return True
        else:
            print(f"❌ Failed to remove cron jobs: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error removing cron jobs: {e}")
        return False

def list_cron_jobs():
    """
    List current cron jobs
    """
    print("📋 Current cron jobs:")
    
    try:
        result = subprocess.run(['crontab', '-l'], capture_output=True, text=True)
        
        if result.returncode == 0:
            jobs = result.stdout.strip()
            if jobs:
                print(jobs)
            else:
                print("No cron jobs found.")
        else:
            print("No cron jobs found.")
            
    except Exception as e:
        print(f"❌ Error listing cron jobs: {e}")

def test_auto_update():
    """
    Test the auto update functionality
    """
    print("🧪 Testing auto update functionality...")
    
    auto_update_script = os.path.join(get_project_path(), "auto_update.py")
    
    if not os.path.exists(auto_update_script):
        print("❌ auto_update.py not found!")
        return False
    
    try:
        result = subprocess.run([sys.executable, auto_update_script, "update"], 
                              capture_output=True, text=True)
        
        print("Output:")
        print(result.stdout)
        
        if result.stderr:
            print("Errors:")
            print(result.stderr)
        
        if result.returncode == 0:
            print("✅ Auto update test successful!")
            return True
        else:
            print("❌ Auto update test failed!")
            return False
            
    except Exception as e:
        print(f"❌ Error testing auto update: {e}")
        return False

def main():
    """
    Main setup function
    """
    print("🤖 TOTO Automated Update Setup")
    print("=" * 40)
    
    print("Choose option:")
    print("1. Setup automated updates (cron job)")
    print("2. Remove automated updates")
    print("3. List current cron jobs")
    print("4. Test auto update functionality")
    print("0. Exit")
    
    choice = input("Choice: ")
    
    if choice == "1":
        setup_cron_job()
    elif choice == "2":
        remove_cron_job()
    elif choice == "3":
        list_cron_jobs()
    elif choice == "4":
        test_auto_update()
    elif choice == "0":
        print("Goodbye!")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main() 