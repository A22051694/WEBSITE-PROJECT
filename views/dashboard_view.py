from flask import Blueprint, render_template

dashboard_view = Blueprint('dashboard', __name__)

@dashboard_view.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
