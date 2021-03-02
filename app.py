from flask import Flask, render_template, request, send_file, session, url_for, flash

app = Flask(__name__,static_folder='static',template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080, threaded=True)
