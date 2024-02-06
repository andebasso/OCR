# Projeto de OCR (Reconhecimento Óptico de Caracteres)

Este projeto implementa uma solução de OCR (Reconhecimento Óptico de Caracteres) utilizando o Python, Tesseract OCR, e uma interface gráfica básica (GUI) com Tkinter. O software permite ao usuário selecionar uma imagem do sistema de arquivos e extrair texto dela, otimizando o processo para diferentes tipos de texto, como hexadecimal, dígitos, alfabético, ou uma mistura de todos.

## Características

- **Seleção de Imagem**: Permite ao usuário selecionar uma imagem de seu sistema de arquivos para o reconhecimento de texto.
- **Pré-processamento de Imagem**: Aplica técnicas de pré-processamento na imagem para melhorar a qualidade do texto a ser reconhecido, incluindo ajuste de contraste e nitidez.
- **Suporte a Diferentes Tipos de Texto**: Oferece a opção de otimizar o reconhecimento de texto para formatos específicos - hexadecimal, dígitos, letras alfabéticas ou todos.
- **Interface Gráfica Amigável**: Utiliza Tkinter para uma interface gráfica simples, facilitando a interação com o usuário.
- **Exportação de Texto**: Salva o texto extraído em um arquivo `.txt`, no mesmo diretório da imagem original.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para implementar a lógica do software.
- **Tesseract OCR**: Motor de OCR open-source utilizado para a extração de texto das imagens.
- **Tkinter**: Biblioteca para criação da interface gráfica.

## Requisitos

- Python 3.x
- Bibliotecas Python: Pillow, pytesseract, tkinter (geralmente vem instalada com Python).
- Tesseract OCR instalado no sistema e configurado nas variáveis de ambiente do PATH.

## Instalação

1. **Instalar o Python**: Certifique-se de ter o Python 3.x instalado em seu sistema.
2. **Instalar o Tesseract OCR**: [Baixe e instale o Tesseract OCR](https://github.com/tesseract-ocr/tesseract) seguindo as instruções para o seu sistema operacional.
3. **Instalar Dependências do Python**: Execute o seguinte comando no terminal para instalar as bibliotecas necessárias:
   ```bash
   pip install Pillow pytesseract
