# prediction/views.py
from django.shortcuts import render, redirect
import joblib
from django.http import HttpResponse, HttpResponseNotFound


def predict_sample(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        arr = list(text.split(" "))
        res = [eval(i) for i in arr]

        # train a model and save in file !
        predictor = joblib.load('predictor.pkl')
        predicted_value = predictor.predict([res])
        return render(request, 'prediction/result.html', {'predicted_value': predicted_value})
    return render(request, 'prediction/predict.html')


def index(request):
    return render(request, 'index.html')


def predict(request):
    return render(request, 'predict.html')


def info(request):
    return render(request, 'info.html')


def result(request):
    return render(request, 'result.html')


def handler404(request, exception):
    return HttpResponseNotFound("404: Page not Found! ")