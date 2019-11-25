def areAnagram(palavras1, palavras2):

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

palavras1 = input("Palavra 1: ")
palavras1 = palavras1.split(' ')
palavras2 = input("Palavra 2: ")
palavras2 = palavras2.split(' ')

if (validacaoPalavra(palavras1) == 0 and validacaoPalavra(palavras2) == 0):
	if areAnagram(palavras1, palavras2):
		print ("Yeap")
	else:
		print ("Noap")
else:
	print("Somente palavras que contem caracteres de A-Z")
