def mark(x, y):
    z = (y/x)*100

    if z >= 90.50:
        if z >= 97.75:
            a = "5+"
        elif z <= 93.25:
            a = "5-"
        else:
            a = "5"
    elif 90.49 > z >= 75.50:
        if z >= 86.5:
            a = "4+"
        elif z <= 79.5:
            a = "4-"
        else:
            a = "4"
    elif 75.49 > z >= 60.50:
        if z >= 71.5:
            a = "3+"
        elif z <= 63.5:
            a = "3-"
        else:
            a = "3"
    elif 60.49 > z >= 50.50:
        if z >= 57.75:
            a = "2+"
        elif z <= 53.25:
            a = "2-"
        else:
            a = "2"
    elif 50.49 > z >= 0:
        if z >= 37.5:
            a = "1+"
        elif z <= 12.5:
            a = "1-"
        else:
            a = "1"
    else:
        a = "Bląd"
    return a