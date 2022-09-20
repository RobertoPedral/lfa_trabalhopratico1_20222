
def leArquivo(arquiv):
	arquivo = open(arquiv, "r")
	automato = []
	##-----Adiciona cada linha na lista-----
	for linha in arquivo:
		automato.append(linha)
	##--------------------------------------
	arquivo.close()
	return automato




automato = leArquivo("afd.txt")

print(automato)
