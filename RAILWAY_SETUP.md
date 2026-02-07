# Railway 배포 가이드

## 🚂 배포 단계

### 1. Railway 프로젝트 생성
1. https://railway.app 접속
2. GitHub 계정으로 로그인
3. "New Project" → "Deploy from GitHub repo"
4. `minzy-lab/public-lab` 선택
5. `work` 브랜치 선택

### 2. 자동 배포 시작
- Railway가 `railway.json` 감지
- 자동으로 Python 환경 설정
- `requirements.txt`로 패키지 설치
- Gunicorn으로 앱 실행

### 3. 도메인 확인
- 배포 완료 후 자동 생성된 URL 확인
- 예: `https://nangmanism-production.up.railway.app`
- Settings → Generate Domain으로 URL 생성

---

## 🔧 배포 후 설정

### 환경변수 추가 (선택)
Railway 대시보드에서 Variables 탭:
```
SECRET_KEY=랜덤한-시크릿-키
FLASK_ENV=production
```

### 도메인 연결 (선택)
1. Settings → Custom Domain
2. 원하는 도메인 추가
3. DNS 설정 (Railway가 안내)

---

## 📱 접속 URL

배포 완료 후:
- **운세 페이지**: `https://your-app.up.railway.app/fortune`
- **API 테스트**: `https://your-app.up.railway.app/api/hello`

---

## 🐛 문제 해결

### 배포 실패 시
1. Railway 대시보드 → Deployments → 로그 확인
2. 빌드 에러: `requirements.txt` 확인
3. 런타임 에러: 환경변수 확인

### 앱이 안 켜질 때
- Railway는 비활성 15분 후 자동 슬립
- 첫 요청 시 자동 깨어남 (3-5초 소요)
- 유료 플랜으로 Always On 가능

---

## 💰 비용

### Free Tier
- $5 credit/월 (약 500시간 실행 가능)
- 대부분 무료로 충분

### 비용 절감 팁
1. 사용 안 할 때는 프로젝트 삭제
2. 개발용과 프로덕션용 분리
3. 환경변수로 민감 정보 관리

---

## 🔄 자동 배포 설정

Railway는 GitHub와 자동 연동:
- `work` 브랜치에 push → 자동 배포
- PR 생성 → Preview 환경 자동 생성
- 로그와 상태 실시간 확인 가능

---

## 📊 모니터링

Railway 대시보드에서 확인 가능:
- CPU/메모리 사용량
- 네트워크 트래픽
- 배포 히스토리
- 실시간 로그

---

## 🎯 다음 단계

1. [ ] Railway 배포 완료
2. [ ] 모바일에서 테스트
3. [ ] PostgreSQL 데이터베이스 추가 (필요시)
4. [ ] 커스텀 도메인 연결 (선택)
5. [ ] 모니터링 설정 (Sentry 등)

---

## 🆘 도움말

- Railway 문서: https://docs.railway.app
- Discord 커뮤니티: https://discord.gg/railway
- 질문이 있으면 Railway 대시보드에서 Support 클릭
