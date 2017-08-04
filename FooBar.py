for x in range (100, 10001):

    #Square Test
    for y in range (1,x):
        square = False
        if (x/y == y):
            square = True
            print "Foo"
            break
        else:
            continue
        break




    #Prime Test
    for z in range (2, x):
        prime = True
        if (x % z -- 0):
            prime = False
        else:
            continue
        if prime:
            print "Bar"
            break
        break
