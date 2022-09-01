import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import random


#Antecendentes e Consequente
qualidade  = ctrl.Antecedent(np.arange(0,11, 1), 'qualidade')
servico  = ctrl.Antecedent(np.arange(0,11, 1), 'servico')
gorjeta = ctrl.Consequent(np.arange(0,21, 1), 'gorjeta')

#Antecendentes
qualidade.automf(number=3, names=['ruim', 'boa', 'saborosa'])
servico.automf(number=3, names=['ruim', 'aceitável', 'ótimo'])

#Consequente - Solução baseada na forma sigmoid
gorjeta['baixa'] = fuzz.sigmf(gorjeta.universe, 5, -1)
gorjeta['media'] = fuzz.gaussmf(gorjeta.universe, 10, 3)
gorjeta['alta'] = fuzz.pimf(gorjeta.universe, 10, 20, 20, 21)

#Regras de referencia, podendo ter uma ou mais regras
regra1 = ctrl.Rule(qualidade['ruim'] | servico['ruim'], gorjeta['baixa'])
regra2 = ctrl.Rule( servico['aceitável'], gorjeta['media'])
regra3 = ctrl.Rule(qualidade['saborosa'] | servico['ótimo'], gorjeta['alta'])

#Sistema de Controle
sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3])
sistema = ctrl.ControlSystemSimulation(sistema_controle)
nota_servico = random.randint(0, 11)
nota_qualidade = random.randint(0, 11)
sistema.input['qualidade'] = nota_qualidade
sistema.input['servico'] = nota_servico
sistema.compute()
valor_gorgeta = sistema.output['gorjeta']
print(f'Nota dada ao serviço: {nota_servico}, Nota dada a qualidade da comida {nota_qualidade}, Valor de gorjeta indicado {round(valor_gorgeta, 2)}')
