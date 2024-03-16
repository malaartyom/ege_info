import turtle as t  # Подключим модуль черепашка
import math
k = 25
t.left(90)
t.speed(10)
t.right(90)
for i in range(4):  # пропишем алгоритм построения фигуры по условию
    t.forward(4 * math.sqrt(5) * k)
    t.right(150)
    t.forward(4 * math.sqrt(5) * k)
    t.right(300)
t.up()
t.speed(10)  # Увеличим скорость черепашки
for x in range(10, -20, - 1):  # Алгоритм построения точек
    for y in range(10, -15, - 1):
        t.goto(x * k, y * k)
        t.dot(10)  # точки размером 4 пикселя
t.done()