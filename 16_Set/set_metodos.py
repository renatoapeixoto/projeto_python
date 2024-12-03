import os


os.system('cls')

# Criação de 4 Set´s.
set_1 = {'3', '4'}
set_2 = {'3', '4', '5', '6'} 
set_3 = {1, 3, 5, 7} 
set_4 = {2, 4, 6, 8}

# função mostrar_sets
def mostrar_sets():
    print(F'set_1: {set_1} - <str>')
    print(F'set_2: {set_2} - <str>')
    print(F'set_3: {set_3} - <int>')
    print(F'set_4: {set_4} - <int>')

# função mostrar_set_1 e set_2 
def mostrar_sets_1_2():
    print(F'set_1: {set_1} - <str>')
    print(F'set_2: {set_2} - <str>')

# função mostrar_set_3 e set_4 
def mostrar_sets_3_4():
    print(F'set_3: {set_3} - <int>')
    print(F'set_4: {set_4} - <int>')

# Função para mostrar a tela principal do programa
def tela ():
    os.system("cls")
    print('***  SETs JÁ CRIADOS  ***')
    print('-' * 80)
    mostrar_sets()
    print('-' * 80)
    print('***  MENU PRINCIPAL / METODOS SETs  ***')
    print('Escolha "1" para Metodo  .add(elemento)')
    print('Escolha "2" para Metodo  .remove(elemento)')
    print('Escolha "3" para Metodo  .discard(elemento) ')
    print('Escolha "4" para Metodo  .clear() ')
    print('Escolha "5" para Metodo  .union() ')
    print('Escolha "6" para Metodo  .intersection() ')
    print('Escolha "7" para Metodo  .difference() ')
    print('Escolha "8" para Metodo  .symmetric_difference() ')
    print('Escolha "9" para Metodo  .issubset() ')
    print('Escolha "10" para Metodo .issuperset() ')
    print('Escolha "11" para Metodo .isdisjoint() ')
    print('-' * 80)

