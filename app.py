from flask import Flask, render_template, request, redirect, url_for

from utils import load_data_from_json_file, write_data_to_json_file

app = Flask(__name__)


@app.route('/')
def index():
    blog_posts = load_data_from_json_file('storage.json')
    return render_template('index.html', posts=blog_posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        all_posts = load_data_from_json_file('storage.json')

        new_post = {
            'id': len(all_posts) + 1,
            'title': request.form.get('title'),
            'author': request.form.get('author'),
            'content': request.form.get('content')
        }
        all_posts.append(new_post)
        write_data_to_json_file('storage.json', all_posts)

        return redirect(url_for('index'))

    return render_template('add.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)