# 🚀 Deploy to Render.com - Step by Step Guide

Complete guide to deploy your Registration Form Web App to Render.com for free.

## 📋 Prerequisites

Before deploying, make sure you have:
- ✅ Google Sheets API credentials set up (`credentials.json`)
- ✅ Google Sheet created and shared with service account
- ✅ All code files ready

## 🎯 Step-by-Step Deployment

### Step 1: Prepare Your Code

#### 1.1 Create a Procfile

Create a file named `Procfile` (no extension) in your project root with this content:

```
web: gunicorn app:app
```

**Note**: We'll use `gunicorn` instead of Flask's built-in server for production.

#### 1.2 Update requirements.txt

Make sure your `requirements.txt` includes `gunicorn`:

```
flask>=3.0.0
gspread>=5.12.0
google-auth>=2.23.0
google-auth-oauthlib>=1.1.0
google-auth-httplib2>=0.1.1
gunicorn>=21.2.0
```

#### 1.3 Update app.py for Production

We need to modify `app.py` to work better with Render. Update the last section:

```python
if __name__ == '__main__':
    # Check if credentials file exists
    if not os.path.exists(CREDENTIALS_FILE):
        print(f"\n⚠️  Warning: Credentials file '{CREDENTIALS_FILE}' not found!")
        print("Please set up Google Sheets API credentials (see README_REGISTRATION.md)\n")
    
    # Check if spreadsheet ID is set
    if not SPREADSHEET_ID:
        print("\n⚠️  Warning: Google Sheet ID is not set!")
        print("Please set GOOGLE_SHEET_ID environment variable or update app.py\n")
    else:
        print(f"\n✅ Using Google Sheet ID: {SPREADSHEET_ID}")
        print("Make sure the service account email has access to this sheet!\n")
    
    # Run the app
    port = int(os.environ.get('PORT', 5000))
    print(f"🚀 Starting server on http://0.0.0.0:{port}")
    print(f"📱 Access the app at: http://localhost:{port}\n")
    app.run(host='0.0.0.0', port=port, debug=False)  # debug=False for production
```

### Step 2: Convert credentials.json to Environment Variable

Since we can't upload files directly to Render, we need to convert the credentials to an environment variable.

#### 2.1 Get Your credentials.json Content

1. Open your `credentials.json` file
2. Copy the entire JSON content
3. You'll need to paste this as an environment variable on Render

**Important**: The JSON needs to be on a single line or properly escaped.

### Step 3: Create Render Account

