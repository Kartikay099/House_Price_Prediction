# Install flask, pandas,pickle-mixin,scikit-learn
from sys import breakpointhook
import pandas as pd
import pickle 
from flask import Flask,render_template,request

x=r"C:\Users\ajay\Desktop\HousePricePrediction\Data_Set\project\templates\Cleaned_data.csv"
y=r"C:\Users\ajay\Desktop\HousePricePrediction\Data_Set\project\templates\RidgeModel.pkl"
app=Flask(__name__)
data=pd.read_csv(x)
pipe=pickle.load(open(y,'rb'))



@app.route('/')
def index():

    locations=sorted(data['location'].unique())
    return render_template('indexx.html',locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    location=request.form.get('location')
    bhk=request.form.get('bhk')
    bath =request.form.get('bath')
    sqft=request.form.get('total_sqft')
    print(location,bhk,bath,sqft)
    input=pd.DataFrame([[location,sqft,bath,bhk]],columns=['location','total_sqft','bath','BHK'])
    prediction=pipe.predict(input)[0]*100000
    return str(prediction)


if __name__=="__main__":
    app.run(debug=True)
     

