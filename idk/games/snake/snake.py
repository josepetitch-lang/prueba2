import turtle
import time
import random

ventana = turtle.Screen()
ventana.title("Snake Game")
ventana.bgcolor("black")
ventana.setup(width = 600, height = 600)
ventana.tracer(0)

cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("green")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direccion = "stop" 

comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

segmentos = []

def arriba():
    if cabeza.direccion != "down":
        cabeza.direccion = "up"

def abajo():
    if cabeza.direccion != "up": 
        cabeza.direccion = "down"

def izquierda():
    if cabeza.direccion != "right":
        cabeza.direccion = "left"

def derecha():
    if cabeza.direccion != "left":
        cabeza.direccion = "right"

def mover():
    if cabeza.direccion == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20) 

    if cabeza.direccion == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direccion == "left":
        x = cabeza.xcor() 
        cabeza.setx(x - 20)

    if cabeza.direccion == "right":
        x = cabeza.xcor() 
        cabeza.setx(x + 20) 
ventana.listen()
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(derecha, "Right")

while True:
    ventana.update()

    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direccion = "stop" 

        for segmento in segmentos:
            segmento.goto(1000, 1000)
        segmentos.clear()

    if cabeza.distance(comida) < 20:
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        comida.goto(x, y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("lightgreen")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento) 

    # Mover el cuerpo segun el bloque anterior
    for i in range(len(segmentos) - 1, 0, -1):
        x = segmentos[i-1].xcor()
        y = segmentos[i-1].ycor() # Corregido xcor -> ycor
        segmentos[i].goto(x, y)

    if len(segmentos) > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    mover()

    
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direccion = "stop" 

            for seg in segmentos:
                seg.goto(1000, 1000)
            segmentos.clear()

    time.sleep(0.08) 