# from flask import Flask, request, render_template

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def multiply():
#     if request.method == 'POST':
#         num1 = float(request.form['num1'])
#         num2 = float(request.form['num2'])
#         result = num1 * num2
#         return render_template('result.html', result=result)
#     return render_template('multiply.html')

# if __name__ == '__main__':
#     app.run(debug=True)
