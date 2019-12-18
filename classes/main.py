import visitor
from classes.nodo import Nodo

class Main(object):

	def __init__(self, stm, expression):
		self.stm = stm
		self.expression = expression

	def avalia(self):
		return self.stm.avalia()

	def accept(self, visitor):
		visitor.visita_main(self)

class bloco_stm(Nodo):

	def __init__(self, bloco, stm):
		self.bloco = bloco
		self.stm = stm

	def avalia(self):
		return self.stm.avalia()

	def accept(self, visitor):
		visitor.visita_bloco_stm(self)

class lambda_(Nodo):

	def __init__(self): pass

	def avalia(self): pass

	def accept(self, visitor): pass

class break_(object):

	def __init__(self, stm):
		self.stm = stm

	def avalia(self):
		return "break"

	def accept(self, visitor):
		if self.stm:
			visitor.visita_break(self)


class continue_(object):

	def __init__(self, stm):
		self.stm = stm

	def avalia(self):
		return "continue"

	def accept(self, visitor):
		visitor.visita_continue(self)


class tipo_VOID(Nodo):

	def __init__(self, void):
		self.type = "void"
		self.void = void

	def avalia(self):
		return self.void

	def accept(self, visitor):
		visitor.visita_tipo(self)

class tipo_BOOLEAN(Nodo):

	def __init__(self, boolean):
		self.type = "boolean"
		self.boolean = boolean

	def avalia(self):
	    return self.boolean

	def accept(self, visitor):
	    visitor.visita_tipo(self)

class tipo_CHAR(Nodo):

	def __init__(self, char):
		self.type = "char"
		self.char = char

	def avalia(self):
		return self.char

	def accept(self, visitor):
		visitor.visita_tipo(self)

class tipo_INT(Nodo):

	def __init__(self, int_):
		self.type = "int"
		self.int_ = int_

	def avalia(self):
		return self.int_

	def accept(self, visitor):
		visitor.visita_tipo(self)

class tipo_FLOAT(object):

	def __init__(self, float_):
		self.type = "float"
		self.float_ = float_

	def avalia(self):
		return self.float_

	def accept(self, visitor):
		visitor.visita_tipo(self)

class bloco(object):

	def __init__(self, stm):
		self.stm = stm

	def avalia(self):
		return self.stm

	def accept(self, visitor):
		visitor.visita_bloco(self)

class pointer(object):

	def __init__(self, pointer):
		self.pointer = pointer

	def avalia(self):
		return self.pointer

	def accept(self, visitor):
		visitor.visita_pointer(self)

# DECLARACAO

class declaracao1(object):

	def __init__(self, tipo, pointer, id_, stm):
		self.tipo = tipo
		self.pointer = pointer
		self.id_ = id_
		self.stm = stm

	def avalia(self):
		return self.stm

	def accept(self, visitor):
	    visitor.visita_declaracao1(self)

class declaracao2(object):

	def __init__(self, tipo, pointer, id_, expression, stm):
		self.tipo = tipo
		self.pointer = pointer
		self.id_ = id_
		self.expression = expression
		self.stm = stm

	def avalia(self):
		return self.stm

	def accept(self, visitor):
	    visitor.visita_declaracao2(self)

class declaracao3(object):

	def __init__(self, tipo, pointer, id_, arg, stm):
		self.tipo = tipo
		self.pointer = pointer
		self.id_ = id_
		self.arg = arg
		self.stm = stm

	def avalia(self):
		return self.stm

	def accept(self, visitor):
	    visitor.visita_declaracao3(self)

class declaracao4(object):

	def __init__(self, tipo, pointer, id_, arg, atribuicao_mat, stm):
		self.tipo = tipo
		self.pointer = pointer
		self.id_ = id_
		self.arg = arg
		self.atribuicao_mat = atribuicao_mat
		self.stm = stm

	def avalia(self):
		return self.stm

	def accept(self, visitor):
	    visitor.visita_declaracao4(self)

class declaracao5(object):

	def __init__(self, tipo, pointer, id_, arg1, arg2, more_arg, stm):
		self.tipo = tipo
		self.pointer = pointer
		self.id_ = id_
		self.arg1 = arg1
		self.arg2 = arg2
		self.more_arg = more_arg
		self.stm = stm

	def avalia(self):
		return self.stm

	def accept(self, visitor):
	    visitor.visita_declaracao5(self)

