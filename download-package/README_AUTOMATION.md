# TOTO Analysis - Automated Features 🚀

This document describes the automated features that have been integrated into the TOTO analysis system.

## 🆕 New Features

### 1. **Integrated Web Scraper**
- **Automatic data download** from Lottolyzer website
- **No manual intervention** required
- **Data validation** and cleaning built-in
- **Error handling** and fallback strategies

### 2. **Automated Update System**
- **Fresh data on demand** via main menu
- **Scheduled updates** via cron jobs
- **Data freshness checking** (7-day threshold)
- **Automatic backups** before updates

### 3. **Command-Line Automation**
- **Batch processing** capabilities
- **Scheduled execution** support
- **Logging** and error reporting
- **Report generation** automation

## 📋 Quick Start

### **Option 1: Interactive Mode**
```bash
python main.py
```
Then select option **4** to download fresh TOTO data.

### **Option 2: Command Line**
```bash
# Download fresh data
python auto_update.py update

# Run analysis
python auto_update.py analyze

# Generate report
python auto_update.py report

# Full update and analysis
python auto_update.py full
```

### **Option 3: Automated Scheduling**
```bash
# Setup automated daily updates
python setup_cron.py
```

## 🔧 Setup Instructions

### **1. Install Dependencies**
```bash
pip install requests beautifulsoup4 pandas matplotlib numpy scipy seaborn
```

### **2. Test the System**
```bash
# Test scraper
python scraper_final.py

# Test auto update
python auto_update.py update

# Test main application
python main.py
```

### **3. Setup Automated Updates (Optional)**
```bash
python setup_cron.py
```
Choose your preferred schedule:
- **Daily** (recommended) - Updates every day at 9 AM
- **Weekly** - Updates every Sunday at 9 AM
- **Custom** - Define your own schedule

## 📊 Available Commands

### **Main Application (`main.py`)**
- **Option 1**: Analyze past data
- **Option 2**: Analyze simulated data
- **Option 3**: Generate new simulated data
- **Option 4**: Download fresh TOTO data ⭐ **NEW**
- **Option 0**: Exit

### **Auto Update Script (`auto_update.py`)**
- `update` - Download fresh TOTO data
- `analyze` - Run comprehensive analysis
- `report` - Generate text report
- `full` - Update + analyze + report

### **Setup Script (`setup_cron.py`)**
- **Setup cron jobs** for automated updates
- **Remove cron jobs** if needed
- **List current jobs** for verification
- **Test functionality** before scheduling

## 📁 File Structure

```
SG-TOTO-Analysis/
├── main.py                 # Main application (now with scraper integration)
├── auto_update.py          # Automated update and analysis script
├── setup_cron.py           # Cron job setup utility
├── scraper_final.py        # Web scraper for TOTO data
├── scraper_v2.py           # Enhanced scraper with debugging
├── scraper.py              # Basic scraper implementation
├── toto_results.csv        # Downloaded TOTO data
├── toto_report.txt         # Generated analysis report
├── toto_update.log         # Update log file (if using cron)
├── images/                 # Generated visualizations
└── [other original files]  # Original analysis modules
```

## 🕐 Scheduling Options

### **Daily Updates (Recommended)**
```bash
# Runs every day at 9 AM
0 9 * * * cd /path/to/SG-TOTO-Analysis && python auto_update.py update
```

### **Weekly Updates**
```bash
# Runs every Sunday at 9 AM
0 9 * * 0 cd /path/to/SG-TOTO-Analysis && python auto_update.py update
```

### **Custom Schedule**
```bash
# Example: Every 3 days at 2 PM
0 14 */3 * * cd /path/to/SG-TOTO-Analysis && python auto_update.py update
```

## 📈 Benefits of Automation

### **1. Always Fresh Data**
- **Automatic updates** ensure latest results
- **No manual downloading** required
- **Consistent data quality** through validation

### **2. Time Savings**
- **One-click updates** via main menu
- **Scheduled execution** while you sleep
- **Batch processing** for multiple operations

### **3. Reliability**
- **Error handling** and recovery
- **Automatic backups** before updates
- **Logging** for troubleshooting

### **4. Flexibility**
- **Multiple update options** (quick/extended)
- **Custom scheduling** support
- **Command-line** and **interactive** modes

## 🔍 Monitoring and Logs

### **Update Logs**
- **Location**: `toto_update.log`
- **Content**: Update timestamps, success/failure status
- **Rotation**: Manual cleanup recommended

### **Generated Reports**
- **Location**: `toto_report.txt`
- **Content**: Frequency analysis, statistical insights
- **Format**: Human-readable text report

### **Data Files**
- **Location**: `toto_results.csv`
- **Backup**: Automatic backup before updates
- **Validation**: Automatic cleaning and validation

## 🚨 Troubleshooting

### **Common Issues**

1. **Scraper not working**
   ```bash
   pip install requests beautifulsoup4
   python scraper_final.py
   ```

2. **Cron job not running**
   ```bash
   python setup_cron.py  # Check setup
   crontab -l            # Verify cron jobs
   ```

3. **Data not updating**
   ```bash
   python auto_update.py update  # Test manually
   cat toto_update.log           # Check logs
   ```

### **Error Recovery**
- **Automatic backup restoration** if update fails
- **Graceful degradation** if scraper unavailable
- **Fallback to existing data** if needed

## 🎯 Usage Examples

### **Daily Workflow**
```bash
# Morning: Check for updates
python auto_update.py update

# Analysis: Run comprehensive analysis
python auto_update.py analyze

# Report: Generate summary report
python auto_update.py report
```

### **Weekly Workflow**
```bash
# Full update and analysis
python auto_update.py full

# Review generated reports
cat toto_report.txt
ls images/
```

### **Scheduled Workflow**
```bash
# Setup once, runs automatically
python setup_cron.py

# Monitor logs
tail -f toto_update.log
```

## ✅ Success Indicators

- **✅ Data file exists**: `toto_results.csv`
- **✅ Recent updates**: File modified within 7 days
- **✅ Clean data**: No validation errors
- **✅ Generated reports**: `toto_report.txt` exists
- **✅ Visualizations**: Files in `images/` directory

---

**🎉 Congratulations!** Your TOTO analysis system is now fully automated and ready for regular use. 