from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template('game.html', play=True)
    return render_template('game.html', play=False)

@app.route('/play', methods=['POST'])
def play():
    hit = int(request.form['hit'])
    score = random.randint(1, 6)
    if score > 4:
        message = "Wow! Great Job."
    elif score == 4:
        message = "Congratulations! Good Job!"
    else:
        message = "Oh no! Low score. Better luck next time."
    return render_template('result.html', score=score, message=message)

if __name__ == '__main__':
    app.run(debug=True)
