from django.shortcuts import render

import numpy as n
from django import forms
import sympy as sym
from sympy import *




def index(request):
    return render(request,'index.html')
def root(request):
    return render(request,'root.html')
def quadratic(request):
      class quadform(forms.Form):
           x2=forms.IntegerField(label='Co-eff of  X^2 ')
           print(end='/n')
           x=forms.IntegerField(label='Co-eff of  X ')
           const=forms.IntegerField(label='Constant term')
      if request.method=='POST':
            form=quadform(request.POST)
            if form.is_valid():
                 x=form.cleaned_data['x2']
                 y=form.cleaned_data['x']
                 z=form.cleaned_data['const']
                 res=n.roots([x,y,z])
                 return render(request,'result2.html',{'res':res})
                 exit()

      return render(request,'quad.html',{'form':quadform()})
def cubic(request):
      class cubicform(forms.Form):
             x3=forms.IntegerField(label='Co-eff of X^3')
             x2=forms.IntegerField(label='Co-eff of X^2')
             x=forms.IntegerField(label='Co-eff of X')
             Const=forms.IntegerField(label='Constant term')
      if request.method=="POST":
            form=cubicform(request.POST)
            if form.is_valid():
                 a=form.cleaned_data['x3']
                 b=form.cleaned_data['x2']
                 c=form.cleaned_data['x']
                 d=form.cleaned_data['Const']
                 res=n.roots([a,b,c,d])
                 return render(request,'result3.html',{'res':res})
                 exit()
      return render(request,'cubic.html',{'form':cubicform()})
def difx(request):
    class difform(forms.Form):

        y1=forms.CharField(label='f(x)')


        x1=forms.CharField(label='Differentiate with respect to')


    if request.method=='POST':
        nform=difform(request.POST)
        if nform.is_valid():
            a=nform.cleaned_data['x1']
            b=nform.cleaned_data['y1']
            x,y,z=sym.symbols('x y z')
            if a=='x':
                c=x
            elif a=='y':
                c=y
            else:
                c=z





            resd=sym.diff(b,c)
            return render(request,'difresult.html',{'mmm':str(resd)})
    return render(request,'dif.html',{'form':difform()})


# Create your views here.
