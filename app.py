from flask import Flask, render_template, jsonify
import os

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
