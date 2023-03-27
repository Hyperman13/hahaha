let a = 0
let b = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    a += 1
    basic.showNumber(a)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showLeds(`
        . # . # .
                . # . # .
                . . . . .
                . # # # .
                . # . # .
    `)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    b += 1
    basic.showNumber(b)
})
