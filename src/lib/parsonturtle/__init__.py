from turtle import Turtle

class ParsonTurtle(Turtle):
  def __init__(self):
    self._turtle = Turtle()
    self._commands = []

  def forward(self, dist, log=True):
    self._turtle.forward(dist)
    if log:
      self._commands.append("fwd" + str(dist))
  def fd(self, dist, log=True):
    return self.forward(dist, log=log)


  def backward(self, dist, log=True):
    self._turtle.backward(dist)
    if log:
      self._commands.append("bwd" + str(dist))
  def back(self, dist, log=True):
    return self.backward(dist, log=log)
  def bk(self, dist, log=True):
    return self.backward(dist, log=log)

  def left(self, angle, log=True):
    self._turtle.left(angle)
    if log:
      self._commands.append("lt" + str(angle))
  def lt(self, angle, log=True):
    return self.left(angle, log=log)

  def right(self, angle, log=True):
    self._turtle.right(angle)
    if log:
      self._commands.append("rt" + str(angle))
  def rt(self, angle, log=True):
    return self.right(angle, log=log)

  def goto(self, nx, ny, log=True):
    self._turtle.goto(nx, ny)
    if log:
      self._commands.append("gt" + str(nx) + "-" + str(ny))

  def setposition(self, nx, ny, log=True):
    self._turtle.setposition(nx, ny)
    if log:
      self._commands.append("setpos" + str(nx) + "-" + str(ny))
  def setpos(self, nx, ny, log=True):
    return self.setposition(nx, ny, log=log)

  def setx(self, nx, log=True):
    self._turtle.setx(nx)
    if log:
      self._commands.append("setx" + str(nx))

  def sety(self, ny, log=True):
    self._turtle.sety(ny)
    if log:
      self._commands.append("sety" + str(ny))

  def dot(self, size, color, log=True):
    self._turtle.dot(size, color)
    if log:
      self._commands.append("dot" + str(size) + "-" + str(color))

  def circle(self, radius, extent, log=True):
    self._turtle.circle(radius, extent)
    if log:
      self._commands.append("circle" + str(radius) + "-" + str(extent))

  def up(self, log=True):
    self._turtle.up()
    if log:
      self._commands.append("up")
  def penup(self, log=True):
    return self.up(log=log)
  def pu(self, log=True):
    return self.up(log=log)

  def down(self, log=True):
    self._turtle.down()
    if log:
      self._commands.append("down")
  def pendown(self, log=True):
    return self.down(log=log)
  def pd(self, log=True):
    return self.down(log=log)

  def speed(self, spd):
    self._turtle.speed(spd)

  def _logColorChange(self, command, color, green, blue):
    if blue is not None:
      self._commands.append("%s(%d, %d, %d)"%(command, color, green, blue))
    else:
      self._commands.append("%s(%s)"%(command, color))

  def pencolor(self, color, green=None, blue=None, log=True):
    if blue is not None:
      self._turtle.pencolor(color, green, blue)
    else:
      self._turtle.pencolor(color)
    if log:
      self._logColorChange("pcolor", color, green, blue)

  def color(self, color, green=None, blue=None, log=True):
    if blue is not None:
      self._turtle.color(color, green, blue)
    else:
      self._turtle.color(color)
    if log:
      self._logColorChange("color", color, green, blue)

  def fillcolor(self, color, green=None, blue=None, log=True):
    if blue is not None:
      self._turtle.fillcolor(color, green, blue)
    else:
      self._turtle.fillcolor(color)
    if log:
      self._logColorChange("fcolor", color, green, blue)

  def width(self, size, log=True):
    self._turtle.pensize(size)
    if log:
      self._commands.append("width%d"%size)
  def pensize(self, size, log=True):
    return self.width(size, log=log)

  def commands(self):
    return ':'.join(self._commands)
