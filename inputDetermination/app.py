from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            if number % 2 == 0:
                result = "even number"
            else:
                result = "odd number"
        except ValueError:
            result = "not an integer"
        return redirect(url_for('result', result=result))
    return render_template('home.html')

@app.route('/result')
def result():
    result = request.args.get('result')
    if result is None:
        return "Error: No query parameter included."
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
