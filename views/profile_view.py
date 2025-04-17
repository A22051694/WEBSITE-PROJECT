from flask import Blueprint, render_template

profile_view = Blueprint('profile', __name__)

@profile_view.route('/profile')
def profile():
    # You can fetch user details from a database, for now, it's static
    user = {"username": "JohnDoe", "profile_pic": "/static/images/default-avatar.png"}
    return render_template('profile.html', user=user)
