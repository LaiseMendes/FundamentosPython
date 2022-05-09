import os

print(os.getcwd())
#nums = []

for arquivo in os.listdir():
#    if arquivo == "Arquivos":
    if "Arquivos(" in arquivo:
        num = int(arquivo.split("(")[1].replace(")", ""))
        #nums.append(num)
        #print(type(num))

os.mkdir(f"Arquivos({num+1})")

#i = input("digite numero da pasta ")

