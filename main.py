import re

def leArquivo(arquiv):
	arquivo = open(arquiv, "r")
	automato = []
	##-----Adiciona cada linha na lista-----
	for linha in arquivo:
		automato.append(linha.strip("\n").replace(" ", "").split(","))
	##--------------------------------------
	arquivo.close()
	return automato





def vals(automato):
	automa = {}
	chave = ''
	for li in automato:
		if (li[0] == '#states'):
			chave = 'states'
			continue
		elif (li[0] == '#initial'):
			chave = 'initial'
			continue

		elif (li[0] == '#accepting'):
			chave = 'accepting'
			continue

		elif (li[0] == '#alphabet'):
			chave = 'alphabet'
			continue

		elif (li[0] == '#transitions'):
			chave = 'transitions'
			continue
		
		automa[chave] = []
		automa[chave].append(li[0])

	return automa













automato = leArquivo("afd.txt") 


automato = vals(automato)

print(automato)



palavra = input("Digite uma palavra: ")




""" print(automato[1])

for c in automato[0]:
	if c == "D":
		print("Achei") """






