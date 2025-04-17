from flask import Flask, render_template
from views.home_view import home_view
from views.dashboard_view import dashboard_view
from views.upload_view import upload_view
from views.profile_view import profile_view

app = Flask(__name__)

# Register blueprints for routing
app.register_blueprint(home_view)
app.register_blueprint(dashboard_view)
app.register_blueprint(upload_view)
app.register_blueprint(profile_view)

if __name__ == '__main__':
    app.run(debug=True)
