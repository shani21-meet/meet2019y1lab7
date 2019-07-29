def draw_2 (n,m,char) :
    for i in range(n-1) :
        shape = char*m
        print(shape)
    return(shape)

test1 = draw_2(5,3,'&')
print(test1)
    
