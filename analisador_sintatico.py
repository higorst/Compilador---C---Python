#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Discente: Higor Santos de Jesus   RA: 2019129325
# Construção: Python3   Entrada: Linguagem C

import sys
import analisador_lexico
import ply.yacc as yacc

from impressao import *

# Get the token map
tokens = analisador_lexico.tokens

sys.path.insert(0, "../..")

if sys.version_info[0] >= 3:
    raw_input = input

precedence = (
  ('right', 'REDUCE'),
  ('right', 'ELSE'),
  ('left', 'OU'),
  ('left', 'AND'),
  ('left', 'IGUAL', 'DIFERENTE'),
  ('left', 'MAIOR', 'MAIOR_IGUAL', 'MENOR', 'MENOR_IGUAL'),
  ('left', 'MAIS', 'MENOS'),
  ('left', 'ASTERISCO', 'BARRA', 'MOD'),
  ('right', 'NEGACAO'),
  ('right', 'MAIS_MAIS', 'MENOS_MENOS'),
  ('right', 'ATRIBUICAO'),
  ('right', 'UASTERISCO', 'UMENOS', 'UMAIS', 'UNEGACAO', 'E_COMERCIAL'),
)

###########################################
# Definição para todo o bloco do código c #
###########################################
# Início do bloco main (principal)
def p_main(p):
  '''main : INT MAIN L_PARENTESE R_PARENTESE L_CHAVE stm RETURN expression PONTO_VIRGULA R_CHAVE'''
  p[0] = Main(p[6], p[8])
  pass

# opções gerais para conteúdo do main
def p_init_programa(p):
  '''stm : declaracao
         | equacao
         | condicional
         | estrutura_repeticao
         | mostrar
         | entrada
         | break
         | continue
         | bloco_stm
         | lambda'''
  p[0] = p[1]
  pass                              

def p_bloco_stm(p):
  '''bloco_stm : bloco stm'''
  p[0] = bloco_stm(p[1], p[2])

# lambda (palavra vazia)
def p_lambda(p):
  '''lambda : '''
  p[0] = lambda_()
  pass
    
# uso de parada (break)
def p_break(p):
  '''break : BREAK PONTO_VIRGULA stm'''
  p[0] = break_(stm=p[3])
  pass

# uso de continue
def p_continue(p):
  '''continue : CONTINUE PONTO_VIRGULA stm'''
  # p[0] = Continue(cont=p[1], ponto_virgula=p[2], stm=p[3])
  p[0] = continue_(stm=p[3])
  pass

# Tipo de declaração
def p_tipo(p):
  '''tipo : tipo_VOID
          | tipo_BOOLEAN
          | tipo_CHAR
          | tipo_INT
          | tipo_FLOAT'''
  # p[0] = Tipo(tipo=p[1])
  p[0] = p[1]
  pass

def p_tipo_VOID(p):
  '''tipo_VOID : VOID'''
  p[0] = tipo_VOID(p[1])

def p_tipo_BOOLEAN(p):
  '''tipo_BOOLEAN : BOOLEAN'''
  p[0] = tipo_BOOLEAN(p[1])

def p_tipo_CHAR(p):
  '''tipo_CHAR : CHAR'''
  p[0] = tipo_CHAR(p[1])

def p_tipo_INT(p):
  '''tipo_INT : INT'''
  p[0] = tipo_INT(p[1])

def p_tipo_FLOAT(p):
  '''tipo_FLOAT : FLOAT'''
  p[0] = tipo_FLOAT(p[1])

# Bloco entre chaves
def p_bloco(p):
  '''bloco : L_CHAVE stm R_CHAVE'''
  # p[0] = Bloco(l_chave=p[1], stm=p[2], r_chave=p[3])
  p[0] = bloco(p[2])
  pass

# asterisco para ponteiro
def p_pointer(p):
  '''pointer : pointer ASTERISCO
             | lambda'''
  if len(p) == 3:
    p[0] = pointer(pointer=p[1])
  # else:
  #   p[0] = Pointer(pointer=p[1])
  pass

