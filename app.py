# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoTokenizer, AutoModel
import torch

app = Flask(__name__)
CORS(app)

tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True).quantize(4).half().cuda()
model.eval()

history = {}

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_id = data.get('user_id', 'default')
    message = data['message']
    message = "请用以下的意象写一首现代诗：" + message

    if user_id not in history:
        history[user_id] = []

    response, history[user_id] = model.chat(tokenizer, message, history=history[user_id])
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
