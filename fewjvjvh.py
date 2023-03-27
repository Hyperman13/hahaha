def on_received_number(receivedNumber):
    basic.show_icon(IconNames.SMALL_DIAMOND)
    if receivedNumber == 0:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # # # # #
                        . . . . .
                        . . . . .
        """)
    if receivedNumber == 1:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
    if receivedNumber == 2:
        basic.show_leds("""
            . # # # #
                        # . . . .
                        . # # # .
                        . . . . #
                        # # # # .
        """)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
                . # # # .
                # . # . #
                # # # # #
                # # # # #
    """)
    radio.send_number(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_leds("""
        . # # # #
                # . . . .
                . # # # .
                . . . . #
                # # # # .
    """)
    radio.send_number(2)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        . # # # .
                # . # . #
                # # # # #
                # # # # #
                # # # # #
    """)
    radio.send_number(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(69)
