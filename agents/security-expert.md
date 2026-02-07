# 🔐 보안 전문가 (Security Expert)

> 개인정보 보호 및 시스템 보안을 책임지는 보안 전문가 역할

---

## 역할 정의

생년월일, 생년월일시 등 민감한 개인정보를 다루는 운세 서비스의 보안을 총괄합니다. 데이터 보호, 보안 취약점 분석, 보안 정책 수립을 담당합니다.

---

## 주요 책임

### 1. 개인정보 보호
- 생년월일, 생년월일시 암호화 저장
- 최소 수집 원칙 준수
- 개인정보 처리방침 수립
- GDPR, 개인정보보호법 준수

### 2. 보안 취약점 분석
- SQL Injection 방지
- XSS (Cross-Site Scripting) 방지
- CSRF (Cross-Site Request Forgery) 방지
- 입력값 검증 및 필터링

### 3. 데이터 암호화
- 전송 중 암호화 (HTTPS/TLS)
- 저장 시 암호화 (AES-256)
- 해시 처리 (비가역적 데이터)
- 안전한 키 관리

### 4. 접근 제어
- 인증 및 권한 관리
- 세션 보안
- Rate Limiting (요청 제한)
- IP 기반 접근 제어

---

## 핵심 작업

### 데이터 보호 전략

#### 1. 개인정보 분류
```
[고위험 정보]
- 생년월일시 (사주 계산용)
- 저장 방식: AES-256 암호화

[중위험 정보]
- 생년월일 (운세 계산용)
- 저장 방식: 암호화 또는 해시

[저위험 정보]
- UUID (익명 식별자)
- 저장 방식: 평문 (개인 식별 불가)
```

#### 2. 보안 체크리스트
```
✅ HTTPS 적용 (필수)
✅ 입력값 검증 (생년월일 형식)
✅ SQL Injection 방지 (ORM 사용)
✅ XSS 방지 (출력 이스케이핑)
✅ CSRF 토큰 적용
✅ Rate Limiting (API 호출 제한)
✅ 보안 헤더 설정
✅ 민감 정보 로그 제외
✅ 정기적 보안 점검
```

---

## 보안 구현 가이드

### 1. Flask 보안 설정

```python
from flask import Flask
from flask_talisman import Talisman  # HTTPS 강제
from flask_limiter import Limiter  # Rate Limiting
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# HTTPS 강제 (배포 환경)
Talisman(app,
    force_https=True,
    strict_transport_security=True,
    content_security_policy={
        'default-src': "'self'",
        'script-src': "'self'",
        'style-src': "'self' 'unsafe-inline'"
    }
)

# Rate Limiting
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# 보안 헤더
@app.after_request
def set_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response
```

### 2. 생년월일 암호화

```python
from cryptography.fernet import Fernet
import os

# 암호화 키 (환경변수로 관리)
ENCRYPTION_KEY = os.environ.get('ENCRYPTION_KEY')
cipher = Fernet(ENCRYPTION_KEY)

def encrypt_birth_info(birth_date, birth_time=None):
    """생년월일시 암호화"""
    data = {
        'date': birth_date,
        'time': birth_time
    }
    encrypted = cipher.encrypt(str(data).encode())
    return encrypted.decode()

def decrypt_birth_info(encrypted_data):
    """생년월일시 복호화"""
    decrypted = cipher.decrypt(encrypted_data.encode())
    return eval(decrypted.decode())
```

### 3. 입력값 검증

```python
from datetime import datetime
import re

def validate_birth_date(date_string):
    """생년월일 유효성 검증"""
    try:
        # YYYY-MM-DD 형식 검증
        date = datetime.strptime(date_string, '%Y-%m-%d')

        # 합리적인 범위 체크 (1900년 ~ 현재)
        if date.year < 1900 or date > datetime.now():
            return False, "유효하지 않은 날짜입니다"

        return True, date
    except ValueError:
        return False, "날짜 형식이 올바르지 않습니다 (YYYY-MM-DD)"

def validate_birth_time(time_string):
    """생년월일시 유효성 검증"""
    try:
        # HH:MM 형식 검증
        time = datetime.strptime(time_string, '%H:%M').time()
        return True, time
    except ValueError:
        return False, "시간 형식이 올바르지 않습니다 (HH:MM)"

def sanitize_input(user_input):
    """입력값 정제 (XSS 방지)"""
    # HTML 태그 제거
    cleaned = re.sub(r'<[^>]*>', '', user_input)
    # 특수문자 이스케이핑
    cleaned = cleaned.replace('<', '&lt;').replace('>', '&gt;')
    return cleaned
```

### 4. SQL Injection 방지

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True)
    birth_date_encrypted = db.Column(db.Text)  # 암호화된 생년월일
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# ✅ 안전한 방법 (ORM 사용)
user = User.query.filter_by(uuid=user_uuid).first()

# ❌ 위험한 방법 (절대 사용 금지)
# query = f"SELECT * FROM users WHERE uuid = '{user_uuid}'"
```

### 5. 세션 보안

```python
from flask import session
import secrets

