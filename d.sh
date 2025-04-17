#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
export FLASK_APP=app.py
export FLASK_ENV=development
export CLOUDINARY_CLOUD_NAME=your-cloud-name
export CLOUDINARY_API_KEY=your-api-key
export CLOUDINARY_API_SECRET=your-api-secret
export SECRET_KEY=your-secret-key

# Run the Flask application
flask run
