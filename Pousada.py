print('Bem vinde a pousada A, temos diversas opções de quartos')
opquartos='Quarto Básico', 'Quarto Prata', 'Quarto Ouro', 'Quarto Platina', 'Quarto Rubi', 'Quarto Diamante'
while True:
    quarto=int(input('''Escolha uma das nossas opções: 
Quarto Básico....R$100 [0] 
Quarto Prata.....R$200 [1] 
Quarto Ouro......R$350 [2] 
Quarto Platina...R$450 [3] 
Quarto Rubi......R$550 [4] 
Quarto Diamante..R$730 [5] 
-------------------------------
Qual quarto deseja escolher?'''))
    if quarto<0 or quarto>5:
        while quarto<0 or quarto>5:
            print('Valor \033[31minválido\033[m')
            quarto=int(input('''Escolha uma das nossas opções: 
Quarto Básico....R$100 [0] 
Quarto Prata.....R$200 [1] 
Quarto Ouro......R$350 [2] 
Quarto Platina...R$450 [3] 
Quarto Rubi......R$550 [4] 
Quarto Diamante..R$730 [5] 
-------------------------------
Qual quarto deseja escolher?'''))
    confirmaq=str(input(f'Você escolheu o {opquartos[quarto]}, certo? [S] [N]')).upper() .strip() [0]
    
    if confirmaq == 'N':
        print('Certo, mostraremos as opções novamente.')
    elif confirmaq != 'S' and confirmaq != 'N':
        while confirmaq != 'S' and confirmaq != 'N':
            confirmaq=str(input(f'Valor \033[31minválido\033[m. Você escolheu o quatro {quarto}, certo? [S] [N]')).upper() .strip() [0]
    if confirmaq =='S':
        break
print('-'*30)

#      Escolha dos quartos
while True:
    tempo=int(input(f'Quantas noites deseja ficar no {opquartos[quarto]}? '))
    if quarto==0:
        conta=tempo*100
    elif quarto==1:
        conta=tempo*200
    elif quarto==2:
        conta=tempo*350
    elif quarto==3:
        conta=tempo*450
    elif quarto==4:
        conta=tempo*550
    elif quarto==5:
        conta=tempo*730
    confirmat=str(input(f'ficando no {opquartos[quarto]} por {tempo} noites ficaria R${conta}. Continuar? [S] [N]')).upper() .strip() [0]
    if confirmat=='N':
        print('Certo. Voltaremos para a seção da estadia.')
    elif confirmat != 'S' and confirmat != 'N':
        while confirmat != 'S' and confirmat != 'N':
            confirmat=str(input(f'Valor \033[31minválido\033[m. Deseja passar {tempo} noites no quarto {opquartos[quarto]} por R${conta}? [S] [N]')).upper() .strip() [0]
    if confirmat=='S':
        break
contatempo=conta
print('-'*30)
#      Estadia
adicionais=['Café da manhã', 'Almoço', 'Janta','Wifi rápido','Lavanderia']
contad=0
precoad=5
ad=str(input(f'Conheça nossos adicionais: {adicionais} \nDeseja algum adicional? [S] [N]')).upper() .strip() [0]
if ad=='S':
    while True:
        while True:
            if contad<=2:
                precoad+=10
            elif contad>2 and contad<5:
                precoad+=15
            elif contad==5:
                break
            adicional=str(input(f'Deseja adicionar {adicionais[contad]} por R${precoad}? [S] [N]')).upper() .strip() [0]
            if adicional!='S' and adicional!='N':
                while adicional!='S' and adicional!='N':
                    adicional=str(input(f'Deseja adicionar {adicionais[contad]} por R${precoad}? [S] [N]')).upper() .strip() [0]
            if adicional=='S':
                conta+=precoad
            contad+=1
        if contad==5:
            break
elif ad!='S' and ad!='N':
    while ad!='S' and ad!='N':
        ad=str(input('Valor \033[31minválido\033[m. Deseja adicionais [S] [N]'))
print('-'*30)
#      Adicionais
print(f'Sua conta deu {conta}. {contatempo} são por passar {tempo} noites no {opquartos[quarto]} e {conta-contatempo} são dos adicionais.')
print('\nOBRIGADO PELA PREFERÊNCIA, VOLTE SEMPRE!')
#      Final