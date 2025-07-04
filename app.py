from flask import Flask, render_template, request
import re

app = Flask(__name__)
kinoko_count = 3
takenoko_count = 5
messages = ['Kinoko is wonderful! See https://moocs.iniad.org/ for details.', 'Takenoko is awesome!']

def auto_link(text):
    pattern = r'(https?://[a-zA-Z0-9\-\._~:/\?#\[\]@!\$&\'\(\)\*\+,;=%]+)'
    return re.sub(pattern, r'<a href="\1">\1</a>', text)

@app.route('/')
def top():
    return render_template('index.html', **vars())

@app.route('/vote', methods=['POST'])
def answer():
    kinoko_percent = kinoko_count / (kinoko_count + takenoko_count) * 100
    takenoko_percent = takenoko_count / (kinoko_count + takenoko_count) * 100

    message_html = ''
    for i, message in enumerate(messages):
        message = auto_link(message)
        alert_class = 'alert-warning ms-5' if i % 2 == 0 else 'alert-success me-5'
        message_html += f'<div class="alert {alert_class}" role="alert">{message}</div>\n'

    return render_template('vote.html', **vars())

if __name__ == '__main__':
    app.run(debug=True)