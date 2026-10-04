#           from  middle  to 
def solve(n,first,second,third): 
    if n == 0:
        return  
    else: 
        solve(n-1,first,third,second)
        print(f"Move disk-{n} from tower-{first} to tower-{third}")
        solve(n-1,second,first,third)
solve(3,"1","2","3")