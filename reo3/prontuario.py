'''
■ Deve	conter	uma	variável	privada	que	armazenará	uma	lista	de	procedimentos	ou	
registros	no	prontuário
■ Deve	implementar	os	seguintes	métodos:
    ● construtor,	que	inicia	a	variável	privada	de	lista	de	procedimentos	como	lista vazia;
    ● insere_procedimento,	que	recebe	os	parâmetros	listados	a	seguir,	cria um	dicionário	como	esses	valores	e	faz	o	append desse	dicionário	na lista	de	procedimentos.	As	chaves	do	dicionário	podem	ser	iguais	aos	nomes	dos	parâmetros	listados	a	seguir:
        ○ medicamento:	objeto	da	classe	Medicamento;
        ○ posologia:	string indicando	hipotética	posologia	do	remédio	utilizado;
        ○ medico:	objeto	da	classe	Medico;
        ○ data:	string da	data	do	procedimento	no	seguinte	formato	"dd-mmaaaa",	por	exemplo	'15/06/2020'.	Dicas em	2;
        ○ hora:	string com	horário	do	procedimento	no	formato	"hh:mm",	por	 exemplo	'10:10'.
    ● exibe_prontuario,	que	exibe	todos	os	procedimentos	armazenados	na	lista	de	procedimentos.	Cada	posição	da	lista	terá	um	dicionário	com	as	informações	de	um	procedimento	armazenado. Veja	o	caso	de	teste	neste documento	para	definir	o	formato	de	saída	deste	método.
'''

class Prontuario:
    
    #constructor
    def __init__(self):
        self.__lista = [] #lista de procedimentos

    #methods
    def insere_procedimento(self, medicamento, posologia, data, hora):
        self.medicamento = medicamento
        self.posologia = posologia
        self.data = data
        self.hora = hora

        self.__lista.objects.append(self)

    def exibe_procedimento(self):
