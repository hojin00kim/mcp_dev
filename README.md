# 📝 Registration Form Web App

A simple web application that automatically saves registration data to Google Sheets.

## 🎯 Features

- Simple web interface to collect registration information
- Automatic data saving to Google Sheets
- Real-time submission confirmation and error handling
- Responsive design (mobile-friendly)

## 📋 Prerequisites

1. **Python 3.7 or higher**
2. **Google Account** (for Google Sheets API)
3. **Internet connection**

## 🚀 Installation & Setup

### Step 1: Install Python Packages

Run the following command in your terminal/command prompt:

```bash
pip install flask gspread google-auth google-auth-oauthlib google-auth-httplib2
```

Or use requirements.txt:

```bash
pip install -r requirements.txt
```

### Step 2: Google Sheets API Setup

#### A. Create a Project in Google Cloud Console

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or select an existing one)
3. Enter a project name and create it

#### B. Enable Google Sheets API

1. Click **"APIs & Services"** > **"Library"** in the left menu
2. Search for "Google Sheets API" and click **"Enable"**
3. Also search for "Google Drive API" and click **"Enable"**

#### C. Create a Service Account

1. Click **"APIs & Services"** > **"Credentials"**
2. Click **"Create Credentials"** at the top
3. Select **"Service Account"**
4. Enter a service account name (e.g., "sheets-registration-app")
5. Click **"Create"**
6. Select role as **"Editor"** (or skip)
7. Click **"Done"**

#### D. Download Service Account Key

1. Click on the created service account
2. Go to the **"Keys"** tab
3. Click **"Add Key"** > **"Create new key"**
4. Key type: Select **JSON**
5. Click **"Create"**
6. A JSON file will be automatically downloaded
7. Save this file as `credentials.json` in your project folder

⚠️ **Important**: Never share or commit the `credentials.json` file to Git!

#### E. Prepare Google Sheet

