import re

def leArquivo(arquiv):
	arquivo = open(arquiv, "r")
	automato = []
	##-----Adiciona cada linha na lista-----
	for linha in arquivo:
		automato.append(linha)
	##--------------------------------------
	arquivo.close()
	return automato

def leRegrasDeTransicao(automato):
	regras = []
	for i in range(1, len(automato)):
		automato[i] = automato[i].strip("\n").replace(" ", "").split(",")
		regras.append(automato[i])
	return regras









automato = leArquivo("afd.txt") 

regras = leRegrasDeTransicao(automato)


for i in len(regras):
	print(regras[i])


palavra = input("Digite uma palavra: ")




""" print(automato[1])

for c in automato[0]:
	if c == "D":
		print("Achei") """






