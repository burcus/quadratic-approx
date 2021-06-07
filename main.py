import numpy as np
import itertools

############################Example############################
# x2_init = 1.0
# epsilon = 0.0001
# h = 0.6
# rel_error = 0.001 #percent

def func(x): #local max 0.7416
    nmtr = np.tanh(x)
    dnmtr = 1 + pow(x,2)
    return nmtr/dnmtr
#############################Example##############################

#############################Example##############################****

# x2_init = 0.2
# epsilon = 0.00001
# h = 0.1
# rel_error = 0.001 #percent

# x2_init = 0.19
# epsilon = 0.00001
# h = 0.09
# rel_error = 0.001 #percent

# def func(x): #local max 0.25
#     return pow(x,4) - 3*pow(x,3) + pow(x,2)

#############################Example##############################***

#############################Example##############################

# x2_init = -2.3
# epsilon = 0.00001
# h = 0.6
# rel_error = 0.001 #percent

# x2_init = -2
# epsilon = 0.00001
# h = 1
# rel_error = 0.001 #percent

# def func(x): #local max -3.0
#     return pow(x,3) + 3*pow(x,2) - 9*x + 7

#############################Example##############################

#############################Example##############################

# x2_init = 1.5
# epsilon = 0.00001
# h = 0.6
# rel_error = 0.001 #percent

# x2_init = 1.3
# epsilon = 0.00001
# h = 0.8
# rel_error = 0.001 #percent

# x2_init = 1.8
# epsilon = 0.00001
# h = 0.3
# rel_error = 0.001 #percent

# def func(x): #local max 2
#     return -pow(x,3) + 3*pow(x,2) - 4

#############################Example##############################

class QuadraticApprox():
    def __init__(self) -> None:
        self.z2_init = float(input("Initial Value of z2:\n"))
        self.h = float(input("Initial Value of h:\n"))
        self.epsilon = float(input("Give Epsilon:\n"))
        self.rel_error = float(input("Give Percent Relative Error: e.g 0.001 = %0.001:\n")) #percent
        self.iter_limit = int(input("Iteration Limit:\n"))

    def run(self):
        z_vals = [self.z2_init-self.h, self.z2_init, self.z2_init+self.h]
        iter_count = 0
        error = None #for division by zero error check

        for i in itertools.count(start=0):
            func_vals = [func(z_vals[0]), func(z_vals[1]), func(z_vals[2])]
            z_new = (z_vals[1] + (((1/2)* self.h)*(func_vals[0]-func_vals[2]) / (func_vals[0] -2*func_vals[1] + func_vals[2])))
            func_new = func(z_new)
            if z_vals[1] != 0:
                error = abs(z_new - z_vals[1])/abs(z_vals[1])*100
                if error <= self.rel_error: break

            self.h = (1/4)*(z_vals[2]-z_vals[0])

            if func_new > func_vals[1]:
                z_vals[0] = z_new - self.h
                z_vals[1] = z_new
                z_vals[2] = z_new + self.h

            if(abs(z_vals[2]-z_vals[0]) <=  self.epsilon): break
            if error != None and error <= self.rel_error: break
            if iter_count >= self.iter_limit: break
            iter_count += 1

        local_max = round(z_vals[1],4)
        print("Values of z:", z_vals)
        print("Iteration: ", iter_count)
        print("Local Maximum x value:", local_max, "Function Value at Local Maximum:", round(func(local_max),4))

if __name__ == '__main__':
    quadratic = QuadraticApprox()
    quadratic.run()
