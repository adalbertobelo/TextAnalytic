import re
from collections import Counter
import tkinter as tk
from tkinter import scrolledtext

def analisar_texto():
    texto = entrada_texto.get("1.0", tk.END)

    # Contar o número de palavras
    palavras = texto.split()
    num_palavras = len(palavras)

    # Contar o número de caracteres (incluindo espaços)
    num_caracteres = len(texto)

    # Contar o número de frases (baseado em pontos finais, exclamações e interrogações)
    num_frases = len(re.findall(r'[.!?]', texto))

    # Encontrar as palavras mais frequentes
    contador_palavras = Counter(palavras)
    palavras_frequentes = contador_palavras.most_common(10)  # 10 palavras mais frequentes

    # Calcular a média de palavras por frase
    media_palavras_por_frase = num_palavras / num_frases if num_frases > 0 else 0

    # Limpar a caixa de texto de saída
    saida_texto.delete("1.0", tk.END)

    # Exibir as estatísticas na caixa de texto de saída
    saida_texto.insert(tk.END, f"Número de palavras: {num_palavras}\n")
    saida_texto.insert(tk.END, f"Número de caracteres: {num_caracteres}\n")
    saida_texto.insert(tk.END, f"Número de frases: {num_frases}\n")
    saida_texto.insert(tk.END, f"Média de palavras por frase: {media_palavras_por_frase:.2f}\n")
    saida_texto.insert(tk.END, "Palavras mais frequentes:\n")
    for palavra, frequencia in palavras_frequentes:
        saida_texto.insert(tk.END, f"{palavra}: {frequencia} vezes\n")

# Configurar a janela
janela = tk.Tk()
janela.title("Analisador de Texto")
janela.geometry("600x400")

# Rótulo
rotulo = tk.Label(janela, text="Digite o texto que deseja analisar:")
rotulo.pack()

# Caixa de entrada de texto
entrada_texto = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=60, height=10)
entrada_texto.pack()

# Botão para realizar a análise
botao_analisar = tk.Button(janela, text="Analisar Texto", command=analisar_texto)
botao_analisar.pack()

# Caixa de texto de saída
saida_texto = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=60, height=15)
saida_texto.pack()

janela.mainloop()