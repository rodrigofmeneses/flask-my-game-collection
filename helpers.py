import os
from mgc import app


def image_recovery(id):
    for filename in os.listdir(app.config['UPLOAD_PATH']):
        if f'cover_{id}' in filename:
            return filename
    return 'default_cover.jpg'

def delete_file(id):
    filename = image_recovery(id)
    if filename != 'default_cover.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], filename))
