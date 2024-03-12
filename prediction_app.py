from flask import Flask, render_template, request
import joblib
import numpy as np

prediction_app = Flask(__name__, template_folder= 'C:\\Users\\danie\\AI\\ML-K8-project\\template')

# Load the pre-trained machine learning model
model = joblib.load("model_joblib.pkl")

# Render the home page with a form to input data
@prediction_app.route("/")
def home( ):
    return render_template("index.html")

# Handle the form submission and make predictions
@prediction_app.route("/predict", methods=["POST"])
def predict():
    # Get the input data from the form
    features = [float(x) for x in request.form.values()]

    # Make predictions using the loaded model
    prediction = model.predict(np.array(features).reshape(1, -1))

    return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
    prediction_app.run(debug=True)


