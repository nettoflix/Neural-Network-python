
from Perceptron import *
from tkinter import *

def doTrain(event):
     for i in range(len(points)):
        inputs = [points[i].x, points[i].y]
        target = points[i].label
        percept.train(inputs, target)
        draw()
        #print("Weight X: ", percept.weights[0])
        #print("Weight Y: ", percept.weights[1])
def draw():
    w.delete("all")
    p1 = Point(canvas_width,canvas_height,-1,f(-1),False)
    p2 = Point(canvas_width,canvas_height,1,f(1),False)
    w.create_line(p1.getX(), p1.getY(), p2.getX(), p2.getY())
    #perceptron draw the line he thinks is the right one
    p3 = Point(canvas_width,canvas_height, -1, percept.guessY(-1), False)
    p4 = Point(canvas_width,canvas_height, 1, percept.guessY(1), False)
    w.create_line(p3.getX(),p3.getY(), p4.getX(),p4.getY(), fill='purple')
    for i in range(len(points)):
        inputs = [points[i].x, points[i].y]
        target = points[i].label
        #
        result = percept.feedforward(inputs)

        if result == target:
            if result == 1:
                w.create_oval(points[i].getX()-5, points[i].getY()-5, points[i].getX()+5, points[i].getY()+5, fill=python_green)
            else:
                w.create_oval(points[i].getX()-5, points[i].getY()-5, points[i].getX()+5, points[i].getY()+5, fill=python_red)

        else:
            if target == 1:
                w.create_oval(points[i].getX()-5, points[i].getY()-5, points[i].getX()+5, points[i].getY()+5, fill=python_black)
            else:
                #print("brown result: ", result)
                #print("brown target: ", target)
                w.create_oval(points[i].getX()-5, points[i].getY()-5, points[i].getX()+5, points[i].getY()+5, fill=python_brown)

canvas_width = 400
canvas_height = 400

percept = Perceptron(2,0000.1)


master = Tk()
master.title("Points")
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack(expand=YES, fill=BOTH)
message = Label(master, text="draw")
message.pack(side=BOTTOM)
python_green = "#00FF00"
python_red = "#FF0000"
python_black = "#000000"
python_brown = "#964B00"
#w.create_oval(50, 50, 70, 70, fill=python_green)
points = []
for i in range(100):
    points.append(Point(canvas_width, canvas_height,0,0))
draw()
w.bind('<Button-1>', doTrain)
mainloop()
