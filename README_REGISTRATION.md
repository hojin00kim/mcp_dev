# 📝 등록 양식 웹 앱 (Registration Form Web App)

Google Sheets에 자동으로 데이터를 저장하는 간단한 등록 양식 웹 애플리케이션입니다.

## 🎯 기능

- 간단한 웹 인터페이스로 등록 정보 수집
- Google Sheets에 자동으로 데이터 저장
- 실시간 제출 확인 및 오류 처리
- 반응형 디자인 (모바일 친화적)

## 📋 필요한 것들

1. **Python 3.7 이상**
2. **Google 계정** (Google Sheets API 사용)
3. **인터넷 연결**

## 🚀 설치 및 설정

### 1단계: Python 패키지 설치

터미널/명령 프롬프트에서 다음 명령어를 실행하세요:

```bash
pip install flask gspread google-auth google-auth-oauthlib google-auth-httplib2
```

또는 requirements.txt를 사용:

```bash
pip install -r requirements.txt
```

### 2단계: Google Sheets API 설정

#### A. Google Cloud Console에서 프로젝트 생성

1. [Google Cloud Console](https://console.cloud.google.com/)에 접속
2. 새 프로젝트 생성 (또는 기존 프로젝트 선택)
3. 프로젝트 이름을 입력하고 생성

#### B. Google Sheets API 활성화

1. 왼쪽 메뉴에서 **"API 및 서비스"** > **"라이브러리"** 클릭
2. "Google Sheets API" 검색 후 **활성화** 클릭
3. "Google Drive API"도 검색 후 **활성화** 클릭

#### C. 서비스 계정 생성

1. **"API 및 서비스"** > **"사용자 인증 정보"** 클릭
2. 상단의 **"사용자 인증 정보 만들기"** 클릭
3. **"서비스 계정"** 선택
4. 서비스 계정 이름 입력 (예: "sheets-registration-app")
5. **"만들기"** 클릭
6. 역할은 **"편집자"** 선택 (또는 건너뛰기)
7. **"완료"** 클릭

#### D. 서비스 계정 키 다운로드

1. 생성된 서비스 계정을 클릭
2. **"키"** 탭으로 이동
3. **"키 추가"** > **"새 키 만들기"** 클릭
4. 키 유형: **JSON** 선택
5. **"만들기"** 클릭
6. JSON 파일이 자동으로 다운로드됩니다
7. 이 파일을 프로젝트 폴더에 `credentials.json`으로 저장

⚠️ **중요**: `credentials.json` 파일은 절대 공개하거나 Git에 커밋하지 마세요!

#### E. Google Sheet 준비

1. [Google Sheets](https://sheets.google.com)에서 새 스프레드시트 생성
2. 첫 번째 행에 헤더 추가 (선택사항 - 앱이 자동으로 생성합니다):
   - A1: `이름`
   - B1: `바나바`
   - C1: `배우자 이름`
   - D1: `동반가족`
3. 스프레드시트 URL에서 **스프레드시트 ID** 복사:
   - URL 예: `https://docs.google.com/spreadsheets/d/SPREADSHEET_ID_HERE/edit`
   - `SPREADSHEET_ID_HERE` 부분이 스프레드시트 ID입니다

#### F. 서비스 계정에 Sheet 공유 권한 부여

1. 다운로드한 `credentials.json` 파일을 열기
2. `client_email` 필드의 이메일 주소 복사 (예: `sheets-registration-app@project-id.iam.gserviceaccount.com`)
3. Google Sheet로 돌아가기
4. **"공유"** 버튼 클릭
5. 복사한 이메일 주소를 입력
6. 권한: **"편집자"** 선택
7. **"완료"** 클릭

### 3단계: 환경 변수 설정 (선택사항)

앱을 실행하기 전에 환경 변수를 설정할 수 있습니다:

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

또는 `app.py` 파일을 직접 수정하여 기본값을 변경할 수 있습니다.

### 4단계: 앱 실행

터미널에서 다음 명령어를 실행:

```bash
python app.py
```

또는 환경 변수와 함께:

```bash
# Windows PowerShell
$env:GOOGLE_SHEET_ID="your-id"; python app.py

# macOS/Linux
GOOGLE_SHEET_ID="your-id" python app.py
```

앱이 실행되면 다음 메시지가 표시됩니다:
```
 * Running on http://0.0.0.0:5000
```

### 5단계: 브라우저에서 접속

웹 브라우저에서 다음 주소로 접속:
```
http://localhost:5000
```

## 🌐 다른 사람들과 공유하기

### 로컬 네트워크에서 공유

같은 Wi-Fi 네트워크에 있는 사람들과 공유하려면:

1. 컴퓨터의 로컬 IP 주소 확인:
   - **Windows**: `ipconfig` (IPv4 주소 확인)
   - **macOS/Linux**: `ifconfig` 또는 `ip addr`
2. 다른 사람들에게 `http://YOUR_IP:5000` 주소 공유
3. 방화벽에서 포트 5000 허용 필요할 수 있음

### 온라인으로 배포 (영구적인 링크)

영구적인 링크를 원한다면 다음 플랫폼에 배포할 수 있습니다:

#### Heroku (무료 티어 제한 있음)
1. [Heroku](https://www.heroku.com) 계정 생성
2. Heroku CLI 설치
3. 프로젝트에 `Procfile` 생성:
   ```
   web: python app.py
   ```
4. 배포:
   ```bash
   heroku create your-app-name
   heroku config:set GOOGLE_SHEET_ID=your-id
   git push heroku main
   ```

#### PythonAnywhere (무료 티어 제공)
1. [PythonAnywhere](https://www.pythonanywhere.com) 계정 생성
2. 파일 업로드 및 설정
3. Web 앱으로 구성

#### Railway, Render, Fly.io 등
다양한 무료/유료 호스팅 서비스 사용 가능

## 📝 사용 방법

1. 웹 브라우저에서 앱 주소 열기
2. 다음 정보 입력:
   - **이름** (필수): 본인 이름
   - **바나바** (필수): 세례명
   - **배우자 이름** (선택): 배우자가 있는 경우만 입력
   - **동반가족 수** (필수): 본인과 배우자를 제외한 가족 수 (없으면 0)
3. **"제출하기"** 버튼 클릭
4. 성공 메시지 확인
5. Google Sheet에서 데이터 확인

## 🔧 문제 해결

### "credentials.json 파일을 찾을 수 없습니다"

- `credentials.json` 파일이 프로젝트 폴더에 있는지 확인
- 파일 이름이 정확히 `credentials.json`인지 확인 (대소문자 구분)

### "Google Sheets 연결 오류"

1. `credentials.json` 파일이 올바른지 확인
2. 서비스 계정 이메일이 Sheet에 공유되어 있는지 확인
3. Google Sheets API와 Drive API가 활성화되어 있는지 확인
4. 스프레드시트 ID가 올바른지 확인

### "ModuleNotFoundError: No module named 'flask'"

```bash
pip install flask gspread google-auth google-auth-oauthlib google-auth-httplib2
```

### 포트가 이미 사용 중입니다

`app.py` 파일의 마지막 줄을 수정하여 다른 포트 사용:
```python
app.run(host='0.0.0.0', port=8080, debug=True)  # 8080 포트 사용
```

## 📁 파일 구조

```
mcp-dev/
├── app.py                    # Flask 애플리케이션
├── templates/
│   └── index.html           # 웹 인터페이스
├── credentials.json         # Google API 인증 정보 (직접 생성 필요)
├── requirements.txt         # Python 패키지 목록
└── README_REGISTRATION.md   # 이 파일
```

## 🔒 보안 주의사항

- ⚠️ **`credentials.json` 파일을 절대 공개하지 마세요!**
- Git에 커밋하기 전에 `.gitignore`에 추가:
  ```
  credentials.json
  ```
- 프로덕션 환경에서는 환경 변수나 보안 키 관리 서비스 사용 권장

## 🎨 커스터마이징

### 색상 변경

`templates/index.html` 파일의 CSS 부분을 수정하여 색상 변경 가능

### 필드 추가/제거

1. `templates/index.html`에서 HTML 폼 필드 수정
2. `app.py`의 `submit()` 함수에서 데이터 처리 로직 수정
3. Google Sheet에 새 컬럼 추가

## 📞 지원

문제가 발생하면:
1. 오류 메시지를 확인하세요
2. Google Sheets API 설정을 다시 확인하세요
3. 로그 파일을 확인하세요 (터미널 출력)

## ✅ 체크리스트

설정 완료 확인:

- [ ] Python 3.7+ 설치됨
- [ ] 필요한 패키지 설치됨 (`pip install -r requirements.txt`)
- [ ] Google Cloud 프로젝트 생성됨
- [ ] Google Sheets API 활성화됨
- [ ] Google Drive API 활성화됨
- [ ] 서비스 계정 생성됨
- [ ] `credentials.json` 파일 다운로드 및 저장됨
- [ ] Google Sheet 생성됨
- [ ] 서비스 계정 이메일이 Sheet에 공유됨
- [ ] 스프레드시트 ID 확인됨
- [ ] 앱 실행 성공
- [ ] 브라우저에서 접속 가능
- [ ] 테스트 제출 성공

**완료되면 앱을 사용할 준비가 되었습니다! 🎉**

