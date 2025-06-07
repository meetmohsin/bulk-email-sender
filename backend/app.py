from flask import Flask, request, jsonify
from mailer import send_email

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send():
    data = request.get_json()
    subject = data.get('subject')
    body = data.get('body')
    recipients = data.get('recipients', [])
    for email in recipients:
        send_email(subject, body, email)
    return jsonify({"status": "Emails sent"}), 200

if __name__ == '__main__':
    app.run(debug=True)