1. Create a new spreadsheet in [Google Sheets](https://sheets.google.com)
2. Add headers in the first row (optional - the app will create them automatically):
   - A1: `이름` (Name)
   - B1: `바나바` (Baptism Name)
   - C1: `배우자 이름` (Spouse Name)
   - D1: `동반가족` (Accompanying Family)
3. Copy the **Spreadsheet ID** from the URL:
   - URL example: `https://docs.google.com/spreadsheets/d/SPREADSHEET_ID_HERE/edit`
   - The `SPREADSHEET_ID_HERE` part is the spreadsheet ID

#### F. Share Sheet with Service Account

1. Open the downloaded `credentials.json` file
2. Copy the email address from the `client_email` field (e.g., `sheets-registration-app@project-id.iam.gserviceaccount.com`)
3. Go back to your Google Sheet
4. Click the **"Share"** button
5. Enter the copied email address
6. Permission: Select **"Editor"**
7. Click **"Done"**

### Step 3: Environment Variables (Optional)

You can set environment variables before running the app:

**Windows (PowerShell):**
```powershell
$env:GOOGLE_SHEET_ID="your-spreadsheet-id-here"
$env:GOOGLE_CREDENTIALS_FILE="credentials.json"
$env:WORKSHEET_NAME="Sheet1"
```

**Windows (CMD):**
```cmd
set GOOGLE_SHEET_ID=your-spreadsheet-id-here
set GOOGLE_CREDENTIALS_FILE=credentials.json
set WORKSHEET_NAME=Sheet1
```

**macOS/Linux:**
```bash
export GOOGLE_SHEET_ID="your-spreadsheet-id-here"
export GOOGLE_CREDENTIALS_FILE="credentials.json"
export WORKSHEET_NAME="Sheet1"
```

Alternatively, you can directly modify the `app.py` file to change the default values.

### Step 4: Run the App

Run the following command in your terminal:

```bash
python app.py
```

Or with environment variables:

```bash
# Windows PowerShell
$env:GOOGLE_SHEET_ID="your-id"; python app.py

# macOS/Linux
GOOGLE_SHEET_ID="your-id" python app.py
```

When the app runs, you'll see:
```
 * Running on http://0.0.0.0:5000
```

### Step 5: Access in Browser

Open the following address in your web browser:
```
http://localhost:5000
```

## 🌐 Sharing with Others

### Share on Local Network

To share with people on the same Wi-Fi network:

1. Find your computer's local IP address:
   - **Windows**: `ipconfig` (check IPv4 address)
   - **macOS/Linux**: `ifconfig` or `ip addr`
2. Share the address `http://YOUR_IP:5000` with others
3. You may need to allow port 5000 in your firewall

### Deploy Online (Permanent Link)

For a permanent link, you can deploy to the following platforms:

#### Heroku (Free tier limitations)
1. Create an account on [Heroku](https://www.heroku.com)
2. Install Heroku CLI
3. Create a `Procfile` in your project:
   ```
   web: python app.py
   ```
4. Deploy:
   ```bash
   heroku create your-app-name
   heroku config:set GOOGLE_SHEET_ID=your-id
   git push heroku main
   ```

#### PythonAnywhere (Free tier available)
1. Create an account on [PythonAnywhere](https://www.pythonanywhere.com)
2. Upload files and configure
3. Set up as a Web app

#### Railway, Render, Fly.io, etc.
Various free/paid hosting services are available

## 📝 How to Use

1. Open the app address in a web browser
2. Enter the following information:
   - **Name** (Required): Your name
   - **Baptism Name** (Required): Your baptism name
   - **Spouse Name** (Optional): Enter only if you have a spouse
   - **Accompanying Family Count** (Required): Number of family members excluding yourself and spouse (0 if none)
3. Click the **"Submit"** button
4. Confirm the success message
5. Check the data in Google Sheet

## 🔧 Troubleshooting

### "credentials.json file not found"

- Check if `credentials.json` file is in the project folder
- Verify the file name is exactly `credentials.json` (case-sensitive)

### "Google Sheets connection error"

1. Verify the `credentials.json` file is correct
2. Check if the service account email is shared with the Sheet
3. Verify Google Sheets API and Drive API are enabled
4. Check if the spreadsheet ID is correct

### "ModuleNotFoundError: No module named 'flask'"

```bash
pip install flask gspread google-auth google-auth-oauthlib google-auth-httplib2
```

### Port already in use

Modify the last line in `app.py` to use a different port:
```python
app.run(host='0.0.0.0', port=8080, debug=True)  # Use port 8080
```

## 📁 File Structure

```
mcp-dev/
├── app.py                    # Flask application
├── templates/
│   └── index.html           # Web interface
├── credentials.json         # Google API credentials (create manually)
├── requirements.txt         # Python package list
└── README.md                # This file
```

## 🔒 Security Notes

- ⚠️ **Never share the `credentials.json` file publicly!**
- Add to `.gitignore` before committing to Git:
  ```
  credentials.json
  ```
- For production environments, use environment variables or secure key management services

## 🎨 Customization

### Change Colors

Modify the CSS section in `templates/index.html` to change colors

### Add/Remove Fields

1. Modify HTML form fields in `templates/index.html`
2. Update data processing logic in the `submit()` function in `app.py`
3. Add new columns to Google Sheet

## 📞 Support

If you encounter issues:
1. Check the error messages
2. Verify Google Sheets API setup again
3. Check log files (terminal output)

## ✅ Checklist

Setup completion check:

- [ ] Python 3.7+ installed
- [ ] Required packages installed (`pip install -r requirements.txt`)
- [ ] Google Cloud project created
- [ ] Google Sheets API enabled
- [ ] Google Drive API enabled
- [ ] Service account created
- [ ] `credentials.json` file downloaded and saved
- [ ] Google Sheet created
- [ ] Service account email shared with Sheet
- [ ] Spreadsheet ID confirmed
- [ ] App runs successfully
- [ ] Accessible in browser
- [ ] Test submission successful

**Once complete, your app is ready to use! 🎉**

