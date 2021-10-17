import PySimpleGUI as Sg

lewa = [
    [
        Sg.Text("Pkt do zdobycia ", background_color = "lightgray", text_color = "black"), 
    ], 
    [
        Sg.Text("Pkt zdobyte ", background_color = "lightgray", text_color = "black"), 
    ], 
]

srodek = [
    [
        Sg.In(size = (5, 1), key = "-CALOSC-"), 
    ], 
    [
        Sg.In(size = (5, 1), key = "-ZDOBYTE-"), 
    ], 
]

prawa = [
    [
        Sg.Button("Oblicz", button_color = ("black", "lightgray"), bind_return_key = True), 
    ], 
]

lewadwa = [
    [
        Sg.Text("Procenty", background_color = "lightgray", text_color = "black"), 
    ], 
    [
        Sg.Text("Ocena", background_color = "lightgray", text_color = "black"), 
     ], 
]

prawadwa = [
    [
        Sg.Text("", key = "procent", background_color = "lightgray", text_color = "black"), 
    ], 
    [
        Sg.Text("", key = "ocena", background_color = "lightgray", text_color = "black"), 
    ], 
]

layout = [
    [
        Sg.Column(lewa, background_color = "lightgray"), 
        Sg.Column(srodek, background_color = "lightgray"), 
        Sg.Column(prawa, background_color = "lightgray"), 
    ], 
    [
        Sg.HSeparator(), 
    ], 
    [
        Sg.Column(lewadwa, pad = (37, 0), background_color = "lightgray"), 
        Sg.Column(prawadwa, background_color = "lightgray"), 
    ]
]
window = Sg.Window("Kalkulator Ocen", layout, background_color = "lightgray", icon = ".\\icon"
                                                                                 "\\calc.ico")  
