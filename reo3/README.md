# Atividade Avaliativa REO3 : Paradigma Orientado a Objetos

Steps to run this project:

1. Run `python3` command
2. Follow the command list below:
   > > > from paciente import Paciente
   > > > from medico import Medico
   > > > from medicamento import Medicamento
   > > > from prontuario import Prontuario
   > > > paciente1 = Paciente('Paciente1')
   > > > prontuario1 = Prontuario()
   > > > paciente2 = Paciente('Paciente2')
   > > > prontuario2 = Prontuario()
   > > > medicamento1 = Medicamento('Omeprazol')
   > > > medicamento2 = Medicamento('Tylenol')
   > > > medicamento3 = Medicamento('Dipirona')
   > > > medico1 = Medico('Medico1')
   > > > medico2 = Medico('Medico2')
   > > > paciente1.definir_prontuario(prontuario1)
   > > > paciente2.definir_prontuario(prontuario2)
   > > > paciente1.prontuario.insere_procedimento(medicamento1, '68mcg',
   > > > output: medico1, "15-06-2020", "10:10")
   > > > paciente1.prontuario.insere_procedimento(medicamento2, '100mg',
   > > > output: medico1, "15-06-2020", "11:40")
   > > > paciente2.prontuario.insere_procedimento(medicamento2, '18mcg',
   > > > output: medico2, "14-06-2020", "12:00")
   > > > paciente2.prontuario.insere_procedimento(medicamento3, '20mg',
   > > > output: medico2, "15-06-2020", "12:05")
   > > > paciente1.prontuario.exibe_prontuario()
   > > > output: Omeprazol - 68mcg - Medico1 - 2020-06-15 - 10:10:00
   > > > output: Tylenol - 100mg - Medico1 - 2020-06-15 - 11:40:00
   > > > paciente2.prontuario.exibe_prontuario()
   > > > output: Tylenol - 18mcg - Medico2 - 2020-06-14 - 12:00:00
   > > > output: Dipirona - 20mg - Medico2 - 2020-06-15 - 12:05:00
   > > > Paciente.pacientes_ativos()
   > > > output: 2
   > > > del paciente2
   > > > Paciente.pacientes_ativos()
   > > > output: 1
#   p l p - u f l a  
 