tela() # função mostrar a tela principal do programa
while True:
    print('Digite "V" para visualizar Menu Principal,')
    print('Digite "S" para Sair,')
    escolha = input('Digite um numero (1-11) do Metodo Sets: ').lower().strip()
    
    if escolha == '':
        continue
    
    elif escolha == 's':
        # aperta S para sair do loop e do programa
        os.system("cls")
        print('Fim do programa!!!')
        exit()
    
    elif escolha == 'v':
        tela() # função mostrar a tela principal do programa
    
    elif escolha == '1':
        # add(elemento): Adiciona um elemento ao set escolhido.
        mostrar_sets()
        print('-' * 80)
        
        elemento = input('Digite um elemento para adicionar: ').strip().lower()
        while elemento == '':
            elemento = input('Digite um elemento para adicionar: ').strip().lower()
        
        escolhe_set = input('Digite "1", "2", "3", "4" para escolher qual Sets será adicionado ').lower().strip()
        while escolhe_set == '' or escolhe_set not in ['1', '2', '3', '4']:
            escolhe_set = input('Digite "1", "2", "3", "4" para escolher qual Sets será adicionado ').lower().strip()
        
        if escolhe_set == '1':
            set_1.add(elemento)
        elif escolhe_set == '2':
            set_2.add(elemento)
        elif escolhe_set == '3':
            set_3.add(int(elemento))
        elif escolhe_set == '4':
            set_4.add(int(elemento))
       
        mostrar_sets()
        print('OBS: set_1.add(elemento) : Adiciona um elemento ao set. Não repete elemento.')
        print('-' * 80)
    
    elif escolha == '2':
        # remove(elemento): Remove um elemento do set. Lança um erro se o elemento 
        # não estiver presente.
        mostrar_sets()
        print('-' * 80)
        
        elemento = input('Digite um elemento para remover: ').strip().lower()
        while elemento == '':
            elemento = input('Digite um elemento para remover: ').strip().lower()
        
        escolhe_set = input('Digite "1", "2", "3", "4" para escolher qual Sets: ').lower().strip()
        while escolhe_set == '' or escolhe_set not in ['1', '2', '3', '4']:
            escolhe_set = input('Digite "1", "2", "3", "4" para escolher qual Sets: ').lower().strip()
        
        if escolhe_set == '1':
            set_1.remove(elemento)
        elif escolhe_set == '2':
            set_2.remove(elemento)
        elif escolhe_set == '3':
            set_3.remove(int(elemento))
        elif escolhe_set == '4':
            set_4.remove(int(elemento))
        
        mostrar_sets()    
        print('OBS: set_1.remove(elemento) : Remove um elemento do set. Lança um erro\n' 
              'se o elemento não estiver presente.')
        print('-' * 80)
    
    elif escolha == '3':
        # discard(elemento): Remove um elemento do set se ele estiver presente. 
        # Não faz nada se o elemento não estiver presente.
        mostrar_sets()
        print('-' * 80)
        
        elemento = input('Digite um elemento para discartar: ').strip().lower()
        while elemento == '':
            elemento = input('Digite um elemento para discartar: ').strip().lower()
        
        escolhe_set = input('Digite "1", "2", "3", "4" para escolher qual Sets: ').lower().strip()
        while escolhe_set == '' or escolhe_set not in ['1', '2', '3', '4']:
            escolhe_set = input('Digite "1", "2", "3", "4" para escolher qual Sets: ').lower().strip()
        
        if escolhe_set == '1':
            set_1.discard(elemento)
        elif escolhe_set == '2':
            set_2.discard(elemento)
        elif escolhe_set == '3':
            set_3.discard(int(elemento))
        elif escolhe_set == '4':
            set_4.discard(int(elemento))
        
        mostrar_sets()   
        print('OBS: set_1.discard(elemento) : Remove um elemento do set se ele estiver presente,\n' 
              'caso contrário, não faz nada se o elemento não estiver presente.')
        print('-' * 80)
    
    elif escolha == '4':
        # clear(): Remove todos os elementos do set.
        mostrar_sets()
        print('-' * 80)
        
        escolhe_set = input('Digite "1", "2", "3", "4" para escolher qual Sets: ').lower().strip()
        while escolhe_set == '' or escolhe_set not in ['1', '2', '3', '4']:
            escolhe_set = input('Digite "1", "2", "3", "4" para escolher qual Sets: ').lower().strip()
        
        if escolhe_set == '1':
            set_1.clear()
        elif escolhe_set == '2':
            set_2.clear()
        elif escolhe_set == '3':
            set_3.clear()
        elif escolhe_set == '4':
            set_4.clear()        
        
        mostrar_sets()
        print('OBS: set_1.clear() : Limpa todos os elementos de um Set.')
        print('-' * 80)
    
    elif escolha == '5':
        # union(set2) ou |: Retorna um novo set que é a união de dois sets.
        print('-' * 80)
        print(F'set_1: {set_1}')
        print(F'set_2: {set_2}')
        set_uniao = set_1.union(set_2)
        print('Resultado: set_uniao = set_1.union(set_2):', set_uniao)
        print(F'set_3: {set_3}')
        print(F'set_4: {set_4}')
        set_uniao = set_3.union(set_4)  
        # set_uniao = set_3 | set_4
        print('Resultado: set_uniao = set_3.union(set_4):', set_uniao)
        print('OBS: Retorna um novo set que é a união de dois sets. Observação, não repete elemento.')
        print('-' * 80)
    
    elif escolha == '6':
        # intersection(set2) ou & : Retorna um novo set que é a interseção de dois sets.
        print('-' * 80)
        print(F'set_1: {set_1}')
        print(F'set_2: {set_2}')
        set_interseção = set_1.intersection(set_2)
        # set_interseção = set_1 & set_2
        print('Resultado: set_interseção = set_1.intersection(set_2): ', set_interseção)
        print(F'set_3: {set_3}')
        print(F'set_4: {set_4}')
        set_interseção = set_3.intersection(set_4)
        print('Resultado: set_interseção = set_3.intersection(set_4): ', set_interseção)
        print('OBS: Retorna um novo set com elementos que estão em ambos os sets.')
        print('-' * 80)
    
    elif escolha == '7':
        # difference(set2) ou -: Retorna um novo set com os elementos do primeiro
        # set que não estão no segundo set.
        print('-' * 80)
        mostrar_sets_1_2()
        set_diferença = set_1.difference(set_2)
        # set_diferença = set_1 - set_2
        print('Resultado: set_diferença = set_1.difference(set_2): ', set_diferença)
        mostrar_sets_3_4()
        set_diferença = set_3.difference(set_4)
        print('Resultado: set_diferença = set_3.difference(set_4): ', set_diferença)
        print('OBS: Retorna um novo set com os elementos do Set_1 que não estão no Set_2.')
        print('-' * 80)
    
    elif escolha == '8':
        # symmetric_difference(set2) ou ^: Retorna um novo set com elementos que 
        # estão em um dos sets, mas não em ambos.
        print('-' * 80)
        mostrar_sets_1_2()
        set_diferenca_simetrica = set_1.symmetric_difference(set_2)
        # set_diferenca_simetrica = set_1 ^ set_2
        print('Resultado: set_diferenca_simetrica = set_1.symmetric_difference(set_2):', set_diferenca_simetrica)
        mostrar_sets_3_4()
        set_diferenca_simetrica = set_3.symmetric_difference(set_4)
        print('Resultado: set_diferenca_simetrica = set_3.symmetric_difference(set_4):', set_diferenca_simetrica)
        print('OBS: Set_diferenca_simetrica: Retorna um novo set com elementos que estão em um\n'
              'dos sets, mas não em ambos.')
        print('-' * 80)
    
    elif escolha == '9':
        # issubset(set2): Verifica se o set_1 é um subconjunto, está contido dentro outro set.
        print('-' * 80)
        mostrar_sets_1_2()
        set_subconjunto = set_1.issubset(set_2)
        print('Resultado: set_subconjunto = set_1.issubset(set_2):', set_subconjunto)
        mostrar_sets_3_4()
        set_subconjunto = set_3.issubset(set_4)
        print('Resultado: set_subconjunto = set_3.issubset(set_4):', set_subconjunto)
        print('OBS: Verifica se o set_1 é um subconjunto(está contido) em set_2.')    
        print('-' * 80)
    
    elif escolha == '10':
        # issuperset(set2): Verifica se o set_1 é um superconjunto(contém) set_2.
        print('-' * 80)
        mostrar_sets_1_2()
        set_superconjunto = set_2.issuperset(set_1)
        print('Resultdo: set_superconjunto = set_2.issuperset(set_1):', set_superconjunto)
        mostrar_sets_3_4()
        set_superconjunto = set_4.issuperset(set_3)
        print('Resultado: set_superconjunto = set_4.issuperset(set_3):', set_superconjunto)
        print('OBS: Verifica se o set_2 é um superconjunto(contém) set_1. ')    
        print('-' * 80)
    
    elif escolha == '11':
        # issuperset(set2): Verifica se o set_1 é um superconjunto(contém) set_2.
        print('-' * 80)
        mostrar_sets_1_2()
        set_disjuncao = set_1.isdisjoint(set_2)
        print('Resultado: set_disjuncao = set_1.isdisjoint(set_2):', set_disjuncao)
        mostrar_sets_3_4()
        set_disjuncao = set_3.isdisjoint(set_4)
        print('Resultado: set_disjuncao = set_3.isdisjoint(set_4):', set_disjuncao)
        print('OBS: Disjunção verifica se não há elemento em comum em ambos os set')    
        print('-' * 80)