# Declaração de variável, ponteiro ou matriz
def p_declaracao(p):
  '''declaracao : tipo pointer ID PONTO_VIRGULA stm
                | tipo pointer ID ATRIBUICAO expression PONTO_VIRGULA stm
                | tipo pointer ID L_COCHETE arg R_COCHETE PONTO_VIRGULA stm
                | tipo pointer ID L_COCHETE arg R_COCHETE ATRIBUICAO atribuicao_mat PONTO_VIRGULA stm
                | tipo pointer ID L_COCHETE arg R_COCHETE L_COCHETE arg R_COCHETE more_arg PONTO_VIRGULA stm
                | tipo pointer ID L_COCHETE arg R_COCHETE L_COCHETE arg R_COCHETE more_arg ATRIBUICAO L_CHAVE atribuicao_mat R_CHAVE PONTO_VIRGULA stm'''
  if len(p) == 6:
    p[0] = declaracao1(tipo=p[1], pointer=p[2], id_=p[3], stm=p[5])
  elif len(p) == 8:
    p[0] = declaracao2(tipo=p[1], pointer=p[2], id_=p[3], expression=p[5], stm=p[7])
  elif len(p) == 9:
    p[0] = declaracao3(tipo=p[1], pointer=p[2], id_=p[3], arg=p[5], stm=p[8])
  elif len(p) == 11:
    p[0] = declaracao4(tipo=p[1], pointer=p[2], id_=p[3], arg=p[5], atribuicao_mat=p[8], stm=p[10])
  elif len(p) == 13:
    p[0] = declaracao5(tipo=p[1], pointer=p[2], id_=p[3], arg1=p[5], arg2=p[8], more_arg=p[10], stm=p[12])
  else:
    p[0] = declaracao6(tipo=p[1], pointer=p[2], id_=p[3], arg1=p[5], arg2=p[8], more_arg=p[10], atribuicao_mat=p[13], stm=p[16])
  pass


# atribuição de expressões separadas por vírgula dentro de uma estrutura de {}
def p_atribuicao_vet(p):
  '''atribuicao_vet : expression VIRGULA atribuicao_vet
                    | expression'''
  if len(p) == 4:
    p[0] = atribuicao_vet1(expression=p[1], atribuicao_vet=p[3])
  else:
    p[0] = atribuicao_vet2(expression=p[1])
  pass

# criação de uma estrutura de chave para definição de valores para um ventor ou para grupos da matriz
def p_atribuicao_mat(p):
  '''atribuicao_mat : L_CHAVE atribuicao_vet R_CHAVE VIRGULA atribuicao_mat
                    | L_CHAVE atribuicao_vet R_CHAVE'''
  if len(p) == 6:
    p[0] = atribuicao_mat1(atribuicao_vet=p[2], atribuicao_mat=p[5])
  else:
    p[0] = atribuicao_mat2(atribuicao_vet=p[2])
  pass

# chamada para equações sem declaração
def p_equacao(p):
  '''equacao : pointer ID L_COCHETE arg R_COCHETE ATRIBUICAO expression PONTO_VIRGULA stm
             | pointer ID L_COCHETE arg R_COCHETE L_COCHETE arg R_COCHETE more_arg ATRIBUICAO expression PONTO_VIRGULA stm
             | pointer ID ATRIBUICAO expression PONTO_VIRGULA stm'''
  if len(p) == 10:
    p[0] = equacao1(pointer=p[1], id_=p[2], arg=p[4], expression=p[7], stm=p[9])
  elif len(p) == 14:
    p[0] = equacao2(pointer=p[1], id_=p[2], arg1=p[4], arg2=p[7], more_arg=p[9], expression=p[11], stm=p[13])
  else:
    p[0] = equacao3(pointer=p[1], id_=p[2], expression=p[4], stm=p[6])
  pass

# argumento de definição para vetor e matriz
def p_arg(p):
  '''arg : expression
         | lambda'''
  p[0] = arg(expression=p[1])
  pass

# permite infinitos [] para matriz
def p_more_arg(p):
  '''more_arg : more_arg L_COCHETE arg R_COCHETE
              | lambda'''
  if len(p) == 5:
    p[0] = more_arg(more_arg=p[1], arg=p[3])
  # else:
  #   p[0] = More_arg(more_arg=p[1])
  pass

