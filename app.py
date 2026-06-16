from flask import Flask, render_template

from utils import load_data_from_json_file

app = Flask(__name__)


@app.route('/')
def index():
    blog_posts = load_data_from_json_file('storage.json')
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)