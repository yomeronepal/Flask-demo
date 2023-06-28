from flask import jsonify
from settings import app


class CustomException(Exception):
    def __init__(self, message):
        self.message = message


# Error handler for the custom exception
@app.errorhandler(CustomException)
def handle_custom_exception(error):
    response = jsonify({"error": error.message})
    response.status_code = 500  # You can set an appropriate status code
    return response
