def triangel_area():
    one = float(input('Length of the first side: '))
    two = float(input('Length of the second side: '))
    three = float(input('Length of the thrid side: '))
    
    p = ( one + two + three)/2

    a = (p*(p-one)*(p-two)*(p-three))**(1/2)

    print(a)

triangel_area()