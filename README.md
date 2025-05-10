# 🔠 Morse Converter com Interface Gráfica

Este é um conversor de texto para **código Morse** com uma interface moderna feita com [`ttkbootstrap`](https://ttkbootstrap.readthedocs.io/). O aplicativo permite que você:

* Digite qualquer texto (com ou sem acentuação);
* Converta para código Morse;
* Exiba o resultado visualmente;
* Reproduza os sinais sonoros (ponto e traço);
* Salve a transcrição em um arquivo `.txt`.

---

## 🖼️ Demonstração

> *\[Adicione aqui um print ou um GIF da interface.]*
> Você pode usar o [ScreenToGif](https://www.screentogif.com/) para criar um gif da aplicação.

---

### 🚀 Como usar

### 1. Clone o repositório

git clone [https://github.com/seu-usuario/morse-converter.git](https://github.com/seu-usuario/morse-converter.git)

cd morse-converter

### 2. Instale as dependências

pip install -r requirements.txt

### 3. Execute o projeto

python morse_converter.py

## 📂 Estrutura do Projeto

morse-converter/

├── morse_converter.py       # Código principal do conversor
├── requirements.txt         # Dependências do projeto
└── README.md                # Este arquivo

## 📦 Bibliotecas Utilizadas

1. [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap)
2. [unidecode](https://pypi.org/project/Unidecode/)
3. [winsound (Windows Only)](https://docs.python.org/3/library/winsound.html) — para reprodução dos sons
4. [tkinter]
5. [time]

## ✨ Funcionalidades

* ✅ Interface gráfica estilizada
* ✅ Suporte a letras, números e pontuações básicas
* ✅ Remoção automática de acentos
* ✅ Exibição do código Morse com espaçamento
* ✅ Exportação para `.txt`