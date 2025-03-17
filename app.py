from flask import Flask, render_template

app=Flask(__name__,static_folder='Static', template_folder='templates')

@app.route('/')
def csshtml():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('Signup.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
