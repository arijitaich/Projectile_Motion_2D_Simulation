# GlowScript 2.9 VPython
f1=gcurve()
ground=box(pos=vector(0,0,0), size=vector(10,0.2,1), color=color.green)
ball=sphere(pos=vector(0,0,0), radius=0.1, color=color.yellow)

g=vector(0,-9.8,0)
v0=100
theta= 45*pi/180
#cos(theta)
#sin(theta)

ball.m=10
ball.v=vector(v0*cos(theta),v0*sin(theta),0)


t=0
dt=0.01
gg=0
attach_trail(ball)

while ball.pos.y>=0:
  rate(100)
  F=ball.m*g
  print("")
  print("")
  ball.v=ball.v+(F/ball.m)*dt
  print("Velocity Required= ", ball.v," m/s")
  ball.pos=ball.pos+ball.v*dt/ball.m
  print("Capsule Position= ", ball.pos," mts")
  t=t+dt
  print("Capsule Height= ", ball.pos.y," mts")
  f1.plot(t,ball.pos.y)
  
gg= ball.pos/1000
print("")
print("Time of flight = ",t," s")
print("The Final Position = ", ball.pos," mts")
print("The Final Position = ", gg," Kms")
