from flask import Flask, render_template, request, Response, send_file, jsonify
import requests
import json

app = Flask(__name__)


@app.route("/api/", methods=['GET'])
def generate():
    try:
        keyword = request.args.get('keyword')
        data = {
            "text": keyword,
            "num_samples": 1,
            "length": 30
        }
        URL = "https://feature-add-torch-serve-gpt-2-server-gkswjdzz.endpoint.ainize.ai/infer/gpt2-PopSongLyrics"
        headers = {
                "Content-Type": "application/json",
        }
        res = requests.post(URL, headers=headers, data=json.dumps(data))
        res = res.json()
        return res
    except Exception as e:
        return jsonify(e), 500


# Health Check
@app.route('/healthz')
def health():
    return "ok", 200


@app.route('/')
def main():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
