import re

def leArquivo(arquiv):
	arquivo = open(arquiv, "r")
	automato = []
	##-----Adiciona cada linha na lista-----
	for linha in arquivo:
		automato.append(linha.strip("\n"))
	##--------------------------------------
	arquivo.close()
	return automato





def vals(automato):
	automa = {}
	chave = ''
	for li in automato:
		if (li == '#states'):
			chave = 'states'
			automa[chave] = []
			continue
		elif (li == '#initial'):
			chave = 'initial'
			automa[chave] = []
			continue

		elif (li == '#accepting'):
			chave = 'accepting'
			automa[chave] = []
			continue

		elif (li == '#alphabet'):
			chave = 'alphabet'
			automa[chave] = []
			continue

		elif (li == '#transitions'):
			chave = 'transitions'
			automa[chave] = []
			continue
		
		automa[chave].append(li)

	return automa


def lerPalavra(automato, palavra):
    
	estado_atual = automato['initial'][0]
 


	for letra in palavra:
		validacao = False
  
		if letra not in automato['alphabet']:
			return False

		for transit in automato['transitions']:
						
			transit = transit.replace('>', ':')
			transit = transit.replace(',', ':')
			transit = transit.split(':')
			transit_estado_entrada, transit_letra, transit_estado_saida = transit
			if (transit_estado_entrada == estado_atual) and (
			    transit_letra == letra):
				print("(" + estado_atual + ", " + letra + ") = " +
				      transit_estado_saida)
				estado_atual = transit_estado_saida
				validacao = True
				break

		if not validacao:
			return False
	if estado_atual in automato['accepting']:
		return True
	else:
		return False




def tipoAut(automato):
    for transit in automato['transitions']:		
        if ',' in transit:
            print('Autômatos Finitos Não Determinístico (AFND) Identificado, Funcionalidade Está Em Manutenção. Por favor insira outro automato')
            return False
    print('Autômatos Finitos Determinístico (AFD) Identificado')
    return True
            
		
				

while True:
	arquivo = input("Digite o Nome do Arquivo: ")

	automato = leArquivo(arquivo) 


	automato = vals(automato)


	if tipoAut(automato):
		palavra = input("Digite uma palavra: ")
		
		if lerPalavra(automato, palavra):
			print('Palavra Aceita')
		else:
			print('Palavra Recusada')
   
	parada = input("Digite 0 para terminar: ")
 
	if parada == '0':
		break
        

     

    
    
	
    
	










