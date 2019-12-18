from pprint import pprint
import sys
import analisador_sintatico as syntatic


def main():
	print()
	arqText = sys.argv[1]
	arquivo = open(arqText, 'r')
	s = arquivo.read()
	arquivo.close()
	t = syntatic.main(s)

	print()
	arquivo = open("resultado_semantico.txt", "r")
	if arquivo.read() == "True":
		print("GERADOR DE CÓDIGO >> LIBERADO!")
	else:
		print("GERADOR DE CÓDIGO >> NÃO LIBERADO!")
	arquivo.close()
	print()

main()