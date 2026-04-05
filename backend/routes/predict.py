from flask import Blueprint, request, jsonify
from services.model_service import predict

predict_bp = Blueprint("predict", __name__)

@predict_bp.route("/predict", methods=["POST"])
def predict_route():
    try:
        data = request.json["features"]
        result = predict(data)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)})