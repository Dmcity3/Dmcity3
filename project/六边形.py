import turtle as t
t.setup()
t.bgcolor("black")
t.speed(100)
sides=6
colors=["red","yellow","lime","deepskyblue","orange","mediumorchid"]
for i in range(230):
    t.pencolor(colors[i%sides])
    t.fd(i*3/sides+i)
    t.left(360/sides+1)
    t.width(i*sides/200)
t.done
