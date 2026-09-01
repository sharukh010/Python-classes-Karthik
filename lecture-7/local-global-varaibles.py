# local variable are defined inside a scope 
# global variables are defined outside any scope 
# they are defined inside global scope 
gv = 10 
def demo(): 
    # lv = 20 
    global gv # all gv changes are global 
    # gv = 20 # function thinks it a local variable 
    gv = 20 
    print(gv)
demo()
print(gv)
# print(lv) # give you name error 