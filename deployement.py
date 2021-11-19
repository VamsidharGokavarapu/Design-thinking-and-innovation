# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
# Load the Random Forest CLassifier model
filename = 'model.pkl'
classifier = pickle.load(open(filename, 'rb'))
classifier1 = pickle.load(open('model1.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index1.html');
@app.route('/predict2',methods=['POST'])
def predict2():
        return render_template('index.html')
@app.route('/predict3',methods=['POST'])
def predict3():
        return render_template('index2.html')
        

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        preg = request.form['pregnancies']
        glucose = request.form['glucose']
        bp = request.form['bloodpressure']
        st = request.form['skinthickness']
        insulin = request.form['insulin']
        bmi = request.form['bmi']
        dpf = request.form['dpf']
        age = request.form['age']
        
        data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
        my_prediction = classifier.predict(data)
        
        return render_template('result.html', prediction=my_prediction)

@app.route('/predict1', methods=['POST'])
def predict1():
    if request.method == 'POST':
        Age = request.form['Age']
        Gender = request.form['Gender']
        Polyuria= request.form['Polyuria']
        Polydipsia = request.form['Polydipsia']
        suddenweightloss = request.form['sudden weight loss']
        weakness = request.form['weakness']
        Polyphagia = request.form['Polyphagia']
        Genitalthrush = request.form['Genital thrush']
        visualblurring = request.form['visual blurring']
        Itching = request.form['Itching']
        Irritability = request.form['Irritability']
        delayedhealing = request.form['delayed healing']
        partialparesis = request.form['partial paresis']
        musclestiffness= request.form['muscle stiffness']
        Alopecia= request.form['Alopecia']
        Obesity= request.form['muscle stiffness']
        data = np.array([[Age, Gender,Polyuria,Polydipsia,suddenweightloss,weakness,Polyphagia, Genitalthrush,visualblurring,Itching,Irritability,delayedhealing,partialparesis, musclestiffness,Alopecia,Obesity]])
        my_prediction1 = classifier1.predict(data)
        
        return render_template('result.html', prediction=my_prediction1)


if __name__ == '__main__':
	app.run(debug=True)