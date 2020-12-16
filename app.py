# import libraries
from flask import Flask, request, render_template
import pickle
# create app and load the trained Model
app = Flask(__name__)
model = pickle.load(open('svc_trained_model.pkl', 'rb'))
# Route to handle HOME
@app.route('/')
def home():
    return render_template('index.html')
# Route to handle PREDICTED RESULT
@app.route('/predict',method=['POST'])
def predict():

    inputs = [] # declaring input array

    inputs.append(request.form['Pregnancies'])
    inputs.append(request.form['Glucose'])
    inputs.append(request.form['BloodPressure'])
    inputs.append(request.form['SkinThikness'])
    inputs.append(request.form['Insulin'])
    inputs.append(request.form['Age'])

    final_inputs = [np.array(inputs)]
    prediction = model.predict(final_inputs)

if(prediction[0] == 1):
    return render_template('index.html', predicted_result = "Diabetes")
if(prediction[0] == 0):
    return render_template('index.html', predicted_result = " NOT Diabetes")

if __name__ == "__main__":
    app.run(debug=True)
