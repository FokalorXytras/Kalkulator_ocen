def mark(i, j):
    k = (j/i)*100
    k = round(k, 2)

    if 90.50 <= k <= 100:
        if 97.75 <= k:
            a = "5+"
        elif 93.25 <= k:
            a = "5-"
        else:
            a = "5"
    elif 75.50 <= k <= 90.49:
        if 86.5 <= k:
            a = "4+"
        elif 79.5 <= k:
            a = "4-"
        else:
            a = "4"
    elif 60.50 <= k <= 75.49:
        if 71.5 <= k:
            a = "3+"
        elif 63.5 <= k:
            a = "3-"
        else:
            a = "3"
    elif 50.50 <= k <= 60.49:
        if 57.75 <= k:
            a = "2+"
        elif 53.25 <= k:
            a = "2-"
        else:
            a = "2"
    elif 0 <= k <= 50.49:
        if 37.5 <= k:
            a = "1+"
        elif 12.5 <= k:
            a = "1-"
        else:
            a = "1"
    else:
        a = "Błąd"
    return a
