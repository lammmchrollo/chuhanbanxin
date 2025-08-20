from flask import Flask, jsonify, render_template
import json
import os

app = Flask(__name__)

# Xác định đường dẫn tuyệt đối đến thư mục chứa file chạy (chuhan.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Tạo đường dẫn chính xác đến file vocab.json
VOCAB_PATH = os.path.join(BASE_DIR, 'vocab.json')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/vocab', methods=['GET']) # Chỉ cho phép phương thức GET
def vocab():
    # --- Chức năng POST đã được chú thích lại vì không hoạt động tốt trên hosting ---
    # if request.method == 'POST':
    #     new_word = request.get_json()
    #     with open(VOCAB_PATH, 'r', encoding='utf-8') as f:
    #         data = json.load(f)
    #     data.append(new_word)
    #     with open(VOCAB_PATH, 'w', encoding='utf-8') as f:
    #         json.dump(data, f, ensure_ascii=False, indent=4)
    #     return 'Đã thêm từ mới!', 200
    # else: # Chỉ chạy phần GET
    with open(VOCAB_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

# Dòng app.run() đã được xóa. Máy chủ hosting (ví dụ: Gunicorn) sẽ tự khởi chạy app.
#if __name__ == '__main__':
  # app.run(debug=True)