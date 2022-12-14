import mlrose


produtos = [('Refrigerador A', 0.751, 999.90 ),
           ('Notebook A', 0.00350, 2499.90 ),
           ('Microondas C', 0.0319, 299.29 ),
           ('Notebook C', 0.0319, 3999.00 ),
           ('Celular', 0.0000899, 2199.12 ),
           ('Refrigerador B', 0.635, 849.00 ),
           ('Ventilador', 0.496, 199.90 ),
           ('TV 55', 0.400, 4346.99 ),
           ('Microondas A', 0.0424, 308.66 ),
           ('TV 50', 0.290, 3999.90 ),
           ('Refrigerador C', 0.870, 1199.89 ),
           ('TV 42', 0.200, 2999.90 ),
           ('Microondas B', 0.0544, 429.90 ),
           ('Notebook B', 0.498, 1999.90),]

tamanho_total = 3.0

def imprimir_produtos(produto):
    valor_total = 0
    espaco_ocupado = 0
    for i in range(len(produto)):
        if produto[i] == 1:
            nome_produto, tamanho, valor  = produtos[i]
            print(f'Produto: {nome_produto} | Tamanho: {tamanho}M³ | Valor: R${valor}')
        
            valor_total += produtos[i][2]
            espaco_ocupado += produtos[i][1]
    if espaco_ocupado < tamanho_total:
        print(f'Tamanho do caminhão: {tamanho_total}M³ | Preço da carga R${valor_total} | Tamanho da carga {espaco_ocupado}M³')
            
#Fitness Function
def fitness_function(produto):
    custo = 0
    soma_espaco = 0
    for i in range(len(produto)):
        if produto[i] == 1:
            custo += produtos[i][2]
            soma_espaco += produtos[i][1]
    if soma_espaco > tamanho_total:
        custo = 1
    return custo


fitness = mlrose.CustomFitness(fitness_function)

problema = mlrose.DiscreteOpt(length=14, fitness_fn=fitness, maximize=True, max_val=2)

#Hill climb 
print('\nResultado dos melhores preços de produtos usando Algoritimos Hill climb.\n')
melhor_solucao_hill_climb, melhor_custo_hill_climb = mlrose.hill_climb(problema)
imprimir_produtos(melhor_solucao_hill_climb)

#simulated annealing 
print('\nResultado dos melhores preços de produtos usando Algoritimos Simulated Annealing (Têmpera simulada).\n')
melhor_solucao_simulated_annealing, melhor_custo_simulated_annealing = mlrose.simulated_annealing(problema, schedule=mlrose.decay.GeomDecay(init_temp=10000))
imprimir_produtos(melhor_solucao_simulated_annealing)

#Algoritimo genetivo
print('\nResultado dos melhores preços de produtos usando Algoritimos Genetícos.\n')
melhor_solucao_genetic_alg, melhor_custo_genetic_alg = mlrose.genetic_alg(problema)
imprimir_produtos(melhor_solucao_genetic_alg)
