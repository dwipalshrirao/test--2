import math


def print_mat_design(mat_height:int) ->None:
    if mat_height % 2==0:
        raise ValueError("mat height must odd  number")
    mat_width = mat_height * 3
    for i in range(0,math.floor(mat_height/2)): 
        s='.|.'*i
        print (s.rjust(math.floor((mat_width-2)/2),'-')+'.|.'+('.|.'*i).ljust(math.floor((mat_width-2)/2),'-'))
    print ('WELCOME'.center(mat_width,'-'))
    for i in reversed(range(0,math.floor(mat_height/2))): 
        s='.|.'*i
        print (s.rjust(math.floor((mat_width-2)/2),'-')+'.|.'+('.|.'*i).ljust(math.floor((mat_width-2)/2),'-'))


print("output: - ")
print_mat_design(10)