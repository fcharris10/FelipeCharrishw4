#xii = xi - J**(-1)*f(x)

import math as m
import numpy as np
from numpy import linalg as LA

def function1( theta1 , theta2 , theta3 , L1 , L2 , L3 , L ):
	return L1*np.cos( theta1 ) + L2*np.cos( theta2 ) + L3*np.cos(theta3) - L


def function2( theta1 , theta2 , theta3 , L1 , L2 , L3 ):
	return L1*np.sin( theta1 ) + L2*np.sin( theta2 ) + L3*np.sin( theta3 )


def function3( theta1 ):
	return ( np.sin( theta1 ) )**2 + ( np.cos( theta1 ) )**2 - 1.0


def function4( theta2 ):
	return ( np.sin( theta2 ) )**2 + ( np.cos( theta2 ) )**2 - 1.0

def function5( theta3 ):
	return ( np.sin( theta3 ) )**2 + ( np.cos( theta3 ) )**2 - 1.0

def function6( theta1 , theta2 , W1 , T1 , T2 ):
	return T1*np.sin( theta1 ) - T2*np.sin( theta2 ) - W1

def function7( theta1 , theta2 , T1 , T2 ):
	return T1*np.cos( theta1 ) - T2*np.cos( theta2 )

def function8( theta2 , theta3 , T2 , T3 , W2 ):
	return T2*np.sin( theta2 ) + T3*np.sin( theta3 ) - W2

def function9( theta2 , theta3 , T2 , T3 ):
	return T2*np.cos( theta2 ) - T3*np.cos( theta3 )

def vector_fx( theta1 , theta2 , theta3 , L1 , L2 , L3 , L , W1 , W2 , T1 , T2 , T3):
	return [ function1( theta1 , theta2 , theta3 , L1 , L2 , L3 , L ) , function2( theta1 , theta2 , theta3 , L1 , L2 , L3 ) , function6( theta1 , theta2 , W1 , T1 , T2 ) , function7( theta1 , theta2 , T1 , T2 ) , function8( theta2 , theta3 , T2 , T3 , W2 ) , function9( theta2 , theta3 , T2 , T3 ) ]


def jacobian( theta1 , theta2 , theta3 , L1 , L2 , L3 , L , W1 , W2 , T1 , T2 , T3 ):
	A = np.zeros( (6,6) )
	h = 0.001
	c = 1/h
	A[0,0] = c*(function1( theta1 + h , theta2 , theta3 , L1 , L2 , L3 , L ) - function1( theta1 , theta2 , theta3 , L1 , L2 , L3 , L ) )
	A[0,1] = c*(function1( theta1 , theta2 + h , theta3 , L1 , L2 , L3 , L ) - function1( theta1 , theta2 , theta3 , L1 , L2 , L3 , L ) )
	A[0,2] = c*(function1( theta1 , theta2 , theta3 + h , L1 , L2 , L3 , L ) - function1( theta1 , theta2 , theta3 , L1 , L2 , L3 , L ) )
	A[1,0] = c*(function2( theta1 + h , theta2 , theta3 , L1 , L2 , L3 ) - function2( theta1 , theta2 , theta3 , L1 , L2 , L3 ))
	A[1,1] = c*(function2( theta1 , theta2 + h , theta3 , L1 , L2 , L3 ) - function2( theta1 , theta2 , theta3 , L1 , L2 , L3 ))
	A[1,2] = c*(function2( theta1 , theta2 , theta3 + h , L1 , L2 , L3 ) - function2( theta1 , theta2 , theta3 , L1 , L2 , L3 ))
	A[2,0] = c*(function6( theta1 + h , theta2 , W1 , T1 , T2 ) - function6( theta1 , theta2 , W1 , T1 , T2 ))
	A[2,1] = c*(function6( theta1 , theta2 + h , W1 , T1 , T2 ) - function6( theta1 , theta2 , W1 , T1 , T2 ))
	A[2,3] = c*(function6( theta1 , theta2 , W1 , T1 + h , T2 ) - function6( theta1 , theta2 , W1 , T1 , T2 ))
	A[2,4] = c*(function6( theta1 , theta2 , W1 , T1 , T2 + h ) - function6( theta1 , theta2 , W1 , T1 , T2 ))
	A[3,0] = c*(function7( theta1 + h , theta2 , T1 , T2 ) - function7( theta1 , theta2 , T1 , T2 ))
	A[3,1] = c*(function7( theta1 , theta2 + h , T1 , T2 ) - function7( theta1 , theta2 , T1 , T2 ))
	A[3,3] = c*(function7( theta1 , theta2 , T1 + h , T2 ) - function7( theta1 , theta2 , T1 , T2 ))
	A[3,4] = c*(function7( theta1 , theta2 , T1 , T2 + h ) - function7( theta1 , theta2 , T1 , T2 ))
	A[4,1] = c*(function8( theta2 + h , theta3 , T2 , T3 , W2 )-function8( theta2 , theta3 , T2 , T3 , W2 ))
	A[4,2] = c*(function8( theta2 , theta3 + h , T2 , T3 , W2 )-function8( theta2 , theta3 , T2 , T3 , W2 ))
	A[4,4] = c*(function8( theta2 , theta3 , T2 + h , T3 , W2 )-function8( theta2 , theta3 , T2 , T3 , W2 ))
	A[4,5] = c*(function8( theta2 , theta3 , T2 , T3 + h , W2 )-function8( theta2 , theta3 , T2 , T3 , W2 ))
	A[5,1] = c*(function9( theta2 + h , theta3 , T2 , T3 ) - function9( theta2 , theta3 , T2 , T3 ))
	A[5,2] = c*(function9( theta2 , theta3 + h , T2 , T3 ) - function9( theta2 , theta3 , T2 , T3 ))
	A[5,4] = c*(function9( theta2 , theta3 , T2 + h , T3 ) - function9( theta2 , theta3 , T2 , T3 ))
	A[5,5] = c*(function9( theta2 , theta3 , T2 , T3 + h ) - function9( theta2 , theta3 , T2 , T3 ))
	return A


pi = 3.141592

def newton( theta1 , theta2 , theta3 , L1 , L2 , L3 , L , W1 , W2 , T1 , T2 , T3 ):
	x = [ theta1 , theta2 , theta3 , T1 , T2 , T3 ]
	J = jacobian( x[0] , x[1] , x[2] , L1 , L2 , L3 , L , W1 , W2 , x[3] , x[4] , x[5] )
	fx = vector_fx( x[0] , x[1] , x[2] , L1 , L2 , L3 , L , W1 , W2 , x[3] , x[4] , x[5] )
	a = np.dot(J,fx)
	x = x - a

	while LA.norm( x ) > 10**(-3):
		fx = vector_fx( x[0] , x[1] , x[2] , L1 , L2 , L3 , L , W1 , W2 , x[3] , x[4] , x[5] )
		J = jacobian( x[0] , x[1] , x[2] , L1 , L2 , L3 , L , W1 , W2 , x[3] , x[4] , x[5] )
		a = np.dot(J,fx)
		x = x - a
	return x


A = jacobian( 1 , 1 , 1 , 3 , 4 , 4 , 8 , 10 , 20 , 1 , 1 , 1 )
print A
print LA.inv( A )
#print newton( pi/2 , pi/2 , pi/2 , 3 , 4 , 4 , 8 , 10 , 20 , 5 , 5 , 5 )



