# Enter your code here
camel_variable=input(("name your variable:"))

def snake(a):
    c=(a.replace('_',' '))
    #keep the terms seperate to captalize second terms
    d=c.title() 
    #learned how to slice in order to pick capitalized letterw
    e=(d[:1].lower()+d[1:])
    return e.replace(' ','')
    
#tested for 2+ terms
print(snake(camel_variable))
#just realized i did it wrong but i spent too long to delete it