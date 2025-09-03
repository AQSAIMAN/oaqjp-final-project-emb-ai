"""Flask server for emotion detection application."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """
    Render the index.html page.

    Returns:
        The rendered HTML template.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["POST"])
def analyze_emotion():
    """
    Handle emotion detection POST request.

    Returns:
        A string containing the emotion analysis result,
        or an error message if analysis fails.
    """
    text_to_analyze = request.form["textToAnalyze"]
    try:
        result = emotion_detector(text_to_analyze)
        if result["dominant_emotion"] is None:
            response_string = "Invalid text! Please try again!"
        else:
            response_string = (
                f"For the given statement, the system response is "
                f"'anger': {result['anger']}, "
                f"'disgust': {result['disgust']}, "
                f"'fear': {result['fear']}, "
                f"'joy': {result['joy']} and "
                f"'sadness': {result['sadness']}. "
                f"The dominant emotion is {result['dominant_emotion']}."
            )
    except (KeyError, TypeError, ValueError) as error:
        response_string = f"Error: {str(error)}"
    return response_string


if __name__ == "__main__":
    app.run(debug=True)
