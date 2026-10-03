def display(n): 
    if n == 0: 
        return 
    else: 
        print(n)
        display(n-1)

display(10)