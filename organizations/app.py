from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


organizations = ['AHC', 'CAB', 'GPSG', 'CAR', 'ANS']


registered_users = {}


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        organization = request.form['organization']

        # Backend validation
        if not name or not organization:
            return render_template('home.html', error='Both name and organization are required.', organizations=organizations)

        if organization not in organizations:
            return render_template('home.html', error='Invalid organization selected.', organizations=organizations)

        # Add user to dictionary
        registered_users[name] = organization

        return redirect(url_for('registered_users_list'))

    return render_template('home.html', organizations=organizations)


@app.route('/registered_users')
def registered_users_list():
    return render_template('registered_users.html', users=registered_users)


if __name__ == '__main__':
    app.run(debug=True)
