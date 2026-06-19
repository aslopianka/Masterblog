"""
This module contains the main Flask application for the Masterblock blog.
It handles routing and rendering for the blog posts.
"""
from flask import Flask, render_template, request, redirect, url_for

from utils import load_data_from_json_file, write_data_to_json_file, fetch_post_by_id, write_data_to_json_file_by_id

app = Flask(__name__)


@app.route('/')
def index():
    """
    Render the home page with all blog posts.
    """
    blog_posts = load_data_from_json_file('storage.json')
    return render_template('index.html', posts=blog_posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Handle adding a new blog post.
    GET: Render the add post form.
    POST: Save the new post and redirect to index.
    """
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


@app.route('/delete/<int:post_id>', methods=['DELETE'])
def delete(post_id):
    """
    Delete a blog post by its ID and redirect to index.
    """
    all_posts = load_data_from_json_file('storage.json')
    all_posts = [post for post in all_posts if post['id'] != post_id]
    write_data_to_json_file('storage.json', all_posts)
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """
    Handle updating an existing blog post.
    GET: Render the update form for the post.
    POST: Save the updated post and redirect to index.
    """
    post = fetch_post_by_id(post_id)

    if post is None:
        return "Post not found", 404

    if request.method == 'POST':

        updated_post = {
            'id': post_id,
            'title': request.form.get('title'),
            'author': request.form.get('author'),
            'content': request.form.get('content')
        }

        write_data_to_json_file_by_id('storage.json', updated_post)
        return redirect(url_for('index'))

    else:
     return render_template('update.html', post=post)





if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)