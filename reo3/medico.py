'''
■ Essa	classe	deve	herdar	a	classe	Pessoa.	
■ Implementar	os	seguintes	métodos:
   ● definir_id,	que	recebe	um	id	de	no	máximo	3	caracteres	alfa-numéricos;	
   Caso	o	id	tenha	mais	de	3	caracteres,	exibir	mensagem	de	erro,	mas	não	
   interromper	a	execução	do	programa;
   ● nome_medico,	que	retorna	o	nome	do	médico.
'''

from pessoa import Pessoa

class Medico(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)

    #getter
    @property
    def nome_medico(self):
        return self.__nome

    #methods
    def definir_id(self, id):
        self.__id = id
        if len(id) > 3:
            raise Exception('Error (mais que 3 caracteres)')
