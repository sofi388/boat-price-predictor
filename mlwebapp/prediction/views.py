# prediction/views.py
import numpy as np
from django.shortcuts import render, redirect
import joblib
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse


def predict_sample(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        arr = list(text.split(" "))
        res = [eval(i) for i in arr]
        predictor = joblib.load('predictor.pkl')
        predicted_value = predictor.predict([res])
        return render(request, 'prediction/result.html', {'predicted_value': predicted_value})
    return render(request, 'prediction/predict.html')


# [36, 720, 14, 2020, 4.00, 1.50, 8, 75]


def predict_price(request):
    return render(request, 'result.html')


def submit_form(request):
    if request.method == 'POST':
        # Process the form data here if needed
        text = request.POST.get('text')
        arr = list(text.split(" "))
        res = [eval(i) for i in arr]

        # requirement - scikit 1.3.2
        predictor = joblib.load('predictor.pkl')
        predicted_value = predictor.predict([res])
        # predicted_value = int((np.power(10, predicted_value) / 1000))
        upper = (np.power(10, (predicted_value + 0.05)) / 1000).round(1)
        lower = (np.power(10, (predicted_value - 0.05)) / 1000).round(1)

        result_pred = []
        result_pred.append(lower)
        result_pred.append(upper)

        # predicted_value = predictor.predict([[36, 720, 14, 2020, 4.00, 1.50, 8, 75]])

        # Redirect to the new page
        # return redirect(reverse('prediction:result'))  # Assuming 'new_page' is the name of the URL pattern for the new page

        # Pass the predicted value to the result page's context
        return render(request, 'result.html', {'predicted_value_upper': int(upper), 'predicted_value_lower': int(lower)})
    else:
        # Handle GET request (if needed)
        pass


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