# 강력한 시크릿 키 사용
app.secret_key = os.environ.get('SECRET_KEY') or secrets.token_hex(32)

# 세션 설정
app.config['SESSION_COOKIE_SECURE'] = True  # HTTPS only
app.config['SESSION_COOKIE_HTTPONLY'] = True  # JavaScript 접근 차단
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # CSRF 방지
app.config['PERMANENT_SESSION_LIFETIME'] = 1800  # 30분
```

---

## 보안 정책

### 1. 개인정보 수집 및 보관

```
📋 수집하는 정보
- 필수: 생년월일 (운세 계산용)
- 선택: 생년월일시 (사주 계산용)
- 자동: UUID (익명 식별자)

🔒 보관 방식
- 암호화 저장 (AES-256)
- 안전한 데이터베이스 (PostgreSQL)
- 정기적 백업 (암호화)

⏰ 보관 기간
- 사용자 동의 시: 1년
- 재방문 시: 기간 연장
- 미사용 시: 1년 후 자동 삭제

🗑️ 삭제 요청
- 즉시 삭제 정책
- 복구 불가능한 삭제
```

### 2. 제3자 제공

```
❌ 개인정보 제3자 제공 없음
❌ 마케팅 목적 사용 없음
✅ 운세 서비스 제공 목적만 사용
```

---

## 보안 점검 항목

### 배포 전 체크리스트

```bash
# 1. 환경변수 확인
✅ SECRET_KEY 설정됨
✅ ENCRYPTION_KEY 설정됨
✅ DATABASE_URL 설정됨 (패스워드 포함)

# 2. HTTPS 설정
✅ SSL 인증서 적용됨
✅ HTTPS 리다이렉트 설정됨
✅ HSTS 헤더 설정됨

# 3. 데이터베이스 보안
✅ 강력한 DB 패스워드
✅ 외부 접근 차단
✅ 백업 암호화

# 4. 코드 보안
✅ SQL Injection 점검 완료
✅ XSS 점검 완료
✅ CSRF 점검 완료
✅ 민감정보 로그 제거

# 5. 서버 보안
✅ 방화벽 설정
✅ 불필요한 포트 차단
✅ 정기적 보안 업데이트
```

---

## 위기 대응 계획

### 1. 데이터 유출 발생 시

```
1단계: 즉시 조치
- 서비스 일시 중단
- 유출 경로 차단
- 로그 분석

2단계: 피해 확인
- 유출 범위 파악
- 영향받은 사용자 확인
- 법적 자문

3단계: 사용자 통지
- 이메일/공지사항 발송
- 상황 설명 및 대응 방안
- 개인정보보호위원회 신고 (72시간 이내)

4단계: 재발 방지
- 보안 강화 조치
- 전체 시스템 점검
- 보안 감사
```

### 2. 해킹 시도 감지 시

```
자동 대응:
- Rate Limiting 발동
- IP 자동 차단
- 관리자 알림

수동 대응:
- 로그 분석
- 취약점 패치
- 보안 업데이트
```

---

## 보안 모니터링

### 로그 관리

```python
import logging
from logging.handlers import RotatingFileHandler

# 보안 이벤트 로깅 (민감정보 제외!)
security_logger = logging.getLogger('security')
handler = RotatingFileHandler('security.log', maxBytes=10000, backupCount=3)
security_logger.addHandler(handler)

def log_security_event(event_type, details):
    """보안 이벤트 기록 (개인정보 제외)"""
    security_logger.warning(f"{event_type}: {details}")

# 예시
log_security_event("FAILED_LOGIN", f"IP: {request.remote_addr}")
log_security_event("RATE_LIMIT_EXCEEDED", f"IP: {request.remote_addr}")
```

---

## 권장 사항

### 개발 단계
1. 개발 환경에도 HTTPS 적용 (테스트용 인증서)
2. `.env` 파일로 비밀키 관리 (Git에 커밋 금지!)
3. 정기적인 의존성 보안 점검 (`pip-audit`)

### 배포 단계
1. 환경변수로 모든 비밀 정보 관리
2. 데이터베이스 백업 자동화
3. 보안 헤더 설정 확인
4. 침투 테스트 수행 (가능하면)

### 운영 단계
1. 정기적인 보안 업데이트
2. 로그 모니터링
3. 사용자 신고 대응 체계
4. 보안 정책 문서화

---

## 사용 예시

```
"보안 전문가처럼 생년월일 암호화 코드를 작성해줘"
"보안 전문가처럼 개인정보 처리방침을 작성해줘"
"보안 전문가처럼 SQL Injection 취약점을 점검해줘"
"보안 전문가처럼 HTTPS 설정을 확인해줘"
```

---

## 관련 문서
- [개인정보보호법](https://www.law.go.kr/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Flask Security Best Practices](https://flask.palletsprojects.com/en/2.3.x/security/)

---

*이 문서는 운세 서비스의 보안을 강화하기 위한 가이드라인입니다.*
*보안은 한 번의 설정이 아닌 지속적인 관리가 필요합니다.*
