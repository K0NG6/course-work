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
def func(x):
	return 1 + np.sin(x)
def index(request):
    a = -5
    b = 5
    x = np.linspace(a, b, 50)
    y = []
    for k in x:
        y.append(func(k))


    def lagranz(x, y, t):
        z = 0
        for j in range(len(y)):
            p1 = 1;
            p2 = 1
            for i in range(len(x)):
                if i == j:
                    p1 = p1 * 1;
                    p2 = p2 * 1
                else:
                    p1 = p1 * (t - x[i])
                    p2 = p2 * (x[j] - x[i])
            z = z + y[j] * p1 / p2
        return z

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # Move left y-axis and bottim x-axis to centre, passing through (0,0)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')

    # Eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Show ticks in the left and lower axes only
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    xnew = np.linspace(np.min(x), np.max(x), 100)
    ynew = [lagranz(x, y, i) for i in xnew]
    ax.plot(x, y, 'o', xnew, ynew)
    buf = io.BytesIO()
    plt.grid(True)
    plt.savefig(buf, format='svg')
    plt.close()
    response = HttpResponse(buf.getvalue(), content_type='image/svg+xml')
    return response