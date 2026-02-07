// API 테스트 함수
async function testAPI() {
    try {
        const response = await fetch('/api/hello');
        const data = await response.json();

        const resultDiv = document.getElementById('api-result');
        resultDiv.innerHTML = `
            <h3>✅ API 응답 성공!</h3>
            <p><strong>메시지:</strong> ${data.message}</p>
            <p><strong>상태:</strong> ${data.status}</p>
        `;
        resultDiv.classList.add('show');
    } catch (error) {
        const resultDiv = document.getElementById('api-result');
        resultDiv.innerHTML = `
            <h3>❌ API 오류</h3>
            <p>${error.message}</p>
        `;
        resultDiv.style.background = '#ffebee';
        resultDiv.classList.add('show');
    }
}

// 페이지 로드 시 실행
document.addEventListener('DOMContentLoaded', () => {
    console.log('Public Lab 웹 서비스가 실행되었습니다! 🚀');
});
