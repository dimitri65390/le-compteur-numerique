def on_button_pressed_a():
    global nombre_élève
    nombre_élève += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global nombre_élève
    nombre_élève = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global nombre_élève
    nombre_élève += -1
input.on_button_pressed(Button.B, on_button_pressed_b)

nombre_élève = 0
nombre_élève = 0

def on_forever():
    global nombre_élève
    basic.show_string("" + str((nombre_élève)))
    if nombre_élève > 10:
        nombre_élève = 10
    if nombre_élève < 0:
        nombre_élève = 0
    if nombre_élève == 10:
        basic.show_leds("""
            . . # . .
                        . . # . .
                        . . # . .
                        . . . . .
                        . . # . .
        """)
basic.forever(on_forever)