class declaracao6(object):

	def __init__(self, tipo, pointer, id_, arg1, arg2, more_arg, atribuicao_mat, stm):
		self.tipo = tipo
		self.pointer = pointer
		self.id_ = id_
		self.arg1 = arg1
		self.arg2 = arg2
		self.more_arg = more_arg
		self.atribuicao_mat = atribuicao_mat
		self.stm = stm

	def avalia(self):
		return self.stm

	def accept(self, visitor):
	    visitor.visita_declaracao6(self)

class atribuicao_vet1(object):

	def __init__(self, expression, atribuicao_vet):
		self.expression = expression
		self.atribuicao_vet = atribuicao_vet

	def avalia(self):
		return self.expression

	def accept(self, visitor):
	    visitor.visita_atribuicao_vet1(self)

class atribuicao_vet2(object):

	def __init__(self, expression):
		self.expression = expression

	def avalia(self):
		return self.expression

	def accept(self, visitor):
	    visitor.visita_atribuicao_vet2(self)

class atribuicao_mat1(object):

	def __init__(self, atribuicao_vet, atribuicao_mat):
		self.atribuicao_vet = atribuicao_vet
		self.atribuicao_mat = atribuicao_mat

	def avalia(self):
		return self.atribuicao_vet

	def accept(self, visitor):
	    visitor.visita_atribuicao_mat1(self)

class atribuicao_mat2(object):

	def __init__(self, atribuicao_vet):
		self.atribuicao_vet = atribuicao_vet

	def avalia(self):
		return self.atribuicao_vet

	def accept(self, visitor):
	    visitor.visita_atribuicao_mat2(self)

# EQUACAO
class equacao1(object):

	def __init__(self, pointer, id_, arg, expression, stm):
		self.pointer = pointer
		self.id_ = id_
		self.arg = arg
		self.expression = expression
		self.stm = stm

	def avalia(self):
		return self.stm

	def accept(self, visitor):
	    visitor.visita_equacao1(self)

class equacao2(object):

	def __init__(self, pointer, id_, arg1, arg2, more_arg, expression, stm):
		self.pointer = pointer
		self.id_ = id_
		self.arg1 = arg1
		self.arg2 = arg2
		self.more_arg = more_arg
		self.expression = expression
		self.stm = stm

	def avalia(self):
		return self.stm

	def accept(self, visitor):
	    visitor.visita_equacao2(self)

class equacao3(object):

	def __init__(self, pointer, id_, expression, stm):
		self.pointer = pointer
		self.id_ = id_
		self.expression = expression
		self.stm = stm

	def avalia(self):
		return self.stm

	def accept(self, visitor):
	    visitor.visita_equacao3(self)

class arg(object):

	def __init__(self, expression):
		self.expression = expression

	def avalia(self):
		return self.expression.avalia()

	def accept(self, visitor):
		visitor.visita_arg(self)

class more_arg(object):

	def __init__(self, more_arg, arg):
		self.more_arg = more_arg
		self.arg = arg

	def avalia(self):
		return self.arg

	def accept(self, visitor):
		visitor.visita_more_arg(self)

class mostrar1(object):

	def __init__(self, const, stm):
		self.const = const
		self.stm = stm

	def avalia(self):
		return self.const

	def accept(self, visitor):
		visitor.visita_mostrar1(self)

class mostrar2(object):

	def __init__(self, expression_mostrar, stm):
		self.expression_mostrar = expression_mostrar
		self.stm = stm

	def avalia(self):
		return self.expression_mostrar.avalia()

	def accept(self, visitor):
		visitor.visita_mostrar2(self)

class expression_mostrar1(object):

	def __init__(self, const, expression, expression_mostrar):
		self.const = const
		self.expression = expression
		self.expression_mostrar = expression_mostrar

	def avalia(self):
		return self.expression

	def accept(self, visitor):
		visitor.visita_expression_mostrar1(self)

class expression_mostrar2(object):

	def __init__(self, expression):
		self.expression = expression

	def avalia(self):
		return self.expression

	def accept(self, visitor):
		visitor.visita_expression_mostrar2(self)

