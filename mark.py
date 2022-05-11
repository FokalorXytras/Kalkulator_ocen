def mark(i, j):
    k = (i/j)*100

    if k >= 90.50:
        if k >= 97.75:
            a = "5+"
        elif k <= 93.25:
            a = "5-"
        else:
            a = "5"
    elif k >= 75.50:
        if k >= 86.5:
            a = "4+"
        elif k <= 79.5:
            a = "4-"
        else:
            a = "4"
    elif k >= 60.50:
        if k >= 71.5:
            a = "3+"
        elif k <= 63.5:
            a = "3-"
        else:
            a = "3"
    elif k >= 50.50:
        if k >= 57.75:
            a = "2+"
        elif k <= 53.25:
            a = "2-"
        else:
            a = "2"
    elif k >= 0:
        if k >= 37.5:
            a = "1+"
        elif k <= 12.5:
            a = "1-"
        else:
            a = "1"
    else:
        a = "Błąd"
    return a
