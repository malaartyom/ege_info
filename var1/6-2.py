import turtle as t  # Подключим модуль черепашка
k = 30

t.speed(10)
for i in range(4):  # пропишем алгоритм построения фигуры по условию
    t.forward(8 * k)
    t.right(150)
    t.forward(8 * k)
    t.right(30)
t.up()
t.speed(10)  # Увеличим скорость черепашки
for x in range(10, -10, - 1):  # Алгоритм построения точек
    for y in range(10, -10, - 1):
        t.goto(x * k, y * k)
        t.dot(3)  # точки размером 4 пикселя
t.done()