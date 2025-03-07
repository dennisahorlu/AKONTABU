from flask import Flask, render_template

app=Flask(__name__,static_folder='Static')

@app.route('/')
def csshtml():
    return render_template('index.html')

app.run(host='0.0.0.0', port=80)