class entrada(object):

	def __init__(self, expression_entrada, stm):
		self.expression_entrada = expression_entrada
		self.stm = stm

	def avalia(self):
		return self.expression_entrada.avalia()

	def accept(self, visitor):
		visitor.visita_entrada(self)

class expression_entrada1(object):

	def __init__(self, const, id_, expression_entrada):
		self.const = const
		self.id_ = id_
		self.expression_entrada = expression_entrada

	def avalia(self):
		return self.id_

	def accept(self, visitor):
		visitor.visita_expression_entrada1(self)

class expression_entrada2(object):

	def __init__(self, id_, expression_entrada):
		self.id_ = id_
		self.expression_entrada = expression_entrada

	def avalia(self):
		return self.id_

	def accept(self, visitor):
		visitor.visita_expression_entrada2(self)

class exp_and(object):

	def __init__(self, exp1, exp2):
		self.type = "&&"
		self.exp1 = exp1
		self.exp2 = exp2

	def avalia(self):
		exp_esq = self.exp1.avalia()
		exp_dir = self.exp2.avalia()
		if isinstance(exp_esq, str) or isinstance(exp_dir, str) and not isinstance(type(exp_esq), type(exp_dir)):
			return "str"
		elif isinstance(exp_esq, bool) or isinstance(exp_dir, bool) and not isinstance(type(exp_esq), type(exp_dir)):
			return "true"
		else:
			return exp_esq and exp_dir

	def accept(self, visitor):
		visitor.visita_bino_exp(self)

class exp_ou(object):

	def __init__(self, exp1, exp2):
		self.type = "||"
		self.exp1 = exp1
		self.exp2 = exp2

	def avalia(self):
		exp_esq = self.exp1.avalia()
		exp_dir = self.exp2.avalia()
		if isinstance(exp_esq, str) or isinstance(exp_dir, str) and not isinstance(type(exp_esq), type(exp_dir)):
			return "str"
		elif isinstance(exp_esq, bool) or isinstance(exp_dir, bool) and not isinstance(type(exp_esq), type(exp_dir)):
			return "true"
		else:
			return exp_esq or exp_dir

	def accept(self, visitor):
		visitor.visita_bino_exp(self)

class exp_menor(object):

	def __init__(self, exp1, exp2):
		self.type = "<"
		self.exp1 = exp1
		self.exp2 = exp2

	def avalia(self):
		exp_esq = self.exp1.avalia()
		exp_dir = self.exp2.avalia()
		if isinstance(exp_esq, str) or isinstance(exp_dir, str) and not isinstance(type(exp_esq), type(exp_dir)):
			return "str"
		elif isinstance(exp_esq, bool) or isinstance(exp_dir, bool) and not isinstance(type(exp_esq), type(exp_dir)):
			return "true"
		else:
			return exp_esq < exp_dir

	def accept(self, visitor):
		visitor.visita_bino_exp(self)

class exp_maior(object):

	def __init__(self, exp1, exp2):
		self.type = ">"
		self.exp1 = exp1
		self.exp2 = exp2

	def avalia(self):
		exp_esq = self.exp1.avalia()
		exp_dir = self.exp2.avalia()
		if isinstance(exp_esq, str) or isinstance(exp_dir, str) and not isinstance(type(exp_esq), type(exp_dir)):
			return "str"
		elif isinstance(exp_esq, bool) or isinstance(exp_dir, bool) and not isinstance(type(exp_esq), type(exp_dir)):
			return "true"
		else:
			return exp_esq > exp_dir

	def accept(self, visitor):
		visitor.visita_bino_exp(self)

class exp_menor_igual(object):

	def __init__(self, exp1, exp2):
		self.type = "<="
		self.exp1 = exp1
		self.exp2 = exp2

	def avalia(self):
		exp_esq = self.exp1.avalia()
		exp_dir = self.exp2.avalia()
		if isinstance(exp_esq, str) or isinstance(exp_dir, str) and not isinstance(type(exp_esq), type(exp_dir)):
			return "str"
		elif isinstance(exp_esq, bool) or isinstance(exp_dir, bool) and not isinstance(type(exp_esq), type(exp_dir)):
			return "true"
		else:
			return exp_esq <= exp_dir

	def accept(self, visitor):
		visitor.visita_bino_exp(self)

