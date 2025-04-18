from django.shortcuts import render

# Create your views here.
def employee_form(request):
    return render(request, 'employees/form.html')

def result(request):
    if request.method == 'POST': 
        name = request.POST.get('ename', 'Unknown')
        age = request.POST.get('age', 'Unkown')
        gross_salary = request.POST.get('gross_salary', '0')
        tax = request.POST.get('tax', 0)
        tax1=float(gross_salary) *float(tax)/100
        bonus = request.POST.get('bonus', 0)
        bonus1=float(gross_salary) *float(bonus)/100

        context = {
            'name': name,
            'age' : age,
            'gross_salary' : gross_salary,
            'tax' : float(tax)/100,
            'bonus' : float(bonus)/100,
            'netsalary' : float(gross_salary) + bonus1 - tax1 
        }
        return render(request, 'employees/details.html', context)
    else:
        return render(request, 'employees/form.html')
    

import random
def jumbled_word(request):
    context={}
    if request.method == 'POST': 
        word = request.POST.get('word')
        jumble=list(word)
        random.shuffle(jumble)
        word1=''.join(jumble)
        context = {
            'word': word1
            }
    return render(request, 'employees/jumble_words.html', context)