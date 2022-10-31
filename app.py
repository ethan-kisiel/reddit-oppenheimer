from flask import Flask, render_template, redirect, request
import asyncio
from terminator import Arnold
from os.path import join as join_path
from os import environ as env

SECRET_KEY = env.get('SECRET_KEY')
print(f'SECRET SECRET SECRET KEY: ->> {SECRET_KEY}')
IMAGES_FOLDER = join_path('static', 'imgs')

def validate_fields(args: list[str]) -> bool:
    for element in args:
        if not element:
            return False
    return True

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['IMG_FOLDER'] = IMAGES_FOLDER

@app.route("/help")
def help():
    image_one_url = join_path(app.config['IMG_FOLDER'], 'step_one.png')
    image_two_url = join_path(app.config['IMG_FOLDER'], 'step_two.png')
    image_three_url = join_path(app.config['IMG_FOLDER'], 'step_three.png')

    return render_template('help.html', image_one_url=image_one_url,
                                image_two_url=image_two_url,
                                image_three_url=image_three_url)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        client_id = request.form['client_id']
        client_secret = request.form['secret']
        username = request.form['username']
        password = request.form['password']

        valid_args = validate_fields([
                client_id,
                client_secret,
                username,
                password])
        
        if valid_args:
            # deletion will happen here
            result = asyncio.run(Arnold.commence_deletion(
                    client_id=client_id,
                    client_secret=client_secret,
                    username=username,
                    password=password))

            if result is not None:
                # an error occured in Arnold.commence_deletion
                error = result
                return render_template('index.html', error=error)
            else:
                # if successful deletion, redirect to reddit user page 
                return redirect(f'https://www.reddit.com/user/{username}')
        else:
            error = 'All fields are required.'
            return render_template('index.html', error=error)
    else:
        return render_template('index.html', error="")



if __name__ == "__main__":
    app.run(host="0.0.0.0")