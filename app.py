from flask import Flask, request, render_template
import pygame
import random
import os


app = Flask(__name__)

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 40

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('game.html')

@app.route('/play')
def play_game():
    pygame.init()
    canvas = pygame.Surface((CANVAS_WIDTH, CANVAS_HEIGHT))
    clock = pygame.time.Clock()

    your_score = 0
    N_CIRCLES = random.randint(1, 7)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        canvas.fill((255, 255, 255))  # Clear the canvas

        for i in range(N_CIRCLES):
            random_circles(canvas)

        if N_CIRCLES == 4:
            message = 'Congratulations! You hit a boundary, You win a prize'
        elif N_CIRCLES == 6:
            message = 'Congratulations! You hit a sixer, Master Blaster! Claim your gift'
        else:
            message = 'You made {} runs'.format(N_CIRCLES)

        your_score += N_CIRCLES

        if your_score >= 50:
            prize = 'Congratulations! You deserve a prize'
            running = False
        else:
            prize = ''

        pygame.image.save(canvas, 'static/canvas.png')  # Save the canvas as an image
        pygame.quit()

        return render_template('play.html', N_CIRCLES=N_CIRCLES, your_score=your_score, message=message, prize=prize)

@app.route('/score/<int:your_score>')
def show_score(your_score):
    if your_score >= 50:
        message = 'Congratulations! You deserve a prize'
    else:
        message = 'Better luck next time!'

    return render_template('score.html', your_score=your_score, message=message)

def random_circles(canvas):
    circle_color = random_color()
    center_x = random.randint(CIRCLE_SIZE // 2, CANVAS_WIDTH - CIRCLE_SIZE // 2)
    center_y = random.randint(CIRCLE_SIZE // 2, CANVAS_HEIGHT - CIRCLE_SIZE // 2)
    pygame.draw.circle(canvas, circle_color, (center_x, center_y), CIRCLE_SIZE // 2)

def random_color():
    colors = [(0, 0, 255), (128, 0, 128), (250, 128, 114), (173, 216, 230), (0, 255, 255), (34, 139, 34)]
    return random.choice(colors)

if __name__ == '__main__':
    app.run(debug=True)