class exp_maior_igual(object):

	def __init__(self, exp1, exp2):
		self.type = ">="
		self.exp1 = exp1
		self.exp2 = exp2

	def avalia(self):
		exp_esq = self.exp1.avalia()
		exp_dir = self.exp2.avalia()
		if isinstance(exp_esq, str) or isinstance(exp_dir, str) and not isinstance(type(exp_esq), type(exp_dir)):
			return "str"
		elif isinstance(exp_esq, bool) or isinstance(exp_dir, bool) and not isinstance(type(exp_esq), type(exp_dir)):
			return "true"
		else:
			return exp_esq >= exp_dir

	def accept(self, visitor):
		visitor.visita_bino_exp(self)

class exp_igual(object):

	def __init__(self, exp1, exp2):
		self.type = "=="
		self.exp1 = exp1
		self.exp2 = exp2

	def avalia(self):
		exp_esq = self.exp1.avalia()
		exp_dir = self.exp2.avalia()
		if isinstance(exp_esq, str) or isinstance(exp_dir, str) and not isinstance(type(exp_esq), type(exp_dir)):
			return "str"
		elif isinstance(exp_esq, bool) or isinstance(exp_dir, bool) and not isinstance(type(exp_esq), type(exp_dir)):
			return "true"
		else:
			return exp_esq == exp_dir

	def accept(self, visitor):
		visitor.visita_bino_exp(self)

class exp_diferente(object):

	def __init__(self, exp1, exp2):
		self.type = "!="
		self.exp1 = exp1
		self.exp2 = exp2

	def avalia(self):
		exp_esq = self.exp1.avalia()
		exp_dir = self.exp2.avalia()
		if isinstance(exp_esq, str) or isinstance(exp_dir, str) and not isinstance(type(exp_esq), type(exp_dir)):
			return "str"
		elif isinstance(exp_esq, bool) or isinstance(exp_dir, bool) and not isinstance(type(exp_esq), type(exp_dir)):
			return "true"
		else:
			return exp_esq != exp_dir

	def accept(self, visitor):
		visitor.visita_bino_exp(self)

class exp_menos(object):

	def __init__(self, exp1, exp2):
		self.type = "-"
		self.exp1 = exp1
		self.exp2 = exp2

	def avalia(self):
		exp_esq = self.exp1.avalia()
		exp_dir = self.exp2.avalia()
		if isinstance(exp_esq, str) or isinstance(exp_dir, str) and not isinstance(type(exp_esq), type(exp_dir)):
			return "str"
		elif isinstance(exp_esq, bool) or isinstance(exp_dir, bool) and not isinstance(type(exp_esq), type(exp_dir)):
			return "true"
		else:
			return exp_esq - exp_dir

	def accept(self, visitor):
		visitor.visita_bino_exp(self)

class exp_mais(object):

	def __init__(self, exp1, exp2):
		self.type = "+"
		self.exp1 = exp1
		self.exp2 = exp2

	def avalia(self):
		exp_esq = self.exp1.avalia()
		exp_dir = self.exp2.avalia()
		if isinstance(exp_esq, str) or isinstance(exp_dir, str) and not isinstance(type(exp_esq), type(exp_dir)):
			return "str"
		elif isinstance(exp_esq, bool) or isinstance(exp_dir, bool) and not isinstance(type(exp_esq), type(exp_dir)):
			return "true"
		else:
			return exp_esq + exp_dir

	def accept(self, visitor):
		visitor.visita_bino_exp(self)

class exp_asterisco(object):

	def __init__(self, exp1, exp2):
		self.type = "*"
		self.exp1 = exp1
		self.exp2 = exp2

	def avalia(self):
		exp_esq = self.exp1.avalia()
		exp_dir = self.exp2.avalia()
		if isinstance(exp_esq, str) or isinstance(exp_dir, str) and not isinstance(type(exp_esq), type(exp_dir)):
			return "str"
		elif isinstance(exp_esq, bool) or isinstance(exp_dir, bool) and not isinstance(type(exp_esq), type(exp_dir)):
			return "true"
		else:
			return exp_esq * exp_dir

	def accept(self, visitor):
		visitor.visita_bino_exp(self)

