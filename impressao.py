import visitor
from classes.main import *

variaveis_declaradas = []
erros = []
tipagem = {}

class Impressao(object):

    # definição inicial da classe semântica
    def __init__(self):
        self.aceita = True
        self.invalida = False

    # main principal
    def visita_main(self, main):
        print("main -> {", end=" ")
        if main.stm:
            check = str(main.stm.avalia())

            main.stm.accept(self)
        print("return -> {", end=" ")
        if main.expression:
            main.expression.accept(self)
        print("}",end=" ")
        print("}\n")

        print("||||||||||||||||||||||||||||||||||||||||||")
        print("\nVARIÁVEIS DECLARADAS {0}\n\nTIPAGEM {2}\n\n"
            "ERROS -> {1}\n".format(variaveis_declaradas, erros, tipagem))
        print("||||||||||||||||||||||||||||||||||||||||||")

        arquivo = open("resultado_semantico.txt", "w")
        arquivo.write(str(self.aceita))
        arquivo.close()

    def visita_bloco_stm(self, bloco_stm):
        print("bloco -> {", end=" ")
        if bloco_stm.bloco:
            bloco_stm.bloco.accept(self)
        print("}", end=" ")
        if bloco_stm.stm:
            bloco_stm.stm.accept(self)

    # break
    def visita_break(self, break_):

        if not self.invalida:
            print("\nERROR: break no escopo do main")
            erros.append("ERROR: break fora de loop")
            self.aceita = False

        print("break -> {", end=" ")
        if break_:
            break_.stm.accept(self)
        print("}", end=" ")

    #continue
    def visita_continue(self, continue_):

        if not self.invalida:
            print("\nERROR: continue no escopo do main")
            erros.append("ERROR: continue fora de loop")
            self.aceita = False

        print("continue -> {", end=" ")
        if continue_.stm:
            continue_.stm.accept(self)
        print("}", end=" ")

    # tipo de variável
    def visita_tipo(self, void):
        print("tipo -> ", end=" ")
        print(void.type, end=" ")

    # percorrimento de bloco
    def visita_bloco(self, bloco):
        print("bloco -> {", end=" ")
        # self.invalida = True
        if bloco.stm:
            bloco.stm.accept(self)
        # self.invalida = False

        variaveis_declaradas.clear()
        print("}", end=" ")

    # possibilidade de ponteiro *
    def visita_pointer(self, pointer):
        print("*", end=" ")
        if pointer.pointer:
            pointer.pointer.accept(self)

    # primeiro tipo de declaração de variável
    def visita_declaracao1(self, declaracao1):
        print("{", end=" ")
        declaracao1.tipo.accept(self)
        if declaracao1.pointer:
            declaracao1.pointer.accept(self)

        # verifica se variável já foi declarada alguma vez
        if declaracao1.id_ in variaveis_declaradas:
            print("\nERROR: ||Id '{0}' já declarada||  ".format(declaracao1.id_))
            # erro só é registrado se ainda não ocoreu
            if "declaração repetida para id '{0}'".format(declaracao1.id_) not in erros:
                erros.append("ERROR: declaração repetida para id '{0}'".format(declaracao1.id_))
            self.aceita = False
            
        # variável é registrada como declarada
        if declaracao1.id_ not in variaveis_declaradas:
            variaveis_declaradas.append(declaracao1.id_)
            tipagem[declaracao1.id_] = declaracao1.tipo.avalia()


        print(declaracao1.id_, end=" ")

        print("}", end=" ")
        if declaracao1.stm:
            declaracao1.stm.accept(self)

    # declaração de variável com atribuição
    def visita_declaracao2(self, declaracao2):
        print("{", end=" ")
        declaracao2.tipo.accept(self)
        if declaracao2.pointer:
            declaracao2.pointer.accept(self)

        # verifica se variável já foi declarada
        if declaracao2.id_ in variaveis_declaradas:
            print("\nERROR:   ||Variável '{0}' já declarada||  ".format(declaracao2.id_))
            if "declaração repetida para id '{0}'".format(declaracao2.id_) not in erros:
                erros.append("ERROR: declaração repetida para id '{0}'".format(declaracao2.id_))
            self.aceita = False
            
        # variável é registrada como declarada
        if declaracao2.id_ not in variaveis_declaradas:
            variaveis_declaradas.append(declaracao2.id_)
            tipagem[declaracao2.id_] = declaracao2.tipo.avalia()

        print(declaracao2.id_, end=" = ")

        check = declaracao2.expression.avalia()
        # verifica a equivalência da atribuição com o tipo da variável
        tp = " "
        t = True
        if declaracao2.id_ in tipagem:
            tp = tipagem[declaracao2.id_]

        if tp == "int":
            t = isinstance(check, int)
        elif tp == "float":
            t = isinstance(check, float)
        elif tp == "boolean":
            t = isinstance(type(check), type(bool))
        elif tp == "char":
            t = isinstance(check, str)  
        if not t:
            if "Expressão recusada para variável '{0}'".format(declaracao2.id_) not in erros:
                erros.append("ERROR: Expressão recusada para variável '{0}'".format(declaracao2.id_))
                print("\nERROR: Expressão recusada para variável '{0}'".format(declaracao2.id_))
                self.aceita = False

        declaracao2.expression.accept(self)
        print("}", end=" ")
        if declaracao2.stm:
            declaracao2.stm.accept(self)

    # declaração de vetor sem atribuição
    def visita_declaracao3(self, declaracao3):
        print("{", end=" ")
        declaracao3.tipo.accept(self)
        if declaracao3.pointer:
            declaracao3.pointer.accept(self)

        # verifica se a variável já foi declarada
        if declaracao3.id_ in variaveis_declaradas:
            print("\nERROR:  ||Variável '{0}' já declarada||  ".format(declaracao3.id_))
            if "declaração repetida para id '{0}'".format(declaracao3.id_) not in erros:
                erros.append("ERROR: declaração repetida para id '{0}'".format(declaracao3.id_))
            self.aceita = False
            
        # variável é registrada como declarada
        if declaracao3.id_ not in variaveis_declaradas:
            variaveis_declaradas.append(declaracao3.id_)
            tipagem[declaracao3.id_] = declaracao3.tipo.avalia()

        print(declaracao3.id_, end=" ")

        print("[", end=" ")
        if declaracao3.arg:
            declaracao3.arg.accept(self)
        print("]", end=" ")
        print("}", end=" ")
        if declaracao3.stm:
            declaracao3.stm.accept(self)

    # declaração de vetor com atribuição
    def visita_declaracao4(self, declaracao4):
        print("{", end=" ")
        declaracao4.tipo.accept(self)
        if declaracao4.pointer:
            declaracao4.pointer.accept(self)

        # verifica se a variável já foi declarada
        if declaracao4.id_ in variaveis_declaradas:
            print("\nERROR:  ||Variável '{0}' já declarada||  ".format(declaracao4.id_))
            if "declaração repetida para id '{0}'".format(declaracao4.id_) not in erros:
                erros.append("ERROR: declaração repetida para id '{0}'".format(declaracao4.id_))
            self.aceita = False
            
        # variável é registrada como declarada
        if declaracao4.id_ not in variaveis_declaradas:
            variaveis_declaradas.append(declaracao4.id_)
            tipagem[declaracao4.id_] = declaracao4.tipo.avalia()

        print(declaracao4.id_, end=" ")
        print("[", end=" ")
        if declaracao4.arg:
            declaracao4.arg.accept(self)
        print("]", end=" = ")
        if declaracao4.atribuicao_mat:
            declaracao4.atribuicao_mat.accept(self)
        print("}", end=" ")

        # check = declaracao4.atribuicao_mat.avalia()
        # tp = " "
        # t = True
        # if declaracao4.id_ in tipagem:
        #     tp = tipagem[declaracao4.id_]

        # if tp == "int":
        #     t = isinstance(check, int)
        # elif tp == "float":
        #     t = isinstance(check, float)
        # elif tp == "boolean":
        #     t = isinstance(type(check), type(bool))
        # elif tp == "char":
        #     t = isinstance(check, str)
        # if not t:
        #     if "Declaração recusada para '{0}'".format(tp) not in erros:
        #         erros.append("ERROR: Declaração recusada para '{0}'".format(tp))
        #         print("\nERROR: Declaração recusada para '{0}'".format(tp))
        #         self.aceita = False

        if declaracao4.stm:
            declaracao4.stm.accept(self)

    # declaração de matriz sem atribuição
    def visita_declaracao5(self, declaracao5):        
        print("{", end=" ")
        declaracao5.tipo.accept(self)
        if declaracao5.pointer:
            declaracao5.pointer.accept(self)

        # variável é registrada como declarada
        if declaracao5.id_ in variaveis_declaradas:
            print("\nERROR:  ||Variável '{0}' já declarada||  ".format(declaracao5.id_))
            if "declaração repetida para id '{0}'".format(declaracao5.id_) not in erros:
                erros.append("ERROR: declaração repetida para id '{0}'".format(declaracao5.id_))
            self.aceita = False
            
        # variável é registrada como declarada
        if declaracao5.id_ not in variaveis_declaradas:
            variaveis_declaradas.append(declaracao5.id_)
            tipagem[declaracao5.id_] = declaracao5.tipo.avalia()

        print(declaracao5.id_, end=" ")
        print("[", end=" ")
        if declaracao5.arg1:
            declaracao5.arg1.accept(self)
        print("]", end=" ")
        print("[", end=" ")
        if declaracao5.arg2:
            declaracao5.arg2.accept(self)
        print("[", end=" ")
        if declaracao5.more_arg:
            declaracao5.more_arg.accept(self)
        print("}", end=" ")
        if declaracao5.stm:
            declaracao5.stm.accept(self)

    # declaração de matriz com atribuição
    def visita_declaracao6(self, declaracao6):
        print("{", end=" ")
        declaracao6.tipo.accept(self)
        if declaracao6.pointer:
            declaracao6.pointer.accept(self)

        # variável é registrada como declarada
        if declaracao6.id_ in variaveis_declaradas:
            print("\nERROR:   ||Variável '{0}' já declarada||  ".format(declaracao6.id_))
            if "declaração repetida para id '{0}'".format(declaracao6.id_) not in erros:
                erros.append("ERROR: declaração repetida para id '{0}'".format(declaracao6.id_))
            self.aceita = False
            
        # variável é registrada como declarada
        if declaracao6.id_ not in variaveis_declaradas:
            variaveis_declaradas.append(declaracao6.id_)
            tipagem[declaracao6.id_] = declaracao6.tipo.avalia()

        print(declaracao6.id_, end=" ")
        print("[", end=" ")
        if declaracao6.arg1:
            declaracao6.arg1.accept(self)
        print("]", end=" ")
        print("[", end=" ")
        if declaracao6.arg2:
            declaracao6.arg2.accept(self)
        print("]", end=" ")
        if declaracao6.more_arg:
            declaracao6.more_arg.accept(self)
        print("=", end=" ")
        if declaracao6.atribuicao_mat:
            declaracao6.atribuicao_mat.accept(self)
        print("}", end=" ")

        # check = declaracao6.atribuicao_mat.avalia()
        # tp = " "
        # t = True
        # if declaracao6.id_ in tipagem:
        #     tp = tipagem[declaracao6.id_]

        #     if tp == "int":
        #         t = isinstance(check, int)
        #     elif tp == "float":
        #         t = isinstance(check, float)
        #     elif tp == "boolean":
        #         t = isinstance(type(check), type(bool))
        #     elif tp == "char":
        #         t = isinstance(check, str)  
        #     if not t:
        #         if "Declaração recusada para '{0}'".format(tp) not in erros:
        #             erros.append("ERROR: Declaração recusada para '{0}'".format(tp))
        #             print("\nERROR: Declaração recusada para '{0}'".format(tp))
        #             self.aceita = False      
        # # elif not isinstance(type(check), type(declaracao6.tipo)):
        # #     print("Não aceita") 

        if declaracao6.stm:
            declaracao6.stm.accept(self)

    # atribuição de múltiplos valores ex: 1, 2, 3, ...
    def visita_atribuicao_vet1(self, atribuicao_vet1):
        atribuicao_vet1.expression.accept(self)
        print(",", end="")
        if atribuicao_vet1.atribuicao_vet:
            atribuicao_vet1.atribuicao_vet.accept(self)

    # atribuição unitária para vetor ex: 1
    def visita_atribuicao_vet2(self, atribuicao_vet2):
        atribuicao_vet2.expression.accept(self)

    # atribuição múltipla para matriz ex: { {1,2}, {3,4} }
    def visita_atribuicao_mat1(self, atribuicao_mat1):
        print("{", end="")
        atribuicao_mat1.atribuicao_vet.accept(self)
        print("},", end=" ")
        atribuicao_mat1.atribuicao_mat.accept(self)

    # atribuição unitária para matriz ex: {1,2}
    def visita_atribuicao_mat2(self, atribuicao_mat2):
        print("{", end="")
        atribuicao_mat2.atribuicao_vet.accept(self)
        print("}", end="")

    # definição de equação para vetor ex: a[10] = 2 + 2
    def visita_equacao1(self, equacao1):
        if equacao1.pointer:
            equacao1.pointer.accept(self)

        # variável é registrada como declarada
        if equacao1.id_ not in variaveis_declaradas:
            print("\nERROR:  ||Variável '{0}' não declarada||  ".format(equacao1.id_))
            if "Variável '{0}' não declarada".format(equacao1.id_) not in erros:
                erros.append("ERROR: Variável '{0}' não declarada".format(equacao1.id_))
            self.aceita = False

        print(equacao1.id_, end=" = ")
        print("[", end="")
        if equacao1.arg:
            equacao1.arg.accept(self)
        print("] = ", end="")

        check = equacao1.expression.avalia()

        tp = " "
        t = True
        if equacao1.id_ in tipagem:
            tp = tipagem[equacao1.id_]

        if tp == "int":
            t = isinstance(check, int)
        elif tp == "float":
            t = isinstance(check, float)
        elif tp == "boolean":
            t = isinstance(type(check), type(bool))
        elif tp == "char":
            t = isinstance(check, str)  
        if not t:
            if "Expressão recusada para variável '{0}'".format(equacao1.id_) not in erros:
                erros.append("ERROR: Expressão recusada para variável '{0}'".format(equacao1.id_))
                print("\nERROR: Expressão recusada para variável '{0}'".format(equacao1.id_))
                self.aceita = False

        if equacao1.expression:
            equacao1.expression.accept(self)
        if equacao1.stm:
            equacao1.stm.accept(self)

    # definição de equação para matriz ex: a[10][100][1000] = 2 + 2
    def visita_equacao2(self, equacao2):
        if equacao2.pointer:
            equacao2.pointer.accept(self)

        if equacao2.id_ not in variaveis_declaradas:
            print("\nERROR:  ||Variável '{0}' não declarada||  ".format(equacao2.id_))
            if "Variável '{0}' não declarada".format(equacao2.id_) not in erros:
                erros.append("ERROR: Variável '{0}' não declarada".format(equacao2.id_))
            self.aceita = False

        print(equacao2.id_, end=" = ")
        print("[", end="")
        if equacao2.arg1:
            equacao2.arg1.accept(self)
        print("]", end="")
        print("[", end=" ")
        if equacao2.arg2:
            equacao2.arg2.accept(self)
        print("]", end=" ")
        if equacao2.more_arg:
            equacao2.more_arg.accept(self)
        print("=", end=" ")

        check = equacao2.expression.avalia()
        
        tp = " "
        t = True
        if equacao2.id_ in tipagem:
            tp = tipagem[equacao2.id_]

        if tp == "int":
            t = isinstance(check, int)
        elif tp == "float":
            t = isinstance(check, float)
        elif tp == "boolean":
            t = isinstance(type(check), type(bool))
        elif tp == "char":
            t = isinstance(check, str)  
        if not t:
            if "Expressão recusada para variável '{0}'".format(equacao2.id_) not in erros:
                erros.append("ERROR: Expressão recusada para variável '{0}'".format(equacao2.id_))
                print("\nERROR: Expressão recusada para variável '{0}'".format(equacao2.id_))
                self.aceita = False

        if equacao2.expression:
            equacao2.expression.accept(self)
        if equacao2.stm:
            equacao2.stm.accept(self)

    # definição de equação ex: a = 2 + 2
    def visita_equacao3(self, equacao3):
        if equacao3.pointer:
            equacao3.pointer.accept(self)

        if equacao3.id_ not in variaveis_declaradas:
            print("\nERROR:  ||Variável '{0}' não declarada||  ".format(equacao3.id_))
            if "Variável '{0}' não declarada".format(equacao3.id_) not in erros:
                erros.append("ERROR: Variável '{0}' não declarada".format(equacao3.id_))
            self.aceita = False

        print(equacao3.id_, end=" = ")

        check = equacao3.expression.avalia()        
        tp = " "
        t = True
        if equacao3.id_ in tipagem:
            tp = tipagem[equacao3.id_]

        if tp == "int":
            t = isinstance(check, int)
        elif tp == "float":
            t = isinstance(check, float)
        elif tp == "boolean":
            t = isinstance(type(check), type(bool))
        elif tp == "char":
            t = isinstance(check, str)  
        if not t:
            if "Expressão recusada para variável '{0}'".format(equacao3.id_) not in erros:
                erros.append("ERROR: Expressão recusada para variável '{0}'".format(equacao3.id_))
                print("\nERROR: Expressão recusada para variável '{0}'".format(equacao3.id_))
                self.aceita = False

        if equacao3.expression:
            equacao3.expression.accept(self)
        if equacao3.stm:
            equacao3.stm.accept(self)


    # arumento para vetor ou matriz
    def visita_arg(self, arg):
        if arg.expression:
            arg.expression.accept(self)
            check = arg.expression.avalia()
            if check:
                t = isinstance(check, int)
                if not t:
                    if "Argumento '{0}' não aceito".format(check) not in erros:
                        erros.append("ERROR: Argumento não aceito")
                        print("\nERROR: Argumento não aceito")
                        self.aceita = False

    # mais possibilidades de argumento para matriz múltipla ex: a[][][][][]
    def visita_more_arg(self, more_arg):
        if more_arg.more_arg:
            more_arg.more_arg.accept(self)
        print("[", end=" ")
        if more_arg.arg:
            more_arg.arg.accept(self)
        print("]", end=" ")

    # printf com apenas uma string
    def visita_mostrar1(self, mostrar1):
        print("printf (", end="")
        print(mostrar1.const, end=") ")
        if mostrar1.stm:
            mostrar1.stm.accept(self)

    # printf com string e variável
    def visita_mostrar2(self, mostrar2):
        print("printf (", end="")
        mostrar2.expression_mostrar.accept(self)
        print(")", end="")
        if mostrar2.stm:
            mostrar2.stm.accept(self)

    # composição múltipla para printf
    def visita_expression_mostrar1(self, expression_mostrar1):
        print(expression_mostrar1.const, end=", ")
        if expression_mostrar1.expression:
            expression_mostrar1.expression.accept(self)

        id_ = expression_mostrar1.expression.avalia()
        if id_ not in variaveis_declaradas and isinstance(id_, str):
            print("\nERROR:  ||Variável '{0}' não declarada||  ".format(id_))
            if "Variável '{0}' não declarada".format(id_) not in erros:
                erros.append("ERROR: Variável '{0}' não declarada".format(id_))
            self.aceita = False

        if expression_mostrar1.expression_mostrar:
            expression_mostrar1.expression_mostrar.accept(self)

    # finalização de composição múltipla para printf
    def visita_expression_mostrar2(self, expression_mostrar2):
        print(", ", end="")
        expression_mostrar2.expression.accept(self)

        id_ = expression_mostrar2.expression.avalia()
        if id_ not in variaveis_declaradas and isinstance(id_, str):
            print("\nERROR:  ||Variável '{0}' não declarada||  ".format(id_))
            if "Variável '{0}' não declarada".format(id_) not in erros:
                erros.append("ERROR: Variável '{0}' não declarada".format(id_))
            self.aceita = False

    # definição de entrada scanf
    def visita_entrada(self, entrada):
        print("scanf (", end="")
        if entrada.expression_entrada:
            entrada.expression_entrada.accept(self)
        print(")", end=" ")

        id_ = entrada.expression_entrada.avalia()
        if id_ not in variaveis_declaradas:
            print("\nERROR:  ||Variável '{0}' não declarada||  ".format(id_))
            if "Variável '{0}' não declarada".format(id_) not in erros:
                erros.append("ERROR: Variável '{0}' não declarada".format(id_))
            self.aceita = False

        if entrada.stm:
            entrada.stm.accept(self)

    # possibilidades múltiplas de entradas para scanf
    def visita_expression_entrada1(self, expression_entrada1):
        print(expression_entrada1.const, end=", &")
        print(expression_entrada1.id_, end="")
        if expression_entrada1.expression_entrada:
            expression_entrada1.expression_entrada.accept(self)

    # finalização de possibilidades múltiplas para scanf
    def visita_expression_entrada2(self, expression_entrada2):
        print(", &", end="")
        print(expression_entrada2.id_, end="")
        if expression_entrada2.expression_entrada:
            expression_entrada2.expression_entrada.accept(self)

    # expression operando expression
    def visita_bino_exp(self, bino_exp):
        print("{",end=" ")
        bino_exp.exp1.accept(self)
        print(bino_exp.type, end=" ")
        bino_exp.exp2.accept(self)
        print("}", end=" ")

    # operando expression
    def visita_uno_exp(self, uno_exp):
        print(uno_exp.type, end=" ")
        uno_exp.exp.accept(self)

    # exibição de constantes -----------------

    def visita_const(self, const):
        print(const.type, end=" ")

    def visita_const_numero_real(self, const):
        print(const.numero_real, end=" ")

    def visita_const_numero_int(self, const):
        print(const.numero_int, end=" ")

    def visita_const_char(self, const):
        print(const.const_char, end=" ")

    def visita_const_string(self, const):
        print(const.const_string, end=" ")

    def visita_id(self, id_):
        print(id_.id_, end=" ")

    # exibição de constantes -----------------

    # id = expression
    def visita_id_atribuicao_exp(self, id_atribuicao_exp):
        print(id_atribuicao_exp.id_, end=" = ")
        id_atribuicao_exp.exp.accept(self)

    # [ expression ]
    def visita_id_cochete_exp(self, id_cochete_exp):
        print(id_cochete_exp.id_, end=" ")
        print("[", end=" ")
        id_cochete_exp.exp.accept(self)
        print("]", end=" ")

    # ( expression )
    def visita_parentese_exp(self, parentese_exp):
        print("(", end=" ")
        parentese_exp.exp.accept(self)
        print(")", end=" ")

    # { expression }
    def visita_chave_exp(self, chave_exp):
        print("{", end=" ")
        chave_exp.exp.accept(self)
        print("}", end=" ")

    # " expression "
    def visita_aspa_dupla_exp(self, aspa_dupla_exp):
        print("\"", end=" ")
        aspa_dupla_exp.exp.accept(self)
        print("\"", end=" ")

    # ' expression '
    def visita_aspa_simples_exp(self, aspa_simples_exp):
        print("\'", end=" ")
        aspa_simples_exp.exp.accept(self)
        print("\'", end=" ")

    # permite o cast par expressão ex: (int) (1.2 + 2.7) 
    def visita_extras(self, extras):
        print('(', end="")
        extras.tipo.accept(self)
        print(')', end="")
        extras.exp.accept(self)

    # condicional apenas if
    def visita_condicional1(self, condicional1):
        print('if (', end="")
        condicional1.expression.accept(self)
        print(')', end="")
        if condicional1.stm:
            condicional1.stm.accept(self)

    # condicional if com else
    def visita_condicional2(self, condicional2):
        print('if (', end="")
        condicional2.expression.accept(self)
        print(')', end="")
        if condicional2.stm1:
            condicional2.stm1.accept(self)
        print(' else ', end="")
        if condicional2.stm2:
            condicional2.stm2.accept(self)

    # estrutura de repetição for com declaração de variável
    def visita_for1(self, for1):
        print('for (', end="")

        if for1.tipo:
            for1.tipo.accept(self)

        # verifica se variável já foi declarada alguma vez
        if for1.id_ in variaveis_declaradas:
            print("\nERROR: ||Id '{0}' já declarada||  ".format(for1.id_))
            # erro só é registrado se ainda não ocoreu
            if "declaração repetida para id '{0}'".format(for1.id_) not in erros:
                erros.append("ERROR: declaração repetida para id '{0}'".format(for1.id_))
            self.aceita = False
            
        # variável é registrada como declarada
        if for1.id_ not in variaveis_declaradas:
            variaveis_declaradas.append(for1.id_)
            tipagem[for1.id_] = for1.tipo.avalia()


        print(for1.id_, end=" = ")


        
        if for1.expression:
            for1.expression.accept(self)
        print(';', end="")
        if for1.arg1:
            for1.arg1.accept(self)
        print(';', end="")
        if for1.arg2:
            for1.arg2.accept(self)
        print(')', end="")
        self.invalida = True
        if for1.bloco:
            for1.bloco.accept(self)
        self.invalida = False
        if for1.stm:
            for1.stm.accept(self)

    # estrutura de repetição for sem declaração de variável
    def visita_for2(self, for2):
        print('for (', end="")
        if for2.arg1:
            for2.arg1.accept(self)
        print(';', end="")
        if for2.arg2:
            for2.arg2.accept(self)
        print(';', end="")
        if for2.arg3:
            for2.arg3.accept(self)
        print(')', end="")
        self.invalida = True
        if for2.bloco:
            for2.bloco.accept(self)
        self.invalida = False
        if for2.stm:
            for2.stm.accept(self)

    # estrutura de repetição while
    def visita_while(self, while_):
        print('while (', end="")
        while_.expression.accept(self)
        print(')', end="")
        self.invalida = True
        if while_.bloco:
            while_.bloco.accept(self)
        self.invalida = False
        if while_.stm:
            while_.stm.accept(self)

    # estrutura de repetição do-while
    def visita_do_while(self, do_while):
        print('do', end="")
        self.invalida = True
        if do_while.bloco:
            do_while.bloco.accept(self)
        self.invalida = False
        print('while (', end="")
        do_while.expression.accept(self)
        print(')', end="")
        if do_while.stm:
            do_while.stm.accept(self)