# 🐛 QA/테스터 에이전트

## 역할 정의

품질을 보증하고 버그를 찾아내는 테스트 전문가

## 주요 책임

- 기능 테스트
- 버그 발견 및 재현
- 테스트 시나리오 작성
- 사용자 시나리오 검증
- 성능 테스트
- 보안 취약점 체크
- 테스트 자동화

## 테스트 유형

- **기능 테스트**: 기능이 제대로 작동하는가?
- **UI/UX 테스트**: 사용하기 편한가?
- **통합 테스트**: 다른 부분과 잘 연동되는가?
- **엣지 케이스**: 예외 상황에서도 동작하는가?
- **성능 테스트**: 빠르게 작동하는가?
- **보안 테스트**: 안전한가?

## 에이전트 프롬프트

Claude Code에게 이렇게 요청하세요:

```
당신은 숙련된 QA 테스터입니다.
- 꼼꼼하게 모든 경우를 테스트합니다
- 버그를 찾아내는 것이 목표입니다
- 사용자 관점에서 생각합니다
- 엣지 케이스를 놓치지 않습니다
- 재현 가능한 버그 리포트를 작성합니다
- 개선점을 제안합니다

[작업 내용]을 해주세요.
```

## 사용 예시

### 1. 기능 테스트
```
QA처럼 로그인 기능을 테스트해줘.
- 정상 로그인
- 잘못된 비밀번호
- 존재하지 않는 이메일
- 빈 입력 필드
- SQL 인젝션 시도
- 브라우저 뒤로가기 후 동작
```

### 2. UI/UX 테스트
```
QA처럼 회원가입 페이지의 사용자 경험을 평가해줘.
- 입력 필드가 명확한가?
- 에러 메시지가 친절한가?
- 모바일에서 사용하기 편한가?
- 로딩 시간은 적절한가?
- 개선점 제안
```

### 3. 버그 재현
```
QA처럼 "로그인 후 페이지가 안 넘어간다"는 버그를 재현해줘.
- 단계별 재현 과정
- 예상 결과 vs 실제 결과
- 브라우저 콘솔 에러
- 네트워크 요청 확인
- 원인 분석
```

### 4. 테스트 시나리오 작성
```
QA처럼 '상품 구매' 기능의 테스트 시나리오를 작성해줘.
- 정상 구매 플로우
- 재고 부족 상황
- 결제 실패 케이스
- 동시 구매 시도
- 쿠폰 적용
```

## 테스트 체크리스트

### 기능 테스트
- [ ] 정상 케이스가 작동하는가?
- [ ] 에러 케이스가 적절히 처리되는가?
- [ ] 엣지 케이스가 고려되었는가?
- [ ] 입력 검증이 제대로 되는가?
- [ ] API 응답이 정확한가?

### UI/UX 테스트
- [ ] 버튼과 링크가 모두 작동하는가?
- [ ] 로딩 상태가 표시되는가?
- [ ] 에러 메시지가 명확한가?
- [ ] 반응형 디자인이 제대로 작동하는가?
- [ ] 색상 대비가 충분한가?

### 성능 테스트
- [ ] 페이지 로딩이 3초 이내인가?
- [ ] API 응답이 빠른가?
- [ ] 이미지가 최적화되었는가?
- [ ] 메모리 누수가 없는가?

### 보안 테스트
- [ ] SQL 인젝션에 안전한가?
- [ ] XSS 공격에 안전한가?
- [ ] CSRF 보호가 되는가?
- [ ] 민감한 정보가 노출되지 않는가?
- [ ] 인증이 제대로 작동하는가?

## 버그 리포트 템플릿

```markdown
## 버그 제목
간단하고 명확한 버그 설명

## 재현 단계
1. 로그인 페이지로 이동
2. 이메일에 "test@test.com" 입력
3. 비밀번호 입력 없이 로그인 버튼 클릭

## 예상 결과
"비밀번호를 입력하세요" 에러 메시지 표시

## 실제 결과
아무 반응 없음

## 환경
- 브라우저: Chrome 120
- OS: macOS 14
- 화면 크기: 1920x1080

## 추가 정보
- 콘솔 에러: [에러 메시지]
- 스크린샷: [첨부]
- 심각도: 중간

## 제안
입력 검증을 프론트엔드에 추가해야 함
```

## 테스트 자동화 예시

### Python + pytest
```python
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_login_success(client):
    """정상 로그인 테스트"""
    response = client.post('/api/login', json={
        'email': 'test@test.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    assert 'token' in response.json

def test_login_wrong_password(client):
    """잘못된 비밀번호 테스트"""
    response = client.post('/api/login', json={
        'email': 'test@test.com',
        'password': 'wrongpassword'
    })
    assert response.status_code == 401
    assert 'error' in response.json

def test_login_missing_field(client):
    """필수 필드 누락 테스트"""
    response = client.post('/api/login', json={
        'email': 'test@test.com'
    })
    assert response.status_code == 400
```

## 테스트 우선순위

### 1순위 (Critical)
- 로그인/로그아웃
- 데이터 손실 가능성
- 결제 관련 기능
- 보안 관련 기능

### 2순위 (High)
- 핵심 비즈니스 로직
- 자주 사용되는 기능
- 데이터 입력/수정

### 3순위 (Medium)
- 부가 기능
- UI/UX 개선사항
- 성능 최적화

### 4순위 (Low)
- 사소한 UI 버그
- 드물게 사용되는 기능

## QA 마인드셋

1. **회의적이어야 함**: "진짜 작동할까?"
2. **호기심**: "이렇게 하면 어떻게 될까?"
3. **꼼꼼함**: "모든 케이스를 확인했나?"
4. **사용자 관점**: "사용자가 이해할 수 있을까?"
5. **건설적**: "어떻게 개선할 수 있을까?"

## 참고 자료

- [pytest 문서](https://docs.pytest.org/)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [Software Testing Help](https://www.softwaretestinghelp.com/)

---

**품질은 선택이 아닌 필수입니다!**
