# ⚡ 빠른 시작 가이드

## 5분 안에 시작하기

### 1. 패키지 설치 (1분)
```bash
pip install flask gspread google-auth google-auth-oauthlib google-auth-httplib2
```

### 2. Google Sheets API 설정 (3분)

#### 간단 버전:
1. [Google Cloud Console](https://console.cloud.google.com/) 접속
2. 프로젝트 생성 → "API 및 서비스" → "라이브러리"
3. "Google Sheets API" 검색 → 활성화
4. "Google Drive API" 검색 → 활성화
5. "사용자 인증 정보" → "사용자 인증 정보 만들기" → "서비스 계정"
6. 서비스 계정 생성 후 "키" 탭 → "키 추가" → JSON 다운로드
7. 다운로드한 파일을 `credentials.json`으로 이름 변경하고 프로젝트 폴더에 저장

### 3. Google Sheet 준비 (1분)
1. [Google Sheets](https://sheets.google.com)에서 새 시트 생성
2. URL에서 스프레드시트 ID 복사 (예: `https://docs.google.com/spreadsheets/d/ABC123XYZ/edit` → `ABC123XYZ`)
3. `credentials.json` 파일을 열어서 `client_email` 값 복사
4. Google Sheet에서 "공유" 버튼 클릭 → 복사한 이메일 주소 입력 → "편집자" 권한 부여

### 4. 실행 (30초)

**방법 1: 환경 변수 사용**
```bash
# Windows PowerShell
$env:GOOGLE_SHEET_ID="여기에-스프레드시트-ID-입력"; python app.py

# macOS/Linux
GOOGLE_SHEET_ID="여기에-스프레드시트-ID-입력" python app.py
```

**방법 2: app.py 파일 수정**
`app.py` 파일을 열어서 다음 줄을 찾아 수정:
```python
SPREADSHEET_ID = os.environ.get('GOOGLE_SHEET_ID', '여기에-스프레드시트-ID-입력')
```

### 5. 브라우저에서 열기
```
http://localhost:5000
```

## ✅ 완료!

이제 양식을 작성하고 제출하면 Google Sheet에 자동으로 저장됩니다!

## 🔗 다른 사람과 공유하기

같은 Wi-Fi에 있는 사람들과 공유:
1. 컴퓨터 IP 주소 확인: `ipconfig` (Windows) 또는 `ifconfig` (Mac/Linux)
2. `http://YOUR_IP:5000` 주소 공유

더 자세한 내용은 `README_REGISTRATION.md`를 참고하세요!

