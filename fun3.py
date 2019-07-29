def draw_d1(num,char) :
    for i in range((num-1)*8) :
        Drawit = char*num
        print (Drawit)
    return Drawit


star1 = draw_d1(3,'*')
print(star1)