class exp_barra(object):

	def __init__(self, exp1, exp2):
		self.type = "/"
		self.exp1 = exp1
		self.exp2 = exp2

	def avalia(self):
		exp_esq = self.exp1.avalia()
		exp_dir = self.exp2.avalia()
		if isinstance(exp_esq, str) or isinstance(exp_dir, str) and not isinstance(type(exp_esq), type(exp_dir)):
			return "str"
		elif isinstance(exp_esq, bool) or isinstance(exp_dir, bool) and not isinstance(type(exp_esq), type(exp_dir)):
			return "true"
		else:
			return exp_esq / exp_dir

	def accept(self, visitor):
		visitor.visita_bino_exp(self)

class exp_mod(object):

	def __init__(self, exp1, exp2):
		self.type = "%"
		self.exp1 = exp1
		self.exp2 = exp2

	def avalia(self):
		exp_esq = self.exp1.avalia()
		exp_dir = self.exp2.avalia()
		if isinstance(exp_esq, str) or isinstance(exp_dir, str) and not isinstance(type(exp_esq), type(exp_dir)):
			return "str"
		elif isinstance(exp_esq, bool) or isinstance(exp_dir, bool) and not isinstance(type(exp_esq), type(exp_dir)):
			return "true"
		else:
			return exp_esq % exp_dir

	def accept(self, visitor):
		visitor.visita_bino_exp(self)

class menos_exp(object):

	def __init__(self, exp):
		self.type = "-"
		self.exp = exp

	def avalia(self):
		try:
			return self.exp.avalia()*(-1)
		except:
			return self.exp.avalia()

	def accept(self, visitor):
		visitor.visita_uno_exp(self)

class mais_exp(object):

	def __init__(self, exp):
		self.type = "+"
		self.exp = exp

	def avalia(self):
		return self.exp.avalia()

	def accept(self, visitor):
		visitor.visita_uno_exp(self)

class asterisco_exp(object):

	def __init__(self, exp):
		self.type = "*"
		self.exp = exp

	def avalia(self):
		return self.exp.avalia()

	def accept(self, visitor):
		visitor.visita_uno_exp(self)

class negacao_exp(object):

	def __init__(self, exp):
		self.type = "!"
		self.exp = exp

	def avalia(self):
		return not self.exp.avalia()

	def accept(self, visitor):
		visitor.visita_uno_exp(self)

class e_comercial_exp(object):

	def __init__(self, exp):
		self.type = "&"
		self.exp = exp

	def avalia(self):
		return self.exp.avalia()

	def accept(self, visitor):
		visitor.visita_uno_exp(self)

# CONSTANTES
class const_virgula(Nodo):

	def __init__(self, virgula):
		self.type = ","
		self.virgula = virgula

	def avalia(self):
		return self.virgula

	def accept(self, visitor):
		visitor.visita_const(self)

class const_ponto(Nodo):

	def __init__(self, ponto):
		self.type = "."
		self.ponto = ponto

	def avalia(self):
		return self.ponto

	def accept(self, visitor):
		visitor.visita_const(self)

class const_numero_real(Nodo):

	def __init__(self, numero_real):
		self.numero_real = numero_real

	def avalia(self):
		return self.numero_real

	def accept(self, visitor):
		visitor.visita_const_numero_real(self)

class const_numero_int(Nodo):

	def __init__(self, numero_int):
		self.numero_int = numero_int

	def avalia(self):
		return self.numero_int

	def accept(self, visitor):
		visitor.visita_const_numero_int(self)

class const_char(Nodo):

	def __init__(self, const_char):
		self.const_char = const_char

	def avalia(self):
		return self.const_char

	def accept(self, visitor):
		visitor.visita_const_char(self)

class const_string(Nodo):

	def __init__(self, const_string):
		self.const_string = const_string

	def avalia(self):
		return self.const_string

	def accept(self, visitor):
		visitor.visita_const_string(self)

class mais_mais(Nodo):

	def __init__(self, mais_mais):
		self.type = "++"
		self.mais_mais = mais_mais

	def avalia(self):
		return self.mais_mais

	def accept(self, visitor):
		visitor.visita_const(self)

class menos_menos(Nodo):

	def __init__(self, menos_menos):
		self.type = "--"
		self.menos_menos = menos_menos

	def avalia(self):
		return self.menos_menos

	def accept(self, visitor):
		visitor.visita_const(self)

