"""
Google Sheets Registration App
A simple web app to collect registration information and save to Google Sheets
"""

from flask import Flask, render_template, request, jsonify
import gspread
from google.oauth2.service_account import Credentials
import os
import json
from datetime import datetime

app = Flask(__name__)

# Google Sheets configuration
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# These will be set via environment variables or config
SPREADSHEET_ID = os.environ.get('GOOGLE_SHEET_ID', '1SidRqMLyUsk2lXYFo-ugR8c9jqYO70QgizWt4GlyFQo')
CREDENTIALS_FILE = os.environ.get('GOOGLE_CREDENTIALS_FILE', 'credentials.json')
WORKSHEET_NAME = os.environ.get('WORKSHEET_NAME', 'Sheet1')


def get_google_sheet():
    """Initialize and return Google Sheet client"""
    try:
        # Try to get credentials from environment variable first (for Render/deployment)
        creds_json = os.environ.get('GOOGLE_CREDENTIALS_JSON')
        if creds_json:
            # Parse JSON from environment variable
            try:
                creds_info = json.loads(creds_json)
                creds = Credentials.from_service_account_info(creds_info, scopes=SCOPE)
            except json.JSONDecodeError as e:
                print(f"Error: Invalid JSON in GOOGLE_CREDENTIALS_JSON: {e}")
                # Fall back to file
                creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPE)
        else:
            # Fall back to file (for local development)
            creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPE)
        
        client = gspread.authorize(creds)
        spreadsheet = client.open_by_key(SPREADSHEET_ID)
        worksheet = spreadsheet.worksheet(WORKSHEET_NAME)
        return worksheet
    except FileNotFoundError:
        print(f"Error: Credentials file '{CREDENTIALS_FILE}' not found!")
        print("Note: For deployment, use GOOGLE_CREDENTIALS_JSON environment variable")
        return None
    except Exception as e:
        print(f"Error connecting to Google Sheets: {e}")
        return None


@app.route('/')
def index():
    """Render the main form page"""
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    """Handle form submission and write to Google Sheets"""
    try:
        # Get form data
        name = request.form.get('name', '').strip()
        baptism_name = request.form.get('baptism_name', '').strip()
        spouse_name = request.form.get('spouse_name', '').strip()
        family_count = request.form.get('family_count', '').strip()
        
        # Validation
        if not name:
            return jsonify({'success': False, 'message': '이름을 입력해주세요.'}), 400
        
        if not baptism_name:
            return jsonify({'success': False, 'message': '바나바를 입력해주세요.'}), 400
        
        # Family count should be a number (can be 0)
        try:
            family_count_int = int(family_count) if family_count else 0
            if family_count_int < 0:
                return jsonify({'success': False, 'message': '동반가족 수는 0 이상이어야 합니다.'}), 400
        except ValueError:
            return jsonify({'success': False, 'message': '동반가족 수는 숫자로 입력해주세요.'}), 400
        
        # Get Google Sheet
        worksheet = get_google_sheet()
        if worksheet is None:
            return jsonify({
                'success': False, 
                'message': 'Google Sheets 연결 오류가 발생했습니다. 관리자에게 문의하세요.'
            }), 500
        
        # Check if headers exist, if not create them
        try:
            headers = worksheet.row_values(1)
            if not headers or len(headers) < 4:
                worksheet.update('A1:D1', [['이름', '바나바', '배우자 이름', '동반가족']])
        except:
            # If first row is empty, add headers
            worksheet.update('A1:D1', [['이름', '바나바', '배우자 이름', '동반가족']])
        
        # Append new row
        new_row = [name, baptism_name, spouse_name, family_count_int]
        worksheet.append_row(new_row)
        
        return jsonify({
            'success': True, 
            'message': '등록이 완료되었습니다! 감사합니다.'
        })
        
    except Exception as e:
        print(f"Error submitting form: {e}")
        return jsonify({
            'success': False, 
            'message': f'오류가 발생했습니다: {str(e)}'
        }), 500


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok'})


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
    # Use debug=False for production (Render will set this automatically)
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug_mode)

