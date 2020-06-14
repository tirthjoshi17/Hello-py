import turtle
turtle.bgcolor("black")
turtle.pensize(4)
turtle.speed(0)
b=["white","green","orange"]
for i in range(12):
	for a in b:
		turtle.color(a)
		turtle.circle(100)
		turtle.left(10)
turtle.mainloop()