# conteúdo para a saída (printf)
def p_mostrar(p):
  '''mostrar : mostrar1
             | mostrar2'''
  # p[0] = Mostrar(printf=p[1], l_parentese=p[2], conteudo=p[3], r_parentese=p[4], ponto_virgula=p[5], stm=p[6])
  p[0] = p[1]
  pass

def p_mostrar1(p):
  '''mostrar1 : PRINTF L_PARENTESE CONST_STRING R_PARENTESE PONTO_VIRGULA stm'''
  p[0] = mostrar1(p[3], p[6])

def p_mostrar2(p):
  '''mostrar2 : PRINTF L_PARENTESE expression_mostrar R_PARENTESE PONTO_VIRGULA stm'''
  p[0] = mostrar2(p[3], p[6])

# expression_mostrar
def p_expression_mostrar(p):
  '''expression_mostrar : CONST_STRING VIRGULA expression expression_mostrar
                        | VIRGULA expression
                        | lambda'''
  if len(p) == 5:
    p[0] = expression_mostrar1(const=p[1], expression=p[3], expression_mostrar=p[4])
  elif len(p) == 3:
    p[0] = expression_mostrar2(expression=p[2])
  # else:
  #   p[0] = Expression_mostrar(expression=p[1])
  pass

# chamada para entrada de dados (scanf)
def p_entrada(p):
  '''entrada : SCANF L_PARENTESE expression_entrada R_PARENTESE PONTO_VIRGULA stm'''
  # p[0] = Entrada(scanf=p[1], l_parentese=p[2], expression_entrada=p[3], r_parentese=p[4], ponto_virgula=p[5], stm=p[6])
  p[0] = entrada(p[3], p[6])
  pass

# conteúdo para a entrada scanf
def p_expression_entrada(p):
  '''expression_entrada : CONST_STRING VIRGULA E_COMERCIAL ID expression_entrada
                        | VIRGULA E_COMERCIAL ID expression_entrada
                        | lambda'''
  if len(p) == 6:
    p[0] = expression_entrada1(const=p[1], id_=p[4], expression_entrada=p[5])
  elif len(p) == 5:
    p[0] = expression_entrada2(id_=p[3], expression_entrada=p[4])
  # else:
  #   p[0] = Expression_entrada(expression_entrada=p[1])
  pass

def p_exp_and(p):
  '''exp_and : exp AND exp'''
  p[0] = exp_and(exp1=p[1], exp2=p[3])

def p_exp_ou(p):
  '''exp_ou : exp OU exp'''
  p[0] = exp_ou(exp1=p[1], exp2=p[3])

def p_exp_menor(p):
  '''exp_menor : exp MENOR exp'''
  p[0] = exp_menor(exp1=p[1], exp2=p[3])

def p_exp_maior(p):
  '''exp_maior : exp MAIOR exp'''
  p[0] = exp_maior(exp1=p[1], exp2=p[3])

def p_exp_menor_igual(p):
  '''exp_menor_igual : exp MENOR_IGUAL exp'''
  p[0] = exp_menor_igual(exp1=p[1], exp2=p[3])

def p_exp_maior_igual(p):
  '''exp_maior_igual : exp MAIOR_IGUAL exp'''
  p[0] = exp_maior_igual(exp1=p[1], exp2=p[3])

def p_exp_igual(p):
  '''exp_igual : exp IGUAL exp'''
  p[0] = exp_igual(exp1=p[1], exp2=p[3])

def p_exp_diferente(p):
  '''exp_diferente : exp DIFERENTE exp'''
  p[0] = exp_diferente(exp1=p[1], exp2=p[3])

def p_exp_menos(p):
  '''exp_menos : exp MENOS exp'''
  p[0] = exp_menos(exp1=p[1], exp2=p[3])

def p_exp_mais(p):
  '''exp_mais : exp MAIS exp'''
  p[0] = exp_mais(exp1=p[1], exp2=p[3])

