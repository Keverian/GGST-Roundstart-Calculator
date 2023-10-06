import vgamepad as vg
import time

#Function use for command as temporary
def inputConvert(input, pad: vg.VDS4Gamepad):
    if input == 'option':
        pad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_OPTIONS)
        pad.update()
        time.sleep(0.1)
        pad.releases_button(button=vg.DS4_BUTTONS.DS4_BUTTON_OPTIONS)
        pad.update()
    elif input == 't':
        pad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)
        pad.update()
        time.sleep(0.1)
        pad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)
        pad.update()
    elif input == 's':
        pad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SQUARE)
        pad.update()
        time.sleep(0.1)
        pad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SQUARE)
        pad.update()
    elif input == 'x':
        pad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
        pad.update()
        time.sleep(0.1)
        pad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
        pad.update()
    elif input == 'c':
        pad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
        pad.update()
        time.sleep(0.1)
        pad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
        pad.update()
    elif input == '1':
        pad.left_joystick_float(x_value_float=-1.0, y_value_float=-1.0)
    elif input == '2':
        pad.left_joystick_float(x_value_float=0.0, y_value_float=-1.0)
    elif input == '3':
        pad.left_joystick_float(x_value_float=1.0, y_value_float=-1.0)
    elif input == '4':
        pad.left_joystick_float(x_value_float=-1.0, y_value_float=0.0)
    elif input == '5':
        pad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
    elif input == '6':
        pad.left_joystick_float(x_value_float=1.0, y_value_float=0.0)
    elif input == '7':
        pad.left_joystick_float(x_value_float=-1.0, y_value_float=1.0)
    elif input == '8':
        pad.left_joystick_float(x_value_float=0.0, y_value_float=1.0)
    elif input == '9':
        pad.left_joystick_float(x_value_float=1.0, y_value_float=1.0)

    pad.update()
    pad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
    time.sleep(0.1)
    pad.update()
# TODO: grab doesnt work, release 6/4 too early for d to input, stick constantly return to neutral
def strToInp(cmd, pad: vg.VDS4Gamepad): #remember to add player side back
    cmd = cmd.lower()
    #run through the string
    for input in cmd:
        if input == '5':
            pad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
        elif input == '6':
            pad.left_joystick_float(x_value_float=1.0, y_value_float=0.0)
        elif input == '2':
            pad.left_joystick_float(x_value_float=0.0, y_value_float=-1.0)
        elif input == '3':
            pad.left_joystick_float(x_value_float=1.0, y_value_float=-1.0)
        elif input == '4':
            pad.left_joystick_float(x_value_float=-1.0, y_value_float=0.0)
        elif input == '5':
            pad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
        elif input == '1':
            pad.left_joystick_float(x_value_float=-1.0, y_value_float=-1.0)
        elif input == '7':
            pad.left_joystick_float(x_value_float=-1.0, y_value_float=1.0)
        elif input == '8':
            pad.left_joystick_float(x_value_float=0.0, y_value_float=1.0)
        elif input == '9':
            pad.left_joystick_float(x_value_float=1.0, y_value_float=1.0)
        elif input == 's':
            pad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)
            pad.update()
            time.sleep(0.05)
            pad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)

        elif input == 'p':
            pad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SQUARE)
            pad.update()
            time.sleep(0.05)
            pad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SQUARE)

        elif input == 'k':
            pad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
            pad.update()
            time.sleep(0.05)
            pad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)

        elif input == 'd':
            pad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
            pad.update()
            time.sleep(0.05)
            pad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
        elif input == 'h':
            pad.press_button(button=vg.DS4_BUTTON_TRIGGER_RIGHT)
            pad.update()
            time.sleep(0.05)
            pad.release_button(button=vg.DS4_BUTTON_TRIGGER_RIGHT)

        pad.update()
        time.sleep(0.05)

    pad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
    pad.update()

lgamepad = vg.VDS4Gamepad()
#rgamepad = vg.VDS4Gamepad()
lui = input()
#rui = ''
if lui == 'start':
    print('starting')
time.sleep(2)
checker = True

while checker:
    print('inputs for l:')
    lui = input()
    time.sleep(1)
    print("userinput =" + lui)
    if lui == 'break':
        checker = False
    else:
        print('why did this run again')
        inputConvert(lui, lgamepad)
    print("checker is " + str(checker))

checker = True
print("the code ran to here")
while checker:
    print('inputs for l2:')
    lui = input()
    time.sleep(1)
    strToInp(lui, lgamepad)
    if lui == 'break':
        checker = False
        break
    else:
        strToInp(lui, lgamepad)

