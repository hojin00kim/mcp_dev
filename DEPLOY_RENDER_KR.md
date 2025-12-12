# 🚀 Render.com 배포 가이드 - 단계별 설명

Registration Form Web App을 Render.com에 무료로 배포하는 완전한 가이드입니다.

## 📋 사전 준비

배포하기 전에 확인사항:
- ✅ Google Sheets API 인증 정보 설정 완료 (`credentials.json`)
- ✅ Google Sheet 생성 및 서비스 계정과 공유 완료
- ✅ 모든 코드 파일 준비 완료

## 🎯 단계별 배포 방법

### 1단계: 코드 준비

#### 1.1 Procfile 생성

프로젝트 루트에 `Procfile` 파일을 생성하세요 (확장자 없음):

```
web: gunicorn app:app
```

**참고**: 프로덕션 환경에서는 Flask 내장 서버 대신 `gunicorn`을 사용합니다.

#### 1.2 requirements.txt 확인

`requirements.txt`에 `gunicorn`이 포함되어 있는지 확인하세요:

```
flask>=3.0.0
gspread>=5.12.0
google-auth>=2.23.0
google-auth-oauthlib>=1.1.0
google-auth-httplib2>=0.1.1
gunicorn>=21.2.0
```

### 2단계: credentials.json을 환경 변수로 변환

Render에서는 파일을 직접 업로드할 수 없으므로, 인증 정보를 환경 변수로 변환해야 합니다.

#### 2.1 credentials.json 내용 가져오기

1. `credentials.json` 파일 열기
2. 전체 JSON 내용 복사
3. Render의 환경 변수로 붙여넣을 준비

**중요**: JSON은 한 줄로 되어 있거나 올바르게 이스케이프되어 있어야 합니다.

### 3단계: Render 계정 생성

