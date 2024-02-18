from scipy.optimize import fsolve
import math

shooting_theta = math.pi/3 # radians
shooting_velo = 20 # random number

a_y = -9.8 # gravity
v_y = math.sin(shooting_theta) * shooting_velo
p_y = 1 # vertical distance from speaker
a_x = 0 # pretend this doesn't exist because i don't feel like doing air resistance
v_x = math.cos(shooting_theta) * shooting_velo 
p_x = 1 # horizontal distance from speaker

t4 = (a_x**2 + a_y**2)/4
t3 = (a_x*v_x + a_y*v_y)
t2 = (v_x**2 + p_x*a_x + v_y**2 + p_y*a_y)
t1 = 2*(p_x*v_x + p_y*v_y)
t0 = (p_x**2 + p_y**2)

f = lambda t: t4*t**4 + t3*t**3 + t2*t**2 + t1*t + t0
roots = fsolve(f, [5])
print(roots)