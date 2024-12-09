from pynput import keyboard
from pynput.keyboard import Controller

keyboard_controller = Controller()

# Словарь замен
replacements = {
    'а': 'a', 'б': '6', 'в': 'ß', 'г': 'g', 'д': 'd',
    'е': 'e', 'ё': 'ë', 'ж': 'ж', 'з': '3', 'и': 'u',
    'й': 'ũ', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'H',
    'о': 'o', 'п': 'n', 'р': 'p', 'с': 'c', 'т': 'т',
    'у': 'y', 'ф': 'f', 'х': 'x', 'ц': 'ц', 'ч': '4',
    'ш': 'w', 'щ': 'w', 'ъ': "'", 'ы': 'bI', 'ь': 'b',
    'э': 'e', 'ю': 'ю', 'я': 'я'
}

def on_press(key):
    try:
        if hasattr(key, 'char') and key.char in replacements:
            keyboard_controller.press(keyboard.Key.backspace)
            keyboard_controller.release(keyboard.Key.backspace)
            keyboard_controller.type(replacements[key.char])

    except Exception as e:
        pass 

def on_release(key):
    if key == keyboard.Key.esc:
        print("Завершение программы.")
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()