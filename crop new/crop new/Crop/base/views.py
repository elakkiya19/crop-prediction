from django.shortcuts import render
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
global scaler
def home(request):
    return render(request, 'index.html')

def getPredictions(N,P,K,temp,humidity,ph,rain,soil_type):
    model = pickle.load(open('DecisionTree.pkl', 'rb'))
    prediction = model.predict(np.array([[N,P,K,temp,humidity,ph,rain,soil_type]]))
    return (prediction)

def result(request):
    N = int(request.GET['        N'])
    P = int(request.GET['        P'])
    K = int(request.GET['        K'])
    temp = int(request.GET['TEMPARATURE'])
    humidity = int(request.GET['HUMIDITY'])
    ph = int(request.GET['       PH'])
    rain = int(request.GET['     RAIN'])
    soil_type = int(request.GET['soil_type'])
    
    result = getPredictions(N,P,K,temp,humidity,ph,rain,soil_type)
    return render(request, 'result.html', {'result': result[0]})

