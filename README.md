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

## 배포

Vercel, Heroku, Railway 등에서 쉽게 배포 가능합니다.
