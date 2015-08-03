###############################################
# Name: Sapna Patil
# Class: CMPS 5363 Cryptography
# Date: 3 August 2015
# Program 2 - Elliptical Curve Encryption
###############################################

#---------------------Directories-------------------------------------------------------------------
#It imports directories those are required in function
import argparse
import sys
from fractions import Fraction
import EllipticalCurve as ep

#-------------Main Function-------------------------------------------------------------------------
#starting point of program is an main function
def main():
    #The argparse module makes it easy to write user-friendly command-line interfaces
    parser = argparse.ArgumentParser()
    #Filling an ArgumentParser with information about program arguments is done by making calls to the add_argument() method.
    parser.add_argument("-a", dest="a", help="Part 'a' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-b", dest="b", help="Part 'b' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-x1",dest="x1", help="")
    parser.add_argument("-y1",dest="y1", help="")
    parser.add_argument("-x2",dest="x2", help="")
    parser.add_argument("-y2",dest="y2", help="")
    #calling parse_args() will return an object
    args = parser.parse_args()
    #-----------------------------------------------------------------------------------------------
   
    print("a=",args.a," b=",args.b,"x1=",args.x1," y1=",args.y1," x2=",args.x2," y2=",args.y2)
    a=int(args.a)
    b=int(args.b)
    #convert the values  of x1,x2,y1,y2 into int  
    x1=args.x1
    x1=Fraction(x1)
    y1=args.y1
    y1=Fraction(y1)
    x2=args.x2
    x2=Fraction(x2)
    y2=args.y2
    y2=Fraction(y2)
    #check whether these point satisfy the equation or not 
    valueofpoint1= str(pow(y1,2) - pow(x1,3) -(a*x1) - b)
    valueofpoint2= str(pow(y2,2) - pow(x2,3) -(a*x2) - b)
    print('valueofpoint1',valueofpoint1)
    print('valueofpoint2',valueofpoint2)
    
    #-----------------------------------------------------------------------------------------------
    #to check whether values of x1,x2,y1,y2 are on the curve or not ?
    if(valueofpoint1 == '0' and valueofpoint2== '0'):
        print('these points satisfy the equation and as well as on the curve')
        a,b=ep.curveValue(a,b)
        #to get the value of slpoe
        m=ep.gettheslope(x1,y1,x2,y2)
        #get the value of x3
        x3=ep.getvalueofx3(x1,x2,m)
        #get the value of y3
        y3=ep.getvalueofy3(x3,x1,y1,m)
        #get the all values to plot on graph
        ep.valuesofallpointsplotedongraph(x1,y1,x2,y2,x3,y3,m,a,b)
    else:
        print('these point does not satisfies the equation and those are not on the curve.')
        sys.exit()
      #-----------------------------------------------------------------------------------------------
    

if __name__ == '__main__':
    main()
