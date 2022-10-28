from flask import Flask, render_template, url_for, request

error = ""
app = Flask(__name__)
        
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # deletion will happen here
        return f"{username}, {password}"
    else:
        return render_template('index.html', error=error)



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)