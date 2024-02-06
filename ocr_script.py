import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os

def preprocess_image_for_hex(image_path):
    image = Image.open(image_path).convert('L')
    image = ImageEnhance.Contrast(image).enhance(4)
    image = image.filter(ImageFilter.SHARPEN)
    image = image.point(lambda x: 0 if x < 128 else 255, '1')
    return image

def perform_ocr_on_image(image, text_type):
    config_map = {
        'hex': r'--psm 11 -c tessedit_char_whitelist=0123456789ABCDEFabcdef',
        'digit': r'--psm 6 -c tessedit_char_whitelist=0123456789',
        'alpha': r'--psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        'all': r'--psm 6'
    }
    custom_config = config_map.get(text_type, r'--psm 6')
    return pytesseract.image_to_string(image, config=custom_config)

def save_text_to_file(text, output_file_path):
    with open(output_file_path, 'w') as file:
        file.write(text)

def center_window(window):
    window.update_idletasks()  # Atualiza o layout para obter as dimensões corretas
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def ask_text_type(root):
    choice_window = tk.Toplevel(root)
    choice_window.title("Escolha o Tipo de Texto")
    choice_window.geometry("300x100")

    # Após definir a geometria inicial, centralize a janela
    center_window(choice_window)

    text_type_var = tk.StringVar(value='all')

    label = tk.Label(choice_window, text="Selecione o tipo de texto:")
    label.grid(column=0, row=0, padx=10, pady=5)

    text_type_combobox = ttk.Combobox(choice_window, width=17, textvariable=text_type_var, state="readonly")
    text_type_combobox['values'] = ('hex', 'digit', 'alpha', 'all')
    text_type_combobox.grid(column=1, row=0, padx=10, pady=5)
    text_type_combobox.current(3)

    confirm_button = tk.Button(choice_window, text="Confirmar", command=choice_window.destroy)
    confirm_button.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

    choice_window.wait_window()

    return text_type_var.get()

def main():
    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo("Selecionar o Tesseract OCR", "Por favor, selecione o executável do Tesseract OCR (tesseract.exe).")
    tesseract_path = filedialog.askopenfilename(title="Selecione o executável do Tesseract OCR")
    if tesseract_path:
        pytesseract.pytesseract.tesseract_cmd = tesseract_path
    else:
        print("Executável do Tesseract não selecionado.")
        return

    messagebox.showinfo("Selecionar Imagem", "Por favor, selecione a imagem para realizar o OCR.")
    image_path = filedialog.askopenfilename(title="Selecione a imagem para OCR")
    if not image_path:
        print("Nenhuma imagem selecionada.")
        return

    text_type = ask_text_type(root)
    if text_type:
        if text_type == 'hex':
            image = preprocess_image_for_hex(image_path)
        else:
            image = Image.open(image_path)
        text = perform_ocr_on_image(image, text_type)
        base_name = os.path.splitext(image_path)[0]
        output_file = f"{base_name}_output.txt"
        save_text_to_file(text, output_file)
        print(f"Texto extraído com sucesso e salvo em: {output_file}")
    else:
        print("Tipo de texto não fornecido.")

if __name__ == "__main__":
    main()
