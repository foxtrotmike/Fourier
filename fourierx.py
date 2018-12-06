"""
Understanding spectrum of a function using Fourier 
Shows how Fourier transform can be viewed as a correlation with sin and cos of 
various frequencies
and how it can be done using a matrix multiplication
"""

import numpy as np
from numpy import sin,cos
import matplotlib.pyplot as plt
#let's generate a signal composed of various cosines and sines
t = np.linspace(0,10,1000)
pi = np.pi
x = np.zeros(len(t))
for f in np.arange(1,50,2):
    x += sin(f*t)/f
x -= np.mean(x)

plt.figure()
plt.plot(t,x)
plt.xlabel('time t')
plt.ylabel('x(t)')
plt.grid()
plt.title("Time Domain Signal")
# Let's take the Fourier Transform through correlations
F = np.linspace(0,50,100)
V = []
for f in F:
    #this is correlation of input with cosines and sines of different freqs
    v = np.dot(x,cos(f*t))+1j*(np.dot(x,sin(f*t))) 
    V.append(v)

plt.figure()
plt.plot(F,np.abs(V))
plt.xlabel('F')
plt.ylabel('|X(f)|')
plt.grid()
plt.title("spectrum generated using correlation approach")
#In the plot, you should be able to see the major frequency components in 
# accordance with their relative weights when the signal was constructed
#Built in spectrum generatpr
plt.figure()
plt.magnitude_spectrum(x,Fs=2*pi*1.0/(t[1]-t[0]))
plt.title("Built-in spectrum generator")


DFT = np.zeros((len(t),len(F)),dtype=np.complex_)
for i,f in enumerate(F):
    DFT[:,i]=np.exp(-1j*f*t)
V2 = np.dot(x,DFT)

plt.figure()
plt.plot(F,np.abs(V2))
plt.xlabel('F')
plt.ylabel('|X(f)|')
plt.grid()
plt.title("spectrum generated using DFT Matrix Multiplication")


    
