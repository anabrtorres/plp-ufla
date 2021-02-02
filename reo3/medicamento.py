'''
Implementar	os	seguintes	métodos:
    ● construtor, que	recebe	o	nome	do	medicamento	e	armazena	em	variável privada;
    ● nome_medicamento,	que	retorna	o	nome	do	medicamento.
'''

import abc

class Medicamento:
    #constructor
    def __init__(self, medicamento):
        self.__medicamento = medicamento
    
    #getter
    @property
    def nome_medicamento(self):
        return self.__medicamento