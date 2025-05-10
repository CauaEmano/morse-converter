import time, winsound
from unidecode import unidecode
import ttkbootstrap as ttk
from tkinter import filedialog

def play_morse(morse_code):
    for symbol in morse_code:
        if symbol == '.':
            winsound.Beep(700, 150)
        elif symbol == '-':
            winsound.Beep(700, 400)
        elif symbol == '/':
            time.sleep(0.5)
        elif symbol == ' ':
            time.sleep(0.2)
        time.sleep(0.1)

def transcrever(base):
    transcrito = ''
    for letter in unidecode(base.upper()):
        transcrito += MORSE_CODE.get(letter, '') + ' '
    return transcrito

def salvar():
    texto_original = entrada.get()
    transcrito_morse = transcrever(texto_original)

    if not texto_original.strip():
        return
    
    caminho = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Arquivos de Texto", "*.txt")],
        title="Salvar como..."
    )

    if caminho:
        with open(caminho, 'w', encoding='utf-8') as i:
            i.write(f'''texto original: 
{texto_original}
texto transcrito: 
{transcrito_morse}''')

MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.',  ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.',  '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'  # espaço entre palavras
}

def main():
    morse = transcrever(entrada.get())
    print(f"Texto: {entrada.get()}")
    print (f'Morse: {morse}')
    play_morse(morse)


janela = ttk.Window(themename='superhero', title='Conversor de texto para código morse', size=(500,200))

ttk.Label(janela, text='Digite aqui o seu texto :', font=('Segoe UI', 24)).pack()
entrada = ttk.Entry(janela, width=50)
entrada.pack(pady=5)

ttk.Button(janela, text='Converter', command=main).pack(pady=10)
ttk.Button(janela, text="Salvar como .txt", bootstyle='SECONDARY', command=salvar).pack(pady=5)

janela.mainloop()