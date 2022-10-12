

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


def transfAFND(automato):

	afd = {}
	afd['states'] = []
	afd['initial'] = automato['initial'][:]
	afd['accepting'] = []
	afd['alphabet'] = automato['alphabet'][:]
	afd['transitions'] = []

	estado_atual = automato['initial'][0]

	afd['states'].append(estado_atual)
	
	for estado in afd['states']:

		for letra in afd['alphabet']:


			for transit in automato['transitions']:			


				transit = transit.replace('>', ':')
				transit = transit.replace(',', ':')
				transit = transit.split(':')

				transit_estado_entrada = transit[0]
				transit_letra = transit[1]
				transit_estado_saida = transit[2:]



				if (',' in estado):
					state = estado.split(',')
				else:
					state = [estado]


				if (transit_estado_entrada in state):

					for st in state:

						if (len(transit_estado_saida) == 1):

							if (transit_estado_entrada == st) and (
								transit_letra == letra):


								afd['transitions'].append(f'{st}:{letra}>{transit_estado_saida[0]}')
							
						elif(len(transit_estado_saida) > 1):

							if (transit_estado_entrada == st) and (
								transit_letra == letra):

								afd['transitions'].append(f'{st}:{letra}>')


							



					
				afd['transitions'].append(f'{estado_atual}:{letra}>{transit_estado_saida[0]}')

		

	print(afd['transitions'])




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
        

     

    
    
	
    
	










