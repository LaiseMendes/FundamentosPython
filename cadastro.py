import json
import os

class Cadastro():
    def __init__(self):
        pastaScript = os.listdir("Scripts")
        self.dicionario = {}

        with open("banco_de_arquivos.json", "r", encoding="utf8") as f:
            data = json.load(f)

        for script in pastaScript:
            if ".py" in script or ".mel" in script:
                self.nome = script
                if self.nome not in data:
                    self.descricao = input(f"Digite uma descrição do arquivo {script}: ")
                    
                    self.dicionario[self.nome] = {}
                    #self.dicionario["nome"] = self.nome
                    self.dicionario[self.nome]["descricao"] = self.descricao

    def armazena(self):
        try:
            with open("banco_de_arquivos.json", "r+", encoding="utf8") as f:
                infoScript = json.load(f)
                infoScript.update(self.dicionario)
                f.seek(0)
                json.dump(infoScript, f, ensure_ascii=False, indent=2)
        except FileNotFoundError:
            with open("banco_de_arquivos.json", "a", encoding="utf8") as f:
                json.dump(self.dicionario, f, ensure_ascii=False, indent=2)

