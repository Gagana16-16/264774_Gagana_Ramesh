from django.urls import path
from . import views

urlpatterns = [
    path('form',views.employee_form,name='form'),
    path('result',views.result,name='result'),
    path('jumble',views.jumbled_word,name='jumble'),

]