class id(Nodo):

	def __init__(self, id_):
		self.id_ = id_

	def avalia(self):
		from impressao import tipagem
		if self.id_ in tipagem:

			tp = tipagem[self.id_]			

			if tp == "int":
				return 1
			elif tp == "float":
				return 1.2
			elif tp == "boolean":
				return "true"
			elif tp == "char":
				return 'a'
		else:
			return self.id_

	def accept(self, visitor):
		visitor.visita_id(self)

class true(Nodo):

	def __init__(self, true_):
		self.type = "true"
		self.true_ = true_

	def avalia(self):
		return self.true_

	def accept(self, visitor):
		visitor.visita_const(self)

class false(Nodo):

	def __init__(self, false_):
		self.type = "false"
		self.false_ = false_

	def avalia(self):
		return self.false_

	def accept(self, visitor):
		visitor.visita_const(self)

class id_atribuicao_exp(object):

	def __init__(self, id_, exp):
		self.id_ = id_
		self.exp = exp

	def avalia(self):
		return self.exp.avalia()

	def accept(self, visitor):
		visitor.visita_id_atribuicao_exp(self)

class id_cochete_exp(object):

	def __init__(self, id_, exp):
		self.id_ = id_
		self.exp = exp

	def avalia(self):
		return self.exp 

	def accept(self, visitor):
		visitor.visita_id_cochete_exp(self)

class parentese_exp(object):

	def __init__(self, exp):
		self.exp = exp

	def avalia(self):
		return self.exp

	def accept(self, visitor):
		visitor.visita_parentese_exp(self)

class chave_exp(object):

	def __init__(self, exp):
		self.exp = exp

	def avalia(self):
		return self.exp

	def accept(self, visitor):
		visitor.visita_chave_exp(self)

class aspa_dupla_exp(object):

	def __init__(self, exp):
		self.exp = exp

	def avalia(self):
		return self.exp

	def accept(self, visitor):
		visitor.visita_aspa_dupla_exp(self)

class aspa_simples_exp(object):

	def __init__(self, exp):
		self.exp = exp

	def avalia(self):
		return self.exp

	def accept(self, visitor):
		visitor.visita_aspa_simples_exp(self)

class extras(object):

	def __init__(self, tipo, exp):
		self.tipo = tipo
		self.exp = exp

	def avalia(self):
		return self.exp

	def accept(self, visitor):
		visitor.visita_extras(self)

class condicional1(object):

	def __init__(self, expression, stm):
		self.expression = expression
		self.stm = stm

	def avalia(self):
		return self.stm

	def accept(self, visitor):
		visitor.visita_condicional1(self)

class condicional2(object):

	def __init__(self, expression, stm1, stm2):
		self.expression = expression
		self.stm1 = stm1
		self.stm2 = stm2

	def avalia(self):
		return self.stm2

	def accept(self, visitor):
		visitor.visita_condicional2(self)

class for1(object):

	def __init__(self, tipo, id_, expression, arg1, arg2, bloco, stm):
		self.tipo = tipo
		self.id_ = id_
		self.expression = expression
		self.arg1 = arg1
		self.arg2 = arg2
		self.bloco = bloco
		self.stm = stm

	def avalia(self):
		return self.bloco

	def accept(self, visitor):
		visitor.visita_for1(self)

class for2(object):

	def __init__(self, arg1, arg2, arg3, bloco, stm):
		self.arg1 = arg1
		self.arg2 = arg2
		self.arg3 = arg3
		self.bloco = bloco
		self.stm = stm

	def avalia(self):
		return self.bloco

	def accept(self, visitor):
		visitor.visita_for2(self)

class while_(object):

	def __init__(self, expression, bloco, stm):
		self.expression = expression
		self.bloco = bloco
		self.stm = stm

	def avalia(self):
		return self.bloco

	def accept(self, visitor):
		visitor.visita_while(self)

class do_while(object):

	def __init__(self, bloco, expression, stm):
		self.bloco = bloco
		self.expression = expression
		self.stm = stm

	def avalia(self):
		return self.bloco

	def accept(self, visitor):
		visitor.visita_do_while(self)
