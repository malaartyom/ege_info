import turtle as t
t.left(90)
t.speed(10)
k = 30
for i in range(5):
    t.forward(9*k)
    t.right(120)
t.up()
t.speed(10)
for x in range(-10, -10, -1):
    for y in range(-10, -10, -1):
        t.goto(x*k, y*k)
        t.dot(3)
t.done()