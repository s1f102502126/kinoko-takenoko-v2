from flask import Flask, render_template, request
app = Flask(__name__)
kinoko_count = 3
takenoko_count = 5
messages = ['Kinoko is wonderful!', 'Takenoko is awesome!']

@app.route('/')
def top():
    return render_template('index.html', **vars())

@app.route('/vote', methods=['POST'])
def answer():
    kinoko_percent = kinoko_count / (kinoko_count + takenoko_count) * 100
    takenoko_percent = takenoko_count / (kinoko_count + takenoko_count) * 100

    message_html = ''
    for i in range(len(messages)):
        message = messages[i]
        message = re.sub(r'&', r'&amp;', message)
        message = re.sub(r'<', r'&lt;', message)
        message = re.sub(r'>', r'&gt;', message)
        message_html += '<div class="alert {1}" role="alert">{0}</div>\n'.format(
            message, 'alert-warning ms-5' if i % 2 == 0 else 'alert-success me-5')

    return render_template('vote.html', **vars())

if __name__ == '__main__':
    app.run(debug=True)
