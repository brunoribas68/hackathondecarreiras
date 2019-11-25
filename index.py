import sys


def areAnagram(palavra1, palavra2):

	n1 = len(palavra1)
	n2 = len(palavra2)

	if n1 != n2:
		return 0

	palavra1 = sorted(palavra1)
	palavra2 = sorted(palavra2)

	for i in range(0, n1):
		if palavra1[i] != palavra2[i]:
			return 0

	return 1

def validacaoPalavra(palavrasQualquer):
	valido = 0
	for palavra in palavrasQualquer:
		if palavra.isalpha():
			valido += 0
		else:
			valido += 1
	return valido

def getAnagramas(palavrasAComparar, listaPalavras):
	anagramas = []
	for palavra in listaPalavras:
		for palavraComparada in palavrasAComparar:
			if areAnagram(palavra.upper(), palavraComparada.upper()):
				combinacao =  palavraComparada
				anagramas.append(combinacao)
			else:
				continue
	return anagramas

palavrasAComparar = sys.argv[1]
palavrasAComparar = palavrasAComparar.split(' ')
listaPalavras = open('palavras.txt').read().split()
if (validacaoPalavra(palavrasAComparar) == 0 and validacaoPalavra(listaPalavras) == 0):
	anagramas = getAnagramas(palavrasAComparar,listaPalavras)
	if len(anagramas) > 0:
		for anagrama in anagramas:
			print(anagrama + '\n')
	else:
		print('Nenhuma anagrama encontrado no universo de palavas do arquivo palavras.txt')
else:
	print("Somente palavras que contem caracteres de A-Z")
