# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Point:                                                               #Clase
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self,initX,initY):                                                    #Instanciamos

        self.x = initX                                                        #x será 0
        self.y = initY                                                         #y será 0

p = Point(1,2)         # Instantiate an object of type Point
q = Point(3,4)         # and make a second point

print(p)
print(q)

lista=[1,2,3]
for i in lista:
    globals()['paying_round'+str(i)] = [i]

print((paying_round1, paying_round2, paying_round3))
    

Dict = {}
for i in range(0,3):
    Dict['x{0}'.format(i)] = [1,2,3]

print (Dict)
# {'x2': [1, 2, 3], 'x0': [1, 2, 3], 'x1': [1, 2, 3]}
print (Dict['x1'])
# [1,2,3]
print([i for i in Dict.values()])
