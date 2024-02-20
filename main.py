import math
import numpy

#shooting_theta = math.pi/3 # radians
shooting_velo = 20 # random number

a_y = -9.8 # gravity
v_y = 0
p_y = -7 # vertical distance from target
a_x = 0 # pretend this doesn't exist because i don't feel like doing air resistance
v_x = 0
p_x = -30 # horizontal distance from target

t4 = (a_x**2 + a_y**2)/4
t3 = (a_x*v_x + a_y*v_y)
t2 = (v_x**2 + p_x*a_x + v_y**2 + p_y*a_y - shooting_velo**2)
t1 = 2*(p_x*v_x + p_y*v_y)
t0 = (p_x**2 + p_y**2)

roots = list(numpy.roots([t4, t3, t2, t1, t0]))
print(roots)
num_roots = 0
t = -1
for i in reversed(sorted(roots)):
    # if the number is a positive real number
    if not (type(i) == numpy.float64 and i > 0):
        roots.remove(i)
print(roots)
if len(roots) == 0:
    print("no solutions")
    exit()
t = min(roots) # not max because we want a low shooting angle

print(t)
p_aimX = -(p_x + v_x*t + (a_x*(t**2))/2)
p_aimY = -(p_y + v_y*t + (a_y*(t**2))/2)
print(p_aimX)
print(p_aimY)
shooting_theta = math.atan(p_aimY/p_aimX)

with open("desmos stuffs.txt", "w") as desmos:
    desmos.write(f"({p_aimX}, {p_aimY})\n")
    desmos.write(f"({-p_x}, {-p_y})\n")
    #desmos.write("f\left(x\\right)=\\tan\left(" + str(shooting_theta) + "\\right)x-\\frac{" + str(a_y) + "x^{2}}{2\left(" + str(shooting_velo) + "\cos\left(" + str(shooting_theta) + "\\right)\\right)^{2}}\n")
    #desmos.write("f\left(x\\right)=\\tan\left(" + str(shooting_theta) + "\\right)x-\\frac{" + str(-a_y) + "x^{2}}{2\left(" + str(shooting_velo) + "\cos\left(" + str(shooting_theta) + "\\right)\\right)^{2}}\n")
    #desmos.write("f\left(x\\right)=" + str(p_aimY/p_aimX) + "x-\\frac{" + str(a_y) + "x^{2}}{2\left(" + str(shooting_velo) + "\cos\left(" + str(shooting_theta) + "\\right)\\right)^{2}}\n")
    desmos.write("f\left(x\\right)=" + str(p_aimY/p_aimX) + "x-\\frac{" + str(-a_y) + "x^{2}}{2\cdot\left(" + str(shooting_velo) + "\\right)^{2}\cdot\cos^{2}\left(" + str(shooting_theta) + "\\right)}")

