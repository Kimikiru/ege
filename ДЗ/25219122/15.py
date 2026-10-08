for a in range(1, 1000):
    is_valid = True
    for x in range(1,100):
        for y in range(1,100):
            f = (x+y <= 27) or (y<=x-1) or (y >= a)
            if not f:
                is_valid = False
                break
        if not is_valid:
            break
    if is_valid:
        print(a)