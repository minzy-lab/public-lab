from flask import Flask, render_template, jsonify, request
import os
from fortune_engine import FortuneEngine

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

@app.route('/')
def index():
    """메인 페이지"""
    return render_template('index.html')

@app.route('/api/hello')
def api_hello():
    """API 예제"""
    return jsonify({
        'message': 'Hello from Flask!',
        'status': 'success'
    })

@app.route('/about')
def about():
    """소개 페이지"""
    return render_template('about.html')

@app.route('/fortune')
def fortune():
    """운세 페이지"""
    return render_template('fortune.html')

@app.route('/api/fortune', methods=['POST'])
def api_fortune():
    """
    운세 데이터 생성 API

    Request Body:
    {
        "name": "지은",
        "birth_date": "1995-03-15",
        "mbti": "ENFP"  // 선택
    }
    """
    try:
        data = request.get_json()

        # 필수 파라미터 확인
        name = data.get('name')
        birth_date = data.get('birth_date')
        mbti = data.get('mbti', None)

        if not name or not birth_date:
            return jsonify({
                'status': 'error',
                'message': '이름과 생년월일은 필수입니다.'
            }), 400

        # 운세 생성
        fortune_data = FortuneEngine.generate_daily_fortune(
            name=name,
            birth_date=birth_date,
            mbti=mbti
        )

        return jsonify({
            'status': 'success',
            'data': fortune_data
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
