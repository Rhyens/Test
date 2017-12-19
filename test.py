import turtle, math
strana = 1
for cislo in range(20000):
    turtle.forward(strana)
    strana = strana + cislo / 1000
    turtle.left(360/300)

turtle.exitonclick()
