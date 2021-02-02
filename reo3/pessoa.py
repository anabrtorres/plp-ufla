# Essa	classe	deve	ser	abstrata	e	ter	os	seguintes	métodos:
#   ● construtor,	que	recebe	o	nome	da	pessoa	e	armazena	em	uma	variável	privada;
#   ● método	getter,	para	retornar	o	nome	da	pessoa;
#   ● método definir_id,	método	abstrato,	que	recebe	um	parâmetro (identificacao)	a	ser	definido	nas	classes	filhas.

import abc

class Pessoa:
    #constructor
    def __init__(self, nome):
        self.__nome = nome
    
    #getter
    @property
    def nome(self):
        return self.__nome

    #method
    @abc.abstractmethod
    def definir_id(self, identificacao):
        pass