import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


#Antecendentes e Consequente
qualidade  = ctrl.Antecedent(np.arange(0,11, 1), 'qualidade')
servico  = ctrl.Antecedent(np.arange(0,11, 1), 'servico')
gorjeta = ctrl.Consequent(np.arange(0,21, 1), 'gorjeta')

#Antecendentes
qualidade.automf(number=3, names=['ruim', 'boa', 'saborosa'])
servico.automf(number=3, names=['ruim', 'aceitável', 'ótimo'])

#Consequente - Solução baseada em forma triangular
gorjeta['baixa'] = fuzz.trimf(gorjeta.universe, [0, 0, 5])
gorjeta['media'] = fuzz.trimf(gorjeta.universe, [2, 10, 15])
gorjeta['alta'] = fuzz.trimf(gorjeta.universe, [15, 18, 20])

#Regras de referencia, podendo ter uma ou mais regras
regra1 = ctrl.Rule(qualidade['ruim'] | servico['ruim'], gorjeta['baixa'])
regra2 = ctrl.Rule( servico['aceitável'], gorjeta['media'])
regra3 = ctrl.Rule(qualidade['saborosa'] | servico['ótimo'], gorjeta['alta'])

#Sistema de Controle
sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3])
sistema = ctrl.ControlSystemSimulation(sistema_controle)
sistema.input['qualidade'] = 10
sistema.input['servico'] = 10
sistema.compute()
print(sistema.output['gorjeta'])
