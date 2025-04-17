import os

# Cloudinary Configuration
CLOUDINARY_CLOUD_NAME = os.getenv('CLOUDINARY_CLOUD_NAME', 'your-cloud-name')
CLOUDINARY_API_KEY = os.getenv('CLOUDINARY_API_KEY', 'your-api-key')
CLOUDINARY_API_SECRET = os.getenv('CLOUDINARY_API_SECRET', 'your-api-secret')

# File upload settings
UPLOAD_FOLDER = 'uploads'
UPLOAD_PRESET = 'your-upload-preset'

# Secret key for session management (you can replace this with a more secure key)
SECRET_KEY = 'your-secret-key'

# Debug settings
DEBUG = True
