from flask import Flask

app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def health_check():
    return {"status": "ok"}

@app.route('/api/test', methods=['GET'])
def return_test_status():
    return {"status": "aarkster-test-ok"}

@app.route('/api/test-info', methods=['GET'])
def get_test_info():
    return {"status": "aarkster-test-info-ok"}

@app.route('/api/agent-verification', methods=['GET'])
def agent_verification():
    return {"status": "aarkster-agent-verification-ok"}
