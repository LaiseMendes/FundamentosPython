import json

class Query():
    def __init__(self):
        pass

    def busca(self):
        with open("banco_de_arquivos.json", "r") as f:
            dados = json.load(f)

        for key in dados:
            for info in dados[key]:
                print(info)