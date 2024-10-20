from flask import Flask, request, jsonify
from generate import PoemGenerator  
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许跨域请求

# 初始化诗歌生成器
poem_generator = PoemGenerator()

@app.route('/generate_poem', methods=['POST'])
def generate_poem():
    data = request.get_json()
    keywords = data.get('keywords', '')
    max_length = data.get('max_length', 150)  # 您可以根据需要调整默认值

    # 生成诗歌
    poem = poem_generator.generate_poem(keywords, max_length)

    # 返回生成的诗歌
    return jsonify({'poem': poem})

if __name__ == '__main__':
    app.run(debug=True)
