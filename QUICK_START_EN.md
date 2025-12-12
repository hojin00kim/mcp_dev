# ⚡ Quick Start Guide

## Get Started in 5 Minutes

### 1. Install Packages (1 minute)
```bash
pip install flask gspread google-auth google-auth-oauthlib google-auth-httplib2
```

### 2. Google Sheets API Setup (3 minutes)

#### Simple Version:
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create project → "APIs & Services" → "Library"
3. Search "Google Sheets API" → Enable
4. Search "Google Drive API" → Enable
5. "Credentials" → "Create Credentials" → "Service Account"
6. After creating service account, go to "Keys" tab → "Add Key" → Download JSON
7. Rename downloaded file to `credentials.json` and save in project folder

### 3. Prepare Google Sheet (1 minute)
1. Create a new sheet in [Google Sheets](https://sheets.google.com)
2. Copy spreadsheet ID from URL (e.g., `https://docs.google.com/spreadsheets/d/ABC123XYZ/edit` → `ABC123XYZ`)
3. Open `credentials.json` file and copy the `client_email` value
4. In Google Sheet, click "Share" → Enter copied email address → Grant "Editor" permission

### 4. Run (30 seconds)

**Method 1: Using Environment Variables**
```bash
# Windows PowerShell
$env:GOOGLE_SHEET_ID="enter-your-spreadsheet-id-here"; python app.py

# macOS/Linux
GOOGLE_SHEET_ID="enter-your-spreadsheet-id-here" python app.py
```

**Method 2: Edit app.py**
Open `app.py` and find this line to modify:
```python
SPREADSHEET_ID = os.environ.get('GOOGLE_SHEET_ID', 'enter-your-spreadsheet-id-here')
```

### 5. Open in Browser
```
http://localhost:5000
```

## ✅ Done!

Now when you fill out and submit the form, it will automatically save to your Google Sheet!

## 🔗 Sharing with Others

To share with people on the same Wi-Fi:
1. Find your computer's IP address: `ipconfig` (Windows) or `ifconfig` (Mac/Linux)
2. Share the address `http://YOUR_IP:5000`

For more details, see `README.md`!