def p_exp_asterisco(p):
  '''exp_asterisco : exp ASTERISCO exp'''
  p[0] = exp_asterisco(exp1=p[1], exp2=p[3])

def p_exp_barra(p):
  '''exp_barra : exp BARRA exp'''
  p[0] = exp_barra(exp1=p[1], exp2=p[3])

def p_exp_mod(p):
  '''exp_mod : exp MOD exp'''
  p[0] = exp_mod(exp1=p[1], exp2=p[3])

def p_menos_exp(p):
  '''menos_exp : MENOS exp %prec UMENOS'''
  p[0] = menos_exp(p[2])

def p_mais_exp(p):
  '''mais_exp : MAIS exp %prec UMAIS'''
  p[0] = mais_exp(p[2])

def p_asterisco_exp(p):
  '''asterisco_exp : ASTERISCO exp %prec UASTERISCO'''
  p[0] = asterisco_exp(p[2])

def p_negacao_exp(p):
  '''negacao_exp : NEGACAO exp %prec UNEGACAO'''
  p[0] = negacao_exp(p[2])

def p_e_comercial_exp(p):
  '''e_comercial_exp : E_COMERCIAL exp'''
  p[0] = e_comercial_exp(p[2])

def p_const_virgula(p):
  '''const_virgula : VIRGULA'''
  p[0] = const_virgula(p[1])

def p_const_ponto(p):
  '''const_ponto : PONTO'''
  p[0] = const_ponto(p[1])

def p_const_numero_real(p):
  '''const_numero_real : NUMERO_REAL'''
  p[0] = const_numero_real(p[1])

def p_const_numero_int(p):
  '''const_numero_int : NUMERO_INT'''
  p[0] = const_numero_int(p[1])

def p_const_char(p):
  '''const_char : CONST_CHAR'''
  p[0] = const_char(p[1])

def p_const_string(p):
  '''const_string : CONST_STRING'''
  p[0] = const_string(p[1])

def p_mais_mais(p):
  '''mais_mais : MAIS_MAIS'''
  p[0] = mais_mais(p[1])

def p_menos_menos(p):
  '''menos_menos : MENOS_MENOS'''
  p[0] = menos_menos(p[1])

def p_id(p):
  '''id : ID'''
  p[0] = id(p[1])

def p_true(p):
  '''true : TRUE'''
  p[0] = true(p[1])

def p_false(p):
  '''false : FALSE'''
  p[0] = false(p[1])

def p_id_atribuicao_exp(p):
  '''id_atribuicao_exp : ID ATRIBUICAO exp'''  
  p[0] = id_atribuicao_exp(p[1], p[3])

def p_id_cochete_exp(p):
  '''id_cochete_exp : ID L_COCHETE exp R_COCHETE'''
  p[0] = id_cochete_exp(p[1], p[3])

def p_parentese_exp(p):
  '''parentese_exp : L_PARENTESE exp R_PARENTESE'''
  p[0] = parentese_exp(p[2])

def p_chave_exp(p):
  '''chave_exp : L_CHAVE exp R_CHAVE'''
  p[0] = chave_exp(p[2])

# definição de tipo de expressões
def p_exp(p):
  '''exp  : exp_and
          | exp_ou
          | exp_menor
          | exp_maior
          | exp_menor_igual
          | exp_maior_igual
          | exp_igual
          | exp_diferente
          | exp_menos
          | exp_mais
          | exp_asterisco
          | exp_barra
          | exp_mod
          | menos_exp
          | mais_exp
          | asterisco_exp
          | negacao_exp
          | e_comercial_exp
          | const_virgula
          | const_ponto
          | const_numero_real
          | const_numero_int
          | const_char
          | const_string
          | mais_mais
          | menos_menos
          | id
          | true
          | false
          | id_atribuicao_exp
          | id_cochete_exp
          | parentese_exp
          | chave_exp'''
  # if len(p) == 5:
  #   p[0] = Exp(id_=p[1], l=p[2], exp1=p[3], r=p[4])
  # elif len(p) == 4:
  #   p[0] = Exp(exp1=p[1], op=p[2], exp2=p[3])
  # elif len(p) == 3:
  #   p[0] = Exp(op=p[1], exp2=p[2])
  # else:
  #   p[0] = Exp(const=p[1])
  p[0] = p[1]
  pass