1. Go to [Render.com](https://render.com)
2. Click **"Get Started for Free"** or **"Sign Up"**
3. Sign up with:
   - GitHub account (recommended - easiest)
   - Email address
   - Google account

### Step 4: Connect Your Repository

#### Option A: Deploy from GitHub (Recommended)

1. **Push your code to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

2. **In Render Dashboard**:
   - Click **"New +"** button
   - Select **"Web Service"**
   - Connect your GitHub account if not already connected
   - Select your repository
   - Click **"Connect"**

#### Option B: Deploy from Public Git Repository

If your repo is already on GitHub/GitLab/Bitbucket:
1. Click **"New +"** > **"Web Service"**
2. Select **"Public Git repository"**
3. Enter your repository URL
4. Click **"Connect"**

### Step 5: Configure Your Web Service

Fill in the configuration:

1. **Name**: Choose a name (e.g., `registration-form-app`)
   - This will be your app URL: `your-app-name.onrender.com`

2. **Region**: Select closest to your users (e.g., `Oregon (US West)`)

3. **Branch**: `main` (or `master`)

4. **Root Directory**: Leave empty (if code is in root) or specify folder

5. **Environment**: Select `Python 3`

6. **Build Command**: 
   ```
   pip install -r requirements.txt
   ```

7. **Start Command**: 
   ```
   gunicorn app:app
   ```

8. **Plan**: Select **"Free"** (or paid if you need more resources)

### Step 6: Set Environment Variables

This is crucial! Click **"Advanced"** and add these environment variables:

#### Required Environment Variables:

1. **GOOGLE_SHEET_ID**
   - Key: `GOOGLE_SHEET_ID`
   - Value: `1SidRqMLyUsk2lXYFo-ugR8c9jqYO70QgizWt4GlyFQo`
   - (Your spreadsheet ID)

2. **GOOGLE_CREDENTIALS_JSON**
   - Key: `GOOGLE_CREDENTIALS_JSON`
   - Value: Paste your entire `credentials.json` content here
   - **Important**: Make sure it's valid JSON on one line or properly formatted

3. **WORKSHEET_NAME** (Optional)
   - Key: `WORKSHEET_NAME`
   - Value: `Sheet1`

4. **GOOGLE_CREDENTIALS_FILE** (Optional, we'll handle this differently)
   - Key: `GOOGLE_CREDENTIALS_FILE`
   - Value: Leave empty or remove (we'll use JSON directly)

#### How to Add credentials.json as Environment Variable:

**Method 1: Single Line JSON**
1. Open `credentials.json`
2. Copy all content
3. Remove all line breaks (make it one line)
4. Paste in the `GOOGLE_CREDENTIALS_JSON` value field

**Method 2: Use Online Tool**
1. Go to https://www.freeformatter.com/json-escape.html
2. Paste your JSON
3. Click "Escape JSON"
4. Copy the escaped version
5. Paste in Render environment variable

### Step 7: Update app.py to Use Environment Variable

We need to modify `app.py` to read credentials from environment variable instead of file:

```python
import json
import os

# ... existing code ...

def get_google_sheet():
    """Initialize and return Google Sheet client"""
    try:
        # Try to get credentials from environment variable first
        creds_json = os.environ.get('GOOGLE_CREDENTIALS_JSON')
        if creds_json:
            # Parse JSON from environment variable
            creds_info = json.loads(creds_json)
            creds = Credentials.from_service_account_info(creds_info, scopes=SCOPE)
        else:
            # Fall back to file
            creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPE)
        
        client = gspread.authorize(creds)
        spreadsheet = client.open_by_key(SPREADSHEET_ID)
        worksheet = spreadsheet.worksheet(WORKSHEET_NAME)
        return worksheet
    except FileNotFoundError:
        print(f"Error: Credentials file '{CREDENTIALS_FILE}' not found!")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in GOOGLE_CREDENTIALS_JSON: {e}")
        return None
    except Exception as e:
        print(f"Error connecting to Google Sheets: {e}")
        return None
```

### Step 8: Deploy

1. Scroll down and click **"Create Web Service"**
2. Render will start building and deploying your app
3. This process takes 2-5 minutes
4. You'll see build logs in real-time

### Step 9: Verify Deployment

1. Wait for deployment to complete (green "Live" status)
2. Click on your service name to see details
3. Your app URL will be: `https://your-app-name.onrender.com`
4. Click the URL to test your app

### Step 10: Test Your App

1. Open your Render app URL
2. Fill out the registration form
3. Submit and verify data appears in Google Sheet

## 🔧 Troubleshooting

### Build Fails

**Error: "Module not found"**
- Check `requirements.txt` includes all packages
- Verify package names are correct

**Error: "Command not found: gunicorn"**
- Make sure `gunicorn` is in `requirements.txt`
- Check build logs for installation errors

### App Crashes After Deployment

**Error: "Google Sheets connection error"**
1. Check `GOOGLE_CREDENTIALS_JSON` environment variable:
   - Is it valid JSON?
   - Is it properly escaped?
   - Try copying from `credentials.json` again
2. Verify `GOOGLE_SHEET_ID` is correct
3. Check service account email is shared with Sheet

**Error: "Invalid credentials"**
- Re-download `credentials.json` from Google Cloud Console
- Make sure you copied the entire JSON content
- Check for any missing quotes or brackets

### App Shows "Application Error"

1. Check **"Logs"** tab in Render dashboard
2. Look for error messages
3. Common issues:
   - Missing environment variables
   - Invalid JSON in credentials
   - Port configuration issues

### How to View Logs

1. Go to your service in Render dashboard
2. Click **"Logs"** tab
3. Check both **"Build Logs"** and **"Runtime Logs"**

## 🔄 Updating Your App

### Method 1: Auto-Deploy from Git (Recommended)

1. Make changes to your code
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update description"
   git push
   ```
3. Render will automatically detect changes and redeploy

### Method 2: Manual Deploy

1. Go to Render dashboard
2. Click **"Manual Deploy"**
3. Select branch and click **"Deploy latest commit"**

## 💰 Free Tier Limitations

Render's free tier includes:
- ✅ 750 hours/month (enough for 24/7 operation)
- ✅ Automatic SSL certificate
- ✅ Custom domain support
- ⚠️ Apps spin down after 15 minutes of inactivity
- ⚠️ First request after spin-down takes ~30 seconds (cold start)

**Note**: If your app spins down, the first user to visit will experience a delay. Consider upgrading to paid plan for always-on service.

## 🔒 Security Best Practices

1. **Never commit `credentials.json` to Git**
   - It's already in `.gitignore`
   - Always use environment variables in production

2. **Use Environment Variables**
   - All sensitive data should be in Render environment variables
   - Never hardcode credentials in code

3. **Regular Updates**
   - Keep dependencies updated
   - Monitor Render dashboard for security alerts

## 📝 Checklist

Before deploying:
- [ ] `Procfile` created with `web: gunicorn app:app`
- [ ] `gunicorn` added to `requirements.txt`
- [ ] `app.py` updated to use `GOOGLE_CREDENTIALS_JSON` environment variable
- [ ] Code pushed to GitHub (if using Git deployment)
- [ ] `credentials.json` content ready to paste as environment variable

After deploying:
- [ ] All environment variables set in Render
- [ ] Build completed successfully
- [ ] App shows "Live" status
- [ ] Test form submission works
- [ ] Data appears in Google Sheet
- [ ] App URL is accessible

## 🎉 Success!

Once deployed, you'll have:
- ✅ A permanent URL: `https://your-app-name.onrender.com`
- ✅ Automatic HTTPS (SSL certificate)
- ✅ Auto-deploy on Git push
- ✅ Free hosting (with limitations)

Share your app URL with users and they can access it from anywhere!

## 📞 Need Help?

- Render Documentation: https://render.com/docs
- Render Community: https://community.render.com
- Check Render dashboard logs for specific errors

