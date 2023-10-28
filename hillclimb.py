import random
def obj_fn(x):return -x**2  

def h_c(max_it, step_size, x):
    for _ in range(max_it):
        curr_val = obj_fn(x)
        nxt_x = x + random.uniform(-step_size, step_size)
        nxt_val = obj_fn(nxt_x)
        
        if nxt_val > curr_val:
            x = nxt_x
    
    return x

max_it = 1000
step_size = 0.1
initial_x = 5.0  

opt_soln = h_c(max_it, step_size, initial_x)
print(f"Optimal solution found: x = {opt_soln}, f(x) = {obj_fn(opt_soln)}")