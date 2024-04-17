from flask import Flask, request, render_template
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline

application = Flask(__name__, template_folder="Templates")
app = application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict_datapoint():
    if request.method == "GET":
        return render_template("predict.html")
    else:
        # Extract data from the form and create a CustomData instance
        data = CustomData(
            Year=int(request.form.get('Year')),
            Present_Price=float(request.form.get('Present_price')),
            Kms_Driven=int(request.form.get("Kms_Driven")),
            Fuel_Type=request.form.get("Fuel_Type"),
            Seller_Type=request.form.get("Seller_Type"),
            Transmission=request.form.get("Transmission"),
            Owner=int(request.form.get("Owner"))
        )

        # Convert CustomData instance to a DataFrame
        new_data = data.get_data_as_dataframe()

        # Use the prediction pipeline to make predictions
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(new_data)

        # Extract the prediction result
        result = round(pred[0], 2)

        # Render the result template with the prediction
        return render_template("predict.html", final_result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

#http://127.0.0.1:5000/ in browser