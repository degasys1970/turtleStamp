import turtle
ablak = turtle.Screen()
ablak.bgcolor('lightgreen')
Tundi = turtle.Turtle()  
Tundi.shape( 'turtle')
Tundi.color('blue')

Tundi.penup()
size = 20
for i in range(30):
  Tundi.stamp()
  size = size + 3
  Tundi.forward(size)
  Tundi.right(24)


ablak.mainloop()