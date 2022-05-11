# -*- utf-8 -*-

import PySimpleGUI as Sg
from mark import mark
from layout import *

while True:
    event, values = window.read()
    if event == Sg.WIN_CLOSED:
        break
    if event == "Oblicz":
        pkt = values["-ZDOBYTE-"]
        pkt = pkt.replace(",", ".")
        cale = values["-CALOSC-"]
        cale = cale.replace(",", ".")
        try:
            i = (float(pkt) / float(cale)) * 100
            j = mark(float(cale), float(pkt))
            window["procent"].update('{:.2f}%'.format(i))
            window["ocena"].update(j)
            window["-ZDOBYTE-"].update("")
        except ValueError:
            window["-ZDOBYTE-"].update("")
            window["-CALOSC-"].update("")
            pkt = []
            cale = []
    else:
        pass

window.close()
