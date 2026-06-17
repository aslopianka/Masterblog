import json


def load_data_from_json_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def write_data_to_json_file(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)  # indend=2 so json gets not saved in single line


def fetch_post_by_id(post_id):
    all_posts = load_data_from_json_file('storage.json')
    # next is more efficient than filter -> returns after first match + returns None if no match
    return next((post for post in all_posts if post['id'] == post_id), None)


def write_data_to_json_file_by_id(filename, updated_post):
    all_posts = load_data_from_json_file('storage.json')

    for i, post in enumerate(all_posts):
        if post['id'] == updated_post['id']:

            all_posts[i] = updated_post
            break

    with open(filename, 'w') as f:
        json.dump(all_posts, f, indent=2)