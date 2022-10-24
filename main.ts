input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    nombre_élève += 1
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    nombre_élève = 0
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    nombre_élève += -1
})
let nombre_élève = 0
nombre_élève = 0
basic.forever(function on_forever() {
    
    basic.showString("" + ("" + nombre_élève))
    if (nombre_élève > 10) {
        nombre_élève = 10
    }
    
    if (nombre_élève < 0) {
        nombre_élève = 0
    }
    
    if (nombre_élève == 10) {
        basic.showLeds(`
            . . # . .
                        . . # . .
                        . . # . .
                        . . . . .
                        . . # . .
        `)
    }
    
})