# chamada para expressões
def p_expression(p):
  '''expression : exp
                | extras
                | aspa_dupla_exp
                | aspa_simples_exp'''
  # if len(p) == 4:
  #   p[0] = Expression(aspa1=p[1], exp1=p[2], aspa2=p[3])
  # else:
  #   p[0] = Expression(exp1=p[1])
  p[0] = p[1]
  pass

def p_aspa_dupla_exp(p):
  '''aspa_dupla_exp : ASPA_DUPLA exp ASPA_DUPLA'''
  p[0] = aspa_dupla_exp(p[2])

def p_aspa_simples_exp(p):
  '''aspa_simples_exp : ASPA_SIMPLES exp ASPA_SIMPLES'''
  p[0] = aspa_simples_exp(p[2])

# extras ( permite uma expressão com o parse de tipo de variáveis )
def p_extras(p):
  '''extras : L_PARENTESE tipo R_PARENTESE exp'''
  # p[0] = Extras(l_parentese=p[1], tipo=p[2], r_parentese=p[3], exp1=p[4])
  p[0] = extras(tipo=p[2], exp=p[4])
  pass

# chamada para condicional
def p_condicional(p):
  '''condicional : IF L_PARENTESE expression R_PARENTESE stm %prec REDUCE
                 | IF L_PARENTESE expression R_PARENTESE stm ELSE stm'''
  if len(p) == 6:
    p[0] = condicional1(expression=p[3], stm=p[5])
  else:
    p[0] = condicional2(expression=p[3], stm1=p[5], stm2=p[7])
  pass

# chamada para as estruturas de repetição
def p_estrutura_repeticao(p):
  '''estrutura_repeticao : for
                         | while
                         | do_while'''
  # p[0] = Estrutura_repeticao(estrutura=p[1], stm=p[2])
  p[0] = p[1]
  pass

# estrutura de repetição for
def p_for(p):
  '''for : FOR L_PARENTESE tipo ID ATRIBUICAO expression PONTO_VIRGULA arg PONTO_VIRGULA arg R_PARENTESE bloco stm
         | FOR L_PARENTESE arg PONTO_VIRGULA arg PONTO_VIRGULA arg R_PARENTESE bloco stm'''
  if len(p) == 14:
    p[0] = for1(tipo=p[3], id_=p[4], expression=p[6], arg1=p[8], arg2=p[10], bloco=p[12], stm=p[13])
  else:
    p[0] = for2(arg1=p[3], arg2=p[5], arg3=p[7], bloco=p[9], stm=p[10])
  pass

# estrutura de repetição while
def p_while(p):
  '''while : WHILE L_PARENTESE expression R_PARENTESE bloco stm'''
  # p[0] = While(while_=p[1], l_parentese=p[2], expression=p[3], r_parentese=p[4], bloco=p[5])
  p[0] = while_(expression=p[3], bloco=p[5], stm=p[6])
  pass

# estrutura de repetição do-while
def p_do_while(p):
  '''do_while : DO bloco WHILE L_PARENTESE expression R_PARENTESE PONTO_VIRGULA stm'''
  # p[0] = Do_while(do=p[1], bloco=p[2], while_=p[3], l_parentese=p[4], expression=p[5], r_parentese=p[6], ponto_virgula=p[7])
  p[0] = do_while(bloco=p[2], expression=p[5], stm=p[8])
  pass

#########################################################################
# Função de erro para não reconhecimento
def p_error(p):
    last_cr = p.lexer.lexdata.rfind('\n', 0, p.lexer.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (p.lexer.lexpos - last_cr) + 1
    if p:
        # print("Erro de sintaxe em '{0}' na linha '{1}' e coluna '{2}'".format(p.value, p.lexer.lineno, column))
        print("Erro de sintaxe em '{0}'".format(p.value))
    else:
        print("Erro de sintaxe para EOF")
    pass

yacc.yacc()

def main(s):
  impressao = Impressao()
  t = yacc.parse(s).accept(impressao)