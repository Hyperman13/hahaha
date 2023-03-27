a = 0
b = 0

def on_button_pressed_a():
    global a
    a += 1
    basic.show_number(a)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_leds("""
        . # . # .
                . # . # .
                . . . . .
                . # # # .
                . # . # .
    """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global b
    b += 1
    basic.show_number(b)
input.on_button_pressed(Button.B, on_button_pressed_b)