1. [Render.com](https://render.com) 접속
2. **"Get Started for Free"** 또는 **"Sign Up"** 클릭
3. 다음 중 하나로 가입:
   - GitHub 계정 (권장 - 가장 쉬움)
   - 이메일 주소
   - Google 계정

### 4단계: 저장소 연결

#### 방법 A: GitHub에서 배포 (권장)

1. **코드를 GitHub에 푸시**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

2. **Render 대시보드에서**:
   - **"New +"** 버튼 클릭
   - **"Web Service"** 선택
   - 아직 연결되지 않았다면 GitHub 계정 연결
   - 저장소 선택
   - **"Connect"** 클릭

#### 방법 B: 공개 Git 저장소에서 배포

이미 GitHub/GitLab/Bitbucket에 저장소가 있다면:
1. **"New +"** > **"Web Service"** 클릭
2. **"Public Git repository"** 선택
3. 저장소 URL 입력
4. **"Connect"** 클릭

### 5단계: Web Service 설정

설정 항목을 입력하세요:

1. **Name**: 앱 이름 선택 (예: `registration-form-app`)
   - 이것이 앱 URL이 됩니다: `your-app-name.onrender.com`

2. **Region**: 사용자와 가장 가까운 지역 선택 (예: `Oregon (US West)`)

3. **Branch**: `main` (또는 `master`)

4. **Root Directory**: 비워두기 (코드가 루트에 있는 경우) 또는 폴더 지정

5. **Environment**: `Python 3` 선택

6. **Build Command**: 
   ```
   pip install -r requirements.txt
   ```

7. **Start Command**: 
   ```
   gunicorn app:app
   ```

8. **Plan**: **"Free"** 선택 (또는 더 많은 리소스가 필요하면 유료 플랜)

### 6단계: 환경 변수 설정

중요합니다! **"Advanced"**를 클릭하고 다음 환경 변수를 추가하세요:

#### 필수 환경 변수:

1. **GOOGLE_SHEET_ID**
   - Key: `GOOGLE_SHEET_ID`
   - Value: `1SidRqMLyUsk2lXYFo-ugR8c9jqYO70QgizWt4GlyFQo`
   - (스프레드시트 ID)

2. **GOOGLE_CREDENTIALS_JSON**
   - Key: `GOOGLE_CREDENTIALS_JSON`
   - Value: `credentials.json`의 전체 내용을 여기에 붙여넣기
   - **중요**: 유효한 JSON이어야 하며 한 줄이거나 올바르게 포맷되어 있어야 합니다

3. **WORKSHEET_NAME** (선택사항)
   - Key: `WORKSHEET_NAME`
   - Value: `Sheet1`

#### credentials.json을 환경 변수로 추가하는 방법:

**방법 1: 한 줄 JSON**
1. `credentials.json` 열기
2. 모든 내용 복사
3. 모든 줄바꿈 제거 (한 줄로 만들기)
4. `GOOGLE_CREDENTIALS_JSON` 값 필드에 붙여넣기

**방법 2: 온라인 도구 사용**
1. https://www.freeformatter.com/json-escape.html 접속
2. JSON 붙여넣기
3. "Escape JSON" 클릭
4. 이스케이프된 버전 복사
5. Render 환경 변수에 붙여넣기

### 7단계: 배포

1. 아래로 스크롤하여 **"Create Web Service"** 클릭
2. Render가 앱 빌드 및 배포를 시작합니다
3. 이 과정은 2-5분이 소요됩니다
4. 실시간으로 빌드 로그를 볼 수 있습니다

### 8단계: 배포 확인

1. 배포가 완료될 때까지 대기 (녹색 "Live" 상태)
2. 서비스 이름을 클릭하여 세부 정보 확인
3. 앱 URL: `https://your-app-name.onrender.com`
4. URL을 클릭하여 앱 테스트

### 9단계: 앱 테스트

1. Render 앱 URL 열기
2. 등록 양식 작성
3. 제출하고 Google Sheet에 데이터가 나타나는지 확인

## 🔧 문제 해결

### 빌드 실패

**오류: "Module not found"**
- `requirements.txt`에 모든 패키지가 포함되어 있는지 확인
- 패키지 이름이 올바른지 확인

**오류: "Command not found: gunicorn"**
- `requirements.txt`에 `gunicorn`이 있는지 확인
- 빌드 로그에서 설치 오류 확인

### 배포 후 앱 크래시

**오류: "Google Sheets 연결 오류"**
1. `GOOGLE_CREDENTIALS_JSON` 환경 변수 확인:
   - 유효한 JSON인가요?
   - 올바르게 이스케이프되어 있나요?
   - `credentials.json`에서 다시 복사해보세요
2. `GOOGLE_SHEET_ID`가 올바른지 확인
3. 서비스 계정 이메일이 Sheet와 공유되어 있는지 확인

**오류: "Invalid credentials"**
- Google Cloud Console에서 `credentials.json` 다시 다운로드
- 전체 JSON 내용을 복사했는지 확인
- 따옴표나 대괄호가 누락되지 않았는지 확인

### 앱이 "Application Error" 표시

1. Render 대시보드에서 **"Logs"** 탭 확인
2. 오류 메시지 확인
3. 일반적인 문제:
   - 환경 변수 누락
   - 인증 정보의 잘못된 JSON
   - 포트 구성 문제

### 로그 보는 방법

1. Render 대시보드에서 서비스로 이동
2. **"Logs"** 탭 클릭
3. **"Build Logs"**와 **"Runtime Logs"** 모두 확인

## 🔄 앱 업데이트

### 방법 1: Git에서 자동 배포 (권장)

1. 코드 변경
2. GitHub에 커밋 및 푸시:
   ```bash
   git add .
   git commit -m "Update description"
   git push
   ```
3. Render가 자동으로 변경사항을 감지하고 재배포합니다

### 방법 2: 수동 배포

1. Render 대시보드로 이동
2. **"Manual Deploy"** 클릭
3. 브랜치 선택 후 **"Deploy latest commit"** 클릭

## 💰 무료 플랜 제한사항

Render 무료 플랜 포함 사항:
- ✅ 월 750시간 (24/7 운영 가능)
- ✅ 자동 SSL 인증서
- ✅ 커스텀 도메인 지원
- ⚠️ 15분 비활성 후 앱이 중지됨
- ⚠️ 중지 후 첫 요청은 ~30초 소요 (콜드 스타트)

**참고**: 앱이 중지되면 첫 방문자가 지연을 경험합니다. 항상 켜져 있는 서비스를 원하면 유료 플랜으로 업그레이드하세요.

## 🔒 보안 모범 사례

1. **절대 `credentials.json`을 Git에 커밋하지 마세요**
   - 이미 `.gitignore`에 추가되어 있습니다
   - 프로덕션에서는 항상 환경 변수 사용

2. **환경 변수 사용**
   - 모든 민감한 데이터는 Render 환경 변수에 있어야 합니다
   - 코드에 자격 증명을 하드코딩하지 마세요

3. **정기 업데이트**
   - 종속성 최신 상태 유지
   - Render 대시보드에서 보안 경고 모니터링

## 📝 체크리스트

배포 전:
- [ ] `Procfile` 생성됨 (`web: gunicorn app:app`)
- [ ] `gunicorn`이 `requirements.txt`에 추가됨
- [ ] `app.py`가 `GOOGLE_CREDENTIALS_JSON` 환경 변수를 사용하도록 업데이트됨
- [ ] 코드가 GitHub에 푸시됨 (Git 배포 사용 시)
- [ ] `credentials.json` 내용이 환경 변수로 붙여넣을 준비됨

배포 후:
- [ ] Render에 모든 환경 변수 설정됨
- [ ] 빌드가 성공적으로 완료됨
- [ ] 앱이 "Live" 상태 표시
- [ ] 양식 제출 테스트 성공
- [ ] 데이터가 Google Sheet에 나타남
- [ ] 앱 URL 접근 가능

## 🎉 성공!

배포가 완료되면 다음을 갖게 됩니다:
- ✅ 영구 URL: `https://your-app-name.onrender.com`
- ✅ 자동 HTTPS (SSL 인증서)
- ✅ Git 푸시 시 자동 배포
- ✅ 무료 호스팅 (제한사항 있음)

앱 URL을 사용자와 공유하면 어디서나 접근할 수 있습니다!

## 📞 도움이 필요하신가요?

- Render 문서: https://render.com/docs
- Render 커뮤니티: https://community.render.com
- Render 대시보드 로그에서 특정 오류 확인

