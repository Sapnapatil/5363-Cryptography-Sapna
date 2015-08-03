###############################################
# Name: Sapna Patil
# Class: CMPS 5363 Cryptography
# Date: 3 August 2015
# Program 2 - Elliptical Curve Encryption
###############################################
#---------------------Directories-------------------------------------------------------------------
#It imports directories those are required in function
import numpy as np
import matplotlib.pyplot as plt
#--------------------------------------------------------------------------------------------------
#get the values of a and b
def curveValue(vala,valb):
    a=0 
    b=0
    a = vala
    b = valb
    return a,b

#--------------------------------------------------------------------------------------------------
#calculate value of slope
def gettheslope(x1,y1,x2,y2):
    m=0
    #to check whether x1 and x2 are same and y1 n y2 are same 
    if( x1==x2 and y1==y2 ):
        m = ((3*pow(x1,2))+a)/(2*y1)
    else:
        m = (y1-y2)/(x1-x2)
    print('value of m',m)
    #Get the slope of the line
    return m

#--------------------------------------------------------------------------------------------------    
#calculate value of x3 
def getvalueofx3(x1,x2,m):
    x3= pow(m,2)-x1-x2
    print('value of x3',x3)
    return x3
    
#--------------------------------------------------------------------------------------------------    
#calculate value of y3
def getvalueofy3(x3,x1,y1,m):
    y3= m*(x3-x1) +y1
    print('value of y3',y3)
    return y3
    
#--------------------------------------------------------------------------------------------------    
def valuesofallpointsplotedongraph(x1,y1,x2,y2,x3,y3,m,a,b):
    #Determines width and height of plot
    maxvalue = max(abs(x1),abs(y1),abs(x2),abs(y2),abs(x3),abs(y3))
	#width and height of plot
    w = maxvalue +8
    h = maxvalue +8
    # Annotate the plot with your name using width (w) and height (h) as your reference points.
    an1 = plt.annotate("Sapna Patil", xy=(-w+2 , h-2), xycoords="data",
    va="center", ha="center",
    bbox=dict(boxstyle="round", fc="w"))
    # This creates a mesh grid with values determined by width and height (w,h)
    # of the plot with increments of .0001 (1000j = .0001 or 5j = .05)
    y, x = np.ogrid[-h:h:1000j, -w:w:1000j]

    # Plot the curve (using matplotlib's countour function)
    # This drawing function applies a "function" described in the
    # 3rd parameter:  pow(y, 2) - ( pow(x, 3) - x + 1 ) to all the
    # values in x and y.
    # The .ravel method turns the x and y grids into single dimensional arrays
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - ( pow(x, 3) + a*x + b ), [0])
    # Plot the points ('ro' = red, 'bo' = blue, 'yo'=yellow and so on)
    plt.plot(x1, y1,'ro')
# Annotate point 1
    plt.annotate('x1,y1', xy=(x1, y1), xytext=(x1+1,y1+1),
    arrowprops=dict(arrowstyle="->",
    connectionstyle="arc3"),)
    plt.plot(x2, y2,'ro')
    # Annotate point 2
    plt.annotate('x2,y2', xy=(x2, y2), xytext=(x2+1,y2+1),
    arrowprops=dict(arrowstyle="->",
    connectionstyle="arc3"),)
    #plotting line passing through points
    plt.contour(x.ravel(), y.ravel(), (y-y1)-m*(x-x1), [0],colors=('pink'))
    # the third point
    plt.plot(x3,y3,'ro')
    # Annotate point 3
    plt.annotate('x3,y3', xy=(x3, y3), xytext=(x3+1,y3+1),
    arrowprops=dict(arrowstyle="->",
    connectionstyle="arc3"),)
    # Show a grid background on our plot
    plt.grid()
    # Show the plot
    plt.show()
#--------------------------------------------------------------------------------------------------