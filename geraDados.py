import os
import tkinter as tk
import json
import random
from faker import Faker
from tkinter import filedialog


def gerar_json():
    # Criar objeto Faker
    faker = Faker('')

    # Obter nome de arquivo
    filename = save_dir + "/dados.json"

    # Verificar se o nome de arquivo foi fornecido
    if not filename:
        return

    # Gerar dados JSON e escrever em um único arquivo
    with open(filename, "w") as outfile:
        outfile.write("{ " + "\n")
        outfile.write('"clients"' + ":[" + "\n")
        for i in range(int(quantidade_entry.get())):
            nome = faker.name()
            email = faker.email()
            idade = random.randint(18, 100)
            cidade = faker.city()
            telefone = faker.phone_number()
            empresa = faker.company()
            pais = faker.country()

            dados = dict(nome=nome, email=email, idade=idade, cidade=cidade, telefone=telefone, empresa=empresa,
                         pais=pais)

            json_data = json.dumps(dados, indent=4)
            #outfile.write('"client"' + ":")
            outfile.write(json_data)  # Adicionar quebra de linha após cada registro
            outfile.write("," + "\n")  # Adicionar quebra de linha após cada registro
        outfile.write("]" + "\n")
        outfile.write("}" + "\n")

    # Exibir mensagem de sucesso
    status_label.config(text=f"Dados JSON salvos em: {save_dir} {filename}")


window = tk.Tk()
window.title("Gerador Automático de JSON - Omar Moussa")
window.geometry('800x200')


# Campo de entrada para quantidade de dados
quantidade_label = tk.Label(window, text="Quantidade de Dados:")
quantidade_label.pack()
quantidade_entry = tk.Entry(window)
quantidade_entry.pack()

# Botão para escolher local de salvamento
escolher_diretorio_button = tk.Button(window, text="Escolher Diretório", command=lambda: escolher_diretorio())
escolher_diretorio_button.pack()

# Rótulo para mostrar o diretório selecionado
diretorio_label = tk.Label(window, text="Diretório de Salvamento: Nenhum")
diretorio_label.pack()

# Botão para gerar JSON
gerar_button = tk.Button(window, text="Gerar JSON", command=gerar_json)
gerar_button.pack()

# Rótulo para status
status_label = tk.Label(window, text="")
status_label.pack()

def escolher_diretorio():
    """
    Função para escolher o diretório de salvamento dos arquivos JSON.
    """
    global save_dir
    save_dir = filedialog.askdirectory()
    if save_dir:
        diretorio_label.config(text=f"Diretório de Salvamento: {save_dir}")

window.mainloop()
