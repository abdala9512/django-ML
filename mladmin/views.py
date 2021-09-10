from django.http import HttpResponse

def mlmodels(request, model_type):
    if model_type == 'regression':
        return HttpResponse("modelos ML: Regression")


