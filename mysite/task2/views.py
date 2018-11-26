import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import SubplotZero
from django.http import HttpResponse
import io
from django.shortcuts import render
from django import forms
from sympy import diff, symbols

class UserForm(forms.Form):
    CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6),)
    formA = forms.ChoiceField(choices=CHOICES)
def forms(request):
    userform = UserForm()
    return render(request, 'task2/forms.html', {"form": userform})
def postS(postSave):
    global a
    global b
    global c
    global d
    global e
    global I
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    I = 0
    if postSave == 1:
        I = 11
        a = 0.2
        b = 97
        c = 88
        d = 350
        e = 112
    if postSave == 2:
        I = 15
        a = 2.3
        b = 150
        c = 120
        d = 457
        e = 97
    if postSave == 3:
        I = 22
        a = 112
        b = 215
        c = 110
        d = 465
        e = 149
    if postSave == 4:
        I = 25
        a = 32
        b = 67
        c = 275
        d = 84
        e = 52
    if postSave == 5:
        I = 32
        a = 39
        b = 140
        c = 97
        d = 192
        e = 76
    if postSave == 6:
        I = 47
        a = 15
        b = 22
        c = 217
        d = 118
        e = 56
def func(u):
    f = (a*u+b*u**2+c*u**3+d*u**4+e*u**5)-I
    return f
def funcg(u):
    f = (a*u+b*u**2+c*u**3+d*u**4+e*u**5)-I
    return f

def mplimage(request):
    if 1:
        postSave = float(request.POST['formA'])
        postS(postSave)
        l = 0
        lmax = 0.6
        E = 1e-4
        y=0.0
        iu=0
        f = plt.figure(1)
        ax = SubplotZero(f, 111)
        f.add_subplot(ax)
        mas = np.arange(l, lmax, E)
        for i in mas:
            y1=func(i)
            y2=func(i+E)
            if y1*y2<0:
                iu = (i+i+E)/2
                break

        for direction in ["xzero", "yzero"]:
            # adds arrows at the ends of each axis
            ax.axis[direction].set_axisline_style("-|>")

            # adds X and Y-axis from the origin
            ax.axis[direction].set_visible(True)

        for direction in ["left", "right", "bottom", "top"]:
            # hides borders
            ax.axis[direction].set_visible(False)
        x = np.linspace(l, lmax, 100)
        ax.plot(iu, funcg(iu), 'o', x, funcg(x))
        print(iu)
        print(y1)
        print(y2)
        print(I)
    buf = io.BytesIO()
    plt.grid(True)
    plt.savefig(buf, format='svg')
    plt.close(f)
    response = HttpResponse(buf.getvalue(), content_type='image/svg+xml')
    return response

def dyhotomia(request):
    if 1:
        postSave = float(request.POST['formA'])
        postS(postSave)
        l = 0.0
        lmax = 0.6
        E = 1e-4
        y=0.0
        f = plt.figure(1)
        ax = SubplotZero(f, 111)
        f.add_subplot(ax)
        x = l
        xmax = lmax
        Ua = 0.0
        U = 0.0
        while(np.abs(l - lmax)>=E):
            Ua = func(l)
            U = func((l+lmax)/2)
            if Ua*U > 0:
                l = (l+lmax)/2
            else:
                lmax = (l+lmax)/2
            y = (l+lmax)/2

        for direction in ["xzero", "yzero"]:
            # adds arrows at the ends of each axis
            ax.axis[direction].set_axisline_style("-|>")

            # adds X and Y-axis from the origin
            ax.axis[direction].set_visible(True)

        for direction in ["left", "right", "bottom", "top"]:
            # hides borders
            ax.axis[direction].set_visible(False)
        x = np.linspace(x, xmax, 100)
        ax.plot(y, funcg(y), 'o', x, funcg(x))
        print(y)
        print(Ua)
        print(U)
        print(I)
        print(a)

    buf = io.BytesIO()
    plt.grid(True)
    plt.savefig(buf, format='svg')
    plt.close(f)
    response = HttpResponse(buf.getvalue(), content_type='image/svg+xml')
    return response

def dFunc(u):
    du = symbols("u")
    return diff((a*du+b*du**2+c*du**3+d*du**4+e*du**5)-I).subs(du, u)
def d2Func(u):
    du = symbols("u")
    return diff((a*du+b*du**2+c*du**3+d*du**4+e*du**5)-I, du, 2 ).subs(du, u)

def newton(request):
    if 1:
        postSave = float(request.POST['formA'])
        postS(postSave)
        l = 0.0
        lmax = 0.6
        E = 1e-4
        f = plt.figure(1)
        ax = SubplotZero(f, 111)
        f.add_subplot(ax)
        x = l
        xmax = lmax
        if(func(l)*d2Func(l) > 0):
            x0 = l
        else: x0 = lmax
        xn = x0 - func(x0) / dFunc(x0)
        while(np.abs(x0 - xn) > E):
            x0 = xn
            xn = x0 - func(x0) / dFunc(x0)

        for direction in ["xzero", "yzero"]:
            # adds arrows at the ends of each axis
            ax.axis[direction].set_axisline_style("-|>")

            # adds X and Y-axis from the origin
            ax.axis[direction].set_visible(True)

        for direction in ["left", "right", "bottom", "top"]:
            # hides borders
            ax.axis[direction].set_visible(False)
        x = np.linspace(x, xmax, 100)
        ax.plot(xn, funcg(xn), 'o', x, funcg(x))
        print("newton",xn)

    buf = io.BytesIO()
    plt.grid(True)
    plt.savefig(buf, format='svg')
    plt.close(f)
    response = HttpResponse(buf.getvalue(), content_type='image/svg+xml')
    return response