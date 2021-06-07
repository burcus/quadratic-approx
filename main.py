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
        self.x2_init = float(input("Initial Value of z2:\n"))
        self.h = float(input("Initial Value of h:\n"))
        self.epsilon = float(input("Give Epsilon:\n"))
        self.rel_error = float(input("Give Percent Relative Error: e.g 0.001 = %0.001:\n")) #percent
        self.iter_limit = int(input("Iteration Limit:\n"))

    def run(self):
        x_vals = [self.x2_init-self.h, self.x2_init, self.x2_init+self.h]
        iter_count = 0
        error = None #for division by zero error check

        for i in itertools.count(start=0):
            y_vals = [func(x_vals[0]), func(x_vals[1]), func(x_vals[2])]
            x_new = (x_vals[1] + (((1/2)* self.h)*(y_vals[0]-y_vals[2]) / (y_vals[0] -2*y_vals[1] + y_vals[2])))
            func_new = func(x_new)
            if x_vals[1] != 0:
                error = abs(x_new - x_vals[1])/abs(x_vals[1])*100
                if error <= self.rel_error: break

            self.h = (1/4)*(x_vals[2]-x_vals[0])

            if func_new > y_vals[1]:
                x_vals[0] = x_new - self.h
                x_vals[1] = x_new
                x_vals[2] = x_new + self.h

            if(abs(x_vals[2]-x_vals[0]) <=  self.epsilon): break
            if error != None and error <= self.rel_error: break
            if iter_count >= self.iter_limit: break
            iter_count += 1

        local_max = round(x_vals[1],4)
        print("Values of z:", x_vals)
        print("Iteration: ", iter_count)
        print("Local Maximum x value:", local_max, "Function Value at Local Maximum:", round(func(local_max),4))

if __name__ == '__main__':
    quadratic = QuadraticApprox()
    quadratic.run()
