import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import SubplotZero
from django.http import HttpResponse
import io
from django.shortcuts import render
from django import forms


class UserForm(forms.Form):
    a = forms.FloatField(label="Введіть a:", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    b = forms.FloatField(label="Введіть b:", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    e = forms.FloatField(label="Введіть крок:", widget=forms.NumberInput(attrs={'class': 'form-control'}))

def forms(request):
    userform = UserForm()
    return render(request, 'labOne/forms.html', {"form": userform})
def func(x):
    return np.power(x, 4) + 2 * np.power(x, 3) - x - 1

def mplimage(request):
    if 1:
        a = float(request.POST['a'])
        b = float(request.POST['b'])
        e = float(request.POST['e'])
        y=0.0
        i=a
        f = plt.figure(1)
        ax = SubplotZero(f, 111)
        f.add_subplot(ax)
        mas = np.arange(a, b, e)

        for i in mas:
            y1=func(i)
            y2=func(i+e)
            if y1*y2<0:
                y = (i + i+e)/2

        for direction in ["xzero", "yzero"]:
            # adds arrows at the ends of each axis
            ax.axis[direction].set_axisline_style("-|>")

            # adds X and Y-axis from the origin
            ax.axis[direction].set_visible(True)

        for direction in ["left", "right", "bottom", "top"]:
            # hides borders
            ax.axis[direction].set_visible(False)
        x = np.linspace(a, b, 100)
        ax.plot(y, func(y), 'o', x, func(x))

    buf = io.BytesIO()
    plt.savefig(buf, format='svg')
    plt.close(f)
    response = HttpResponse(buf.getvalue(), content_type='image/svg+xml')
    return response
# Create your views here.