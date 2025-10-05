from flask import Flask, render_template
app = Flask (__name__)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/premium')
def premium():
    return render_template('premium.html')

if __name__ == '__main__':
    app.run(debug=True)