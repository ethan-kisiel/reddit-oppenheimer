from flask import Flask, render_template, redirect, request
import asyncio
from terminator import Arnold

error = ""

def validate_fields(args: [str]) -> bool:
    for element in args:
        if not element:
            return False
    return True

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test super secret'

@app.route("/help")
def help():
    return render_template('help.html')

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