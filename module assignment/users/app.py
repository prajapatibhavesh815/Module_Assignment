from flask import Flask

app = Flask(__name__)

# Register Blueprints
from user import user_bp
app.register_blueprint(user_bp, url_prefix='/user')

@app.route('/')
def home():
    return "Home Page"

if __name__ == '__main__':
    app.run()
