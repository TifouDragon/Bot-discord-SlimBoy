
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 SlimBoy Discord Bot is alive! ✅"

@app.route('/status')
def status():
    return {
        "status": "online",
        "bot": "SlimBoy", 
        "uptime": "active"
    }

@app.route('/health')
def health():
    return "OK", 200

def run():
    app.run(host='0.0.0.0', port=8080, debug=False)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()
