# Public Lab

Flask 기반 웹 서비스 프로젝트

## 시작하기

### 1. 가상환경 생성 및 활성화

```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# 또는
venv\Scripts\activate  # Windows
```

### 2. 패키지 설치

```bash
pip install -r requirements.txt
```

### 3. 서버 실행

```bash
python app.py
```

브라우저에서 `http://localhost:5000` 접속

## 프로젝트 구조

```
public-lab/
├── app.py              # 메인 애플리케이션
├── requirements.txt    # 필요한 패키지 목록
├── templates/          # HTML 템플릿
│   ├── base.html
│   ├── index.html
│   └── about.html
├── static/            # CSS, JS, 이미지
│   ├── css/
│   └── js/
├── agents/            # AI 에이전트 역할 정의
│   ├── README.md
│   ├── backend-developer.md
│   ├── frontend-developer.md
│   ├── qa-tester.md
│   ├── security-expert.md
│   └── product-manager.md
├── docs/              # 기획서 및 문서
│   ├── README.md
│   └── 운세-서비스-기획서.md
└── README.md          # 이 파일
```

## API 엔드포인트

- `GET /` - 메인 페이지
- `GET /about` - 소개 페이지
- `GET /api/hello` - API 예제

## 개발 팁

- 코드 수정 시 자동으로 서버가 재시작됩니다 (debug=True)
- 새로운 페이지는 `templates/` 폴더에 추가
- 스타일은 `static/css/` 폴더에 추가

## 🤖 AI 에이전트 팀

이 프로젝트는 5가지 AI 에이전트 역할을 정의하여 효율적인 개발을 지원합니다:

- **백엔드 개발자**: API, 데이터베이스 개발
- **프론트엔드 개발자**: UI/UX, 화면 개발
- **QA/테스터**: 품질 보증, 버그 발견
- **보안 전문가**: 개인정보 보호, 보안 취약점 분석
- **PM/기획자**: 제품 기획, 우선순위 결정

자세한 내용은 [`agents/README.md`](./agents/README.md)를 참고하세요.

### 사용 예시
```
"백엔드 개발자처럼 사용자 로그인 API를 만들어줘"
"프론트엔드 개발자처럼 로그인 페이지를 디자인해줘"
"보안 전문가처럼 생년월일 암호화 코드를 작성해줘"
"QA처럼 로그인 기능을 테스트해줘"
"PM처럼 다음 스프린트 계획을 세워줘"
```

## 배포

Vercel, Heroku, Railway 등에서 쉽게 배포 가능합니다.
