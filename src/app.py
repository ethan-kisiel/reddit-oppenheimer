from flask import Flask, render_template, redirect, request
import asyncio
from terminator import Arnold
error = ""
app = Flask(__name__)
        
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # deletion will happen here
        asyncio.run(Arnold.commence_deletion(username=username, password=password))
        return redirect(f'https://www.reddit.com/user/{username}')
    else:
        return render_template('index.html', error=error)



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)