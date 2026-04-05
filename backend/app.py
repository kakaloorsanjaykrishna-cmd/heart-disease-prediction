from flask import Flask, jsonify
from flask_cors import CORS
from routes.predict import predict_bp

def create_app():
    app = Flask(__name__)
    
    # Enable CORS
    CORS(app)

    # Register Blueprints (Routes)
    app.register_blueprint(predict_bp)

    # Home Route
    @app.route("/")
    def home():
        return jsonify({
            "message": "❤️ Heart Disease Prediction API is running",
            "status": "success"
        })

    # Health Check Route
    @app.route("/health")
    def health():
        return jsonify({
            "status": "OK",
            "service": "Heart Disease Prediction API"
        })

    return app


# Run the app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)