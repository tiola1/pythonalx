import turtle

"""
napisz funkcję która narysuje dowolny wielokąt foremny 
"""

print(help(turtle))





def rysuj(n):
    for i in range(n):
        turtle.forward(1000/n)
        turtle.right (360/n)




turtle.done ()