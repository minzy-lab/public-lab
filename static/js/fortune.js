/**
 * 운세 페이지 JavaScript
 */

// 화면 전환 함수
function showScreen(screenId) {
    document.querySelectorAll('.screen').forEach(screen => {
        screen.classList.remove('active');
    });
    document.getElementById(screenId).classList.add('active');
}

// 별 표시 생성
function createStars(score, containerClass = '') {
    const fullStars = Math.floor(score);
    const hasHalfStar = score % 1 >= 0.5;
    const emptyStars = 5 - fullStars - (hasHalfStar ? 1 : 0);

    let html = '';

    // 꽉 찬 별
    for (let i = 0; i < fullStars; i++) {
        html += '<span class="star">⭐</span>';
    }

    // 반 별 (간단히 빈 별로 대체)
    if (hasHalfStar) {
        html += '<span class="star">⭐</span>';
    }

    // 빈 별
    for (let i = 0; i < emptyStars; i++) {
        html += '<span class="star empty">☆</span>';
    }

    return html;
}

// 운세 데이터 표시
function displayFortune(data) {
    const { user, date, scores, messages, actions, lucky } = data;

    // 날짜 표시
    document.getElementById('result-date').textContent = date.display;

    // 사용자 정보
    const greeting = `${user.name}님의 운세`;
    document.getElementById('user-greeting').textContent = greeting;

    // 별자리 배지
    const zodiacBadge = `${user.zodiac.emoji} ${user.zodiac.sign}`;
    document.getElementById('zodiac-badge').textContent = zodiacBadge;

    // MBTI 배지
    const mbtiBadge = document.getElementById('mbti-badge');
    if (user.mbti) {
        mbtiBadge.textContent = user.mbti;
        mbtiBadge.style.display = 'inline-block';
    } else {
        mbtiBadge.style.display = 'none';
    }

    // 종합 운세 점수
    document.getElementById('overall-score').textContent = scores.overall;
    document.getElementById('overall-stars').innerHTML = createStars(scores.overall);
    document.getElementById('summary-message').textContent = messages.summary;

    // MBTI 메시지
    const mbtiMessage = document.getElementById('mbti-message');
    if (messages.mbti) {
        mbtiMessage.textContent = messages.mbti;
        mbtiMessage.style.display = 'block';
    } else {
        mbtiMessage.style.display = 'none';
    }

    // 카테고리별 점수
    const categories = [
        { key: 'love', name: '애정운' },
        { key: 'money', name: '금전운' },
        { key: 'health', name: '건강운' },
        { key: 'work', name: '직장운' }
    ];

    categories.forEach(category => {
        const score = scores[category.key];
        document.getElementById(`${category.key}-score`).textContent = score;
        document.getElementById(`${category.key}-stars`).innerHTML = createStars(score);
    });

    // 오늘 하면 좋은 일
    const doList = document.getElementById('do-list');
    doList.innerHTML = '';
    actions.do.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item;
        doList.appendChild(li);
    });

    // 오늘 피해야 할 일
    const avoidList = document.getElementById('avoid-list');
    avoidList.innerHTML = '';
    actions.avoid.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item;
        avoidList.appendChild(li);
    });

    // 행운 아이템
    document.getElementById('lucky-color').textContent = lucky.color;
    document.getElementById('lucky-item').textContent = lucky.item;

    // 행운의 숫자
    const numberBalls = document.getElementById('lucky-numbers');
    numberBalls.innerHTML = '';
    lucky.numbers.forEach(num => {
        const ball = document.createElement('div');
        ball.className = 'number-ball';
        ball.textContent = num;
        numberBalls.appendChild(ball);
    });

    // 결과 화면 표시
    showScreen('result-screen');
}

// 폼 제출 처리
document.getElementById('fortune-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    // 폼 데이터 수집
    const formData = {
        name: document.getElementById('name').value,
        birth_date: document.getElementById('birth_date').value,
        mbti: document.getElementById('mbti').value || null
    };

    // 로딩 화면 표시
    showScreen('loading-screen');

    try {
        // API 호출
        const response = await fetch('/api/fortune', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        const result = await response.json();

        if (result.status === 'success') {
            // 약간의 딜레이 후 결과 표시 (로딩 효과)
            setTimeout(() => {
                displayFortune(result.data);
            }, 1500);
        } else {
            alert('오류가 발생했습니다: ' + result.message);
            showScreen('input-screen');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('운세를 불러오는 중 오류가 발생했습니다.');
        showScreen('input-screen');
    }
});

// 페이지 로드 시 오늘 날짜를 최대값으로 설정
document.addEventListener('DOMContentLoaded', () => {
    const birthDateInput = document.getElementById('birth_date');
    const today = new Date().toISOString().split('T')[0];
    birthDateInput.setAttribute('max', today);

    // 기본값으로 1995년 설정 (예시)
    birthDateInput.value = '1995-01-01';
});
