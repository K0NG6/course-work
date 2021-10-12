from django.shortcuts import render
import numpy as np
from numpy import *
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import SubplotZero
from django.http import HttpResponse
import io
from django.shortcuts import render
from django import forms
from sympy import diff, symbols
import random as random_number
class UserForm(forms.Form):
    a = forms.FloatField(label="Введіть a:", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    b = forms.FloatField(label="Введіть b:", widget=forms.NumberInput(attrs={'class': 'form-control'}))
def forms(request):
    userform = UserForm()
    return render(request, 'task3/forms.html', {"form": userform})
def func(x):
	return 1 + np.sin(x)
def rectangle(a,b,n):
    if 1:
        f = plt.figure(1)
        ax = SubplotZero(f, 111)
        f.add_subplot(ax)
        dx = (b-a)/float(n)
        total = 0
        for k in range(0, n):
            total = total + func((a + (k * dx)))
        return dx*total
    #     for direction in ["xzero", "yzero"]:
    #         # adds arrows at the ends of each axis
    #         ax.axis[direction].set_axisline_style("-|>")
    #
    #         # adds X and Y-axis from the origin
    #         ax.axis[direction].set_visible(True)
    #
    #     for direction in ["left", "right", "bottom", "top"]:
    #         # hides borders
    #         ax.axis[direction].set_visible(False)
    #     x = np.linspace(a, b, 100)
    #     ax.bar(mas,func(mas), align='edge', width = 0.98)
    #     ax.plot(x, func(x), '#CE302D')
    #     print(dx*total)
    #     print(mas)
    # buf = io.BytesIO()
    # plt.savefig(buf, format='svg')
    # plt.close(f)
    # response = HttpResponse(buf.getvalue(), content_type='image/svg+xml')
    # return response
def trap(a,b,n):
    dx = (b - a) / float(n)
    total = 0
    for k in range(0, n):
        total = total + (func((a + (k * dx)))+func((a + (k * dx))+dx))/2
    return dx * total
def MCint(a, b, n):
    x = random.uniform(a, b, n)
    s = sum(func(x))
    I = (float(b-a)/n)*s
    return I
def Simpson(a, b, n):
    dx = (b - a)/n
    S = 0
    x = a + dx
    while(x < b):
        S = S + 4 * func(x)
        x = x + dx
        S = S + 2 * func(x)
        x = x + dx
    S = dx / 3 * (S + func(a) - func(b))
    return S
def index(request):
    userform = UserForm()
    mas = [10,20,50,100,1000]
    a = float(request.POST['a'])
    b = float(request.POST['b'])
    S = []
    trapS = []
    MCintS = []
    SimpsonS = []
    for k in mas:
        S.append(rectangle(a,b,k))
        trapS.append(trap(a,b,k))
        MCintS.append(MCint(a, b, k))
        SimpsonS.append(Simpson(a, b, k))

    print(S)
    return render(request, 'task3/index.html', {"SimpsonS": SimpsonS,"MCintS": MCintS,"trap": trapS,"S": S,"form": userform})
