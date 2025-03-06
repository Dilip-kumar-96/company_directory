from flask import Flask
from src.company_directory.route import main  # Import the registered Blueprint

app = Flask(__name__)

# Register Blueprint (No Blueprint Logic Here)
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
