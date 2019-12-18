#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Discente: Higor Santos de Jesus	RA: 2019129325
# Construção: Python3  	Entrada: Linguagem C

import ply.lex as lex

# keywords (palavras reservadas da linguagem c)
keywords = {
	'continue'	:	'CONTINUE',	# continue
	'break'		:	'BREAK',	# break

	'main'		:	'MAIN', 	# main
	'void'		:	'VOID',		# void
	'return'	:	'RETURN',	# return
	'printf'	:	'PRINTF',	# printf
	'scanf'		:	'SCANF',	# scanf
	
	'true'		:	'TRUE',		# true
	'false'		:	'FALSE',	# false

	'int'		:	'INT',		# int
	'float'		:	'FLOAT',	# float
	'boolean'	:	'BOOLEAN',	# boll
	'char'		:	'CHAR',

	'do'		:	'DO',		# do
	'if'		:	'IF',		# if
	'else'		:	'ELSE',		# else
	'for'		:	'FOR',		# for
	'while'		:	'WHILE'		# while

}

# tokens atribuidos a caracteres especiais e específicos
# os tokens são somados as palavras reservadas
tokens = list(keywords.values()) + [
'ID',			# ex:abc
'NUMERO_INT', 	# ex:0
'NUMERO_REAL',	# ex:0.00
'CONST_CHAR',	# ex:'a'
'CONST_STRING',	# ex:"abcd"

'ASPA_SIMPLES',	# '
'ASPA_DUPLA',	# " 

'MAIS',			# +
'MAIS_MAIS',	# ++
'MENOS',		# -
'MENOS_MENOS',	# --
'BARRA',		# /
'ASTERISCO',	# *
'ATRIBUICAO',	# =
'IGUAL',		# ==
'MOD',			# %
'AND',			# &&
'E_COMERCIAL',	# &
'OU',			# ||
'MENOR',		# <
'MAIOR',		# >
'MENOR_IGUAL',	# <=
'MAIOR_IGUAL',	# >=
'DIFERENTE',	# !=
'NEGACAO',		# !

'L_PARENTESE',	# (
'R_PARENTESE',	# )
'L_CHAVE',		# {
'R_CHAVE',		# }
'L_COCHETE',	# [
'R_COCHETE',	# ]
'PONTO_VIRGULA',# ;
'PONTO',		# .
'VIRGULA'		# ,
]

# Expressões regulares para os tokens
t_ASPA_SIMPLES		=	r'\''	# '
t_ASPA_DUPLA		=	r'\"'	# " 

t_MAIS				=	r'\+'	# +
t_MAIS_MAIS			= 	r'\+\+'	# ++
t_MENOS				=	r'-'	# -
t_MENOS_MENOS		=	r'--'	# --
t_BARRA				=	r'/'	# /
t_ASTERISCO			=	r'\*'	# *
t_ATRIBUICAO		=	r'='	# =
t_IGUAL				=	r'=='	# ==
t_MOD				=	r'%'	# %
t_AND				=	r'&&'	# &&
t_E_COMERCIAL		=	r'&'	# &
t_OU 				=	r'\|\|'	# ||
t_MENOR				=	r'<'	# <
t_MAIOR				=	r'>'	# >
t_MENOR_IGUAL		=	r'<='	# <=
t_MAIOR_IGUAL		=	r'>='	# >=
t_DIFERENTE 		= 	r'!='	# !=
t_NEGACAO			=	r'!'	# !

t_L_PARENTESE		=	r'\('	# (
t_R_PARENTESE		=	r'\)'	# )
t_L_CHAVE			=	r'\{'	# {
t_R_CHAVE			=	r'\}'	# }
t_L_COCHETE			=	r'\['	# [
t_R_COCHETE			=	r'\]'	# ]
t_PONTO_VIRGULA		=	r';'	# ;
t_PONTO 			=	r'\.'	# .
t_VIRGULA 			=	r','	# ,

# Verificar se é uma constante char entre aspas simples ''
def t_CONST_CHAR(t):
	r'\'(\n|.)?\''
	return t

# verificar se é uma string entre aspas duplas ""
def t_CONST_STRING(t):
	r'\"(\n|.)*?\"'
	return t

# Verificar se o número é real
def t_NUMERO_REAL(t):
    r'([0-9]*[.][0-9]+((E|e)[+|-]?[0-9]+)?) | ([0-9]+([.][0-9]+)?(E|e)[+|-]?[0-9]+)'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Valor real muito grande %d", t.value)
        t.value = 0
    return t

# Verificar se o número é inteiro
def t_NUMERO_INT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor inteiro muito grande %d", t.value)
        t.value = 0
    return t

# Ignora os comentários
def t_comment_multiline(t):
    r'((//.*)|(/\*(.|\n)*\*/))'
    pass

# Rastrear números de linhas
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

# Rastrear números de colunas
def find_column(input, token):
    last_cr = input.rfind('\n', 0, lex.lexer.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (lex.lexer.lexpos - last_cr) + 1
    return column

# Verificar se é um ID ou palavra reservada
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in keywords:
    	t.type = keywords[t.value]
    return t

# String do que deve ser ignorado (tab / quebra de linha / espaço)
t_ignore  = ' \t\n'

# Tratamento de erros (mensagem de caracter ilegal)
def t_error(t):
	print("Caracter Ilegal '%s'" % t.value[0])
	t.lexer.skip(1)

# Construção do léxico
lexer = lex.lex()

if __name__ == "__main__":
    lex.runmain(lexer)