import turtle as t  
k = 30
t.left(90)
t.speed(10)
for i in range(5): 
    t.forward(9 * k)
    t.right(90)
    t.forward(3 * k)
    t.right(90)
t.up()
t.speed(10)
for x in range(10, -5, - 1): 
    for y in range(10, -10, - 1):
        t.goto(x * k, y * k)
        t.dot(3)  
t.done()