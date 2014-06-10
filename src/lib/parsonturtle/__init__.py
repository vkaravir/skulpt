from turtle import Turtle

class ParsonTurtle(Turtle):
  def __init__(self):
    self._turtle = Turtle()
    print self._turtle
    self._commands = []

  def forward(self, dist):
    self._turtle.forward(dist)
    self._commands.append("fwd" + str(dist))
    print self._commands
  def fd(self, dist):
    return self.forward(dist)


  def backward(self, dist):
    self._turtle.backward(dist)
    self._commands.append("bwd" + str(dist))
    print self._commands
  def back(self, dist):
    return self.backward(dist)
  def bk(self, dist):
    return self.backward(dist)

  def left(self, angle):
    self._turtle.left(angle)
    self._commands.append("lt" + str(angle))
  def lt(self, angle):
    return self.left(angle)

  def right(self, angle):
    self._turtle.right(angle)
    self._commands.append("rt" + str(angle))
  def rt(self, angle):
    return self.right(angle)

  def goto(self, nx, ny):
    self._turtle.goto(nx, ny)
    self._commands.append("gt" + str(nx) + "-" + str(ny))

  def setposition(self, nx, ny):
    self._turtle.setposition(nx, ny)
    self._commands.append("setpos" + str(nx) + "-" + str(ny))
  def setpos(self, nx, ny):
    return self.setposition(nx, ny)

  def setx(self, nx):
    self._turtle.setx(nx)
    self._commands.append("setx" + str(nx))

  def sety(self, ny):
    self._turtle.sety(ny)
    self._commands.append("sety" + str(ny))

  def dot(self, size, color):
    self._turtle.dot(size, color)
    self._commands.append("dot" + str(size) + "-" + str(color))

  def circle(self, radius, extent):
    self._turtle.circle(radius, extent)
    self._commands.append("circle" + str(radius) + "-" + str(extent))

  def up(self):
    self._turtle.up()
    self._commands.append("up")
  def penup(self):
    return self.up()
  def pu(self):
    return self.up()

  def down(self):
    self._turtle.down()
    self._commands.append("down")
  def pendown(self):
    return self.down()
  def pd(self):
    return self.down()

  def speed(self, spd):
    self._turtle.speed(spd)

  def pencolor(self, color, green, blue):
    self._turtle.pencolor(color, green, blue)

  def color(self, color, green, blue):
    self._turtle.color(color, green, blue)

  def fillcolor(self, color, green, blue):
    self._turtle.fillcolor(color, green, blue)

  def width(self, size):
    self._turtle.pensize(size)
  def pensize(self, size):
    return self.width(size)

  def commands(self):
    return ':'.join(self._commands)
