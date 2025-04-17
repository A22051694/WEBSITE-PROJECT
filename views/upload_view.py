from flask import Blueprint, render_template, request, redirect, url_for
import cloudinary.uploader
from config.settings import UPLOAD_FOLDER, UPLOAD_PRESET
from models.image_model import Image

upload_view = Blueprint('upload', __name__)

@upload_view.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            # Upload to Cloudinary
            response = cloudinary.uploader.upload(file, 
                                                  upload_preset=UPLOAD_PRESET, 
                                                  folder='nebulafeed')
            # Save the image metadata
            image = Image(name=file.filename, 
                          url=response['secure_url'], 
                          public_id=response['public_id'])
            # You can store image metadata in a database, for now, we'll just pass it
            return render_template('upload.html', image=image)

    return render_template('upload.html', image=None)
