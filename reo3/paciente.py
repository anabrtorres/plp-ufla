'''
Essa	classe	deve	herdar	a	classe1 Pessoa;
    ■ Deve	ter	uma	variável	de	classe	que	seja	incrementada	a	cada	novo	paciente	instanciado	(método	construtor),	e	decrementada	a	cada	paciente	desinstanciado	(método	destrutor).	Essa	variável	armazena	a	quantidade	de	objetos	instanciados,	no	momento,	da	classe Paciente.

    ■ Implementar	os	seguintes	métodos:
        ● definir_id,	que	recebe	um	id	de	no	máximo	5	caracteres	alfa-numéricos.	Caso	o	id	tenha	mais	 de	5	caracteres,	exibir	mensagem de	erro, mas	não	interromper	a	execução	do	programa;
        ● definir_prontuário,	que	recebe um	objeto	da	classe	Prontuario;
        ● pacientes_ativos,	um	método	de	classe,	que	retorna	o	valor	da	variável de	classe	que	armazena a	quantidade	de	pacientes	ativos,	no	momento.
'''

from pessoa import Pessoa

class Paciente(Pessoa):
    count = 0

    #constructor
    def __init__(self, nome):
        super().__init__(nome)
        self.__class__.count += 1

    #destroyer
    def __del__(self):
        self.__class__.count -= 1

    #methods
    def definir_id(self, id):
        self.__id = id
        if len(id) > 5:
            raise Exception('Error (mais que 5 caracteres)')

    def definir_prontuario(self, prontuario):
        self.append(prontuario)

    def pacientes_ativos (self, count):
        return self.__class__.count
