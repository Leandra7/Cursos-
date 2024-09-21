'''print(' Qual a sua idade ?')
idade=int(input())

if idade >= 18:
   print('ACESSO LIBERADO! BOA FESTA! ')
else:
    print('ACESSO NEGADO! VOCÊ È MENOR DE IDADE')'''

    #CÓDIGO PARA LIBERAR ACESSO SOMENTE PARA MAORES DE 19

'''print(' Qual a sua idade?')
idade= int(input())

if idade < 18:
    print(' ACESSO NEGADO! VOCÊ  É MENOR DE IDADE!')
elif idade==18:
    print('VOCÊ ESTÁ QUASE LÁ! MAIS UM ANO E VOCÊ TERÁ ACESSO! ')
else:
    print('ACESSO LIBERADO!BOA FESTA')'''

'''print( 'Digite a nota do primeiro bimestre')
B1= float(input())
print (' Digite a nota do segundo bimestre: ')
B2=float(input())
print('Digite a nota do terceiro bimestre')
B3 = float(input())
print('Digite a nota do quarto bimestre')
B4 = float(input())
media=(B1+B2+B3+B4) / 4
print('a media do aluno é', media )
#Código para verificar se o aluno está aprovado
if media >= 7:
    print('PARABÉNS! VOCÊ ESTÀ APROVADO')
elif media >= 5:
    print('VOCÊ ESTÀ QUASE LÀ! VAMOS REALIZAR UMA RECUPERAÇÃO')
else:
    print('INFELIZMENTE VOCÊ ESTÀ REPROVADO ')'''




    
    #CÓDIGO PARA VERIFICAR SE PODE PARTICIPAR DOS MULHERES TECH

'''print (' Qual seu gênero ? ( F OU M)')
genero = input().upper()
print (' Qual município você mora ? ' )
municipio = input().lower()
if genero == 'F' and  municipio=='rio de janeiro':
    print('VOCÊ PODE PARTICIPAR DO MULHERES TECH')
else:
    print('VOCÊ NÃO PODE PARTICIPAR DO MULHERES TECH')'''


# CÓDIGO PARA LIBERAR O ACESSO DE UM FILME PARA MAORES DE 18 ANOS
  
print("*" * 30, 'BEM VINDO AO CINEMA SEVERIANO RIBEIRO' ,"*" * 30 )
print('')
print('QUAL SUA IDADE ?')
idade = int(input())

if idade >= 18:
 print(' ACESSO LIBERADO!\n BOM FILME')


elif idade  >= 16:
    print(' O FLME SELECIONADO É PARA MAIORES DE !* ANOS\n PARA ACESSAR  PRECO')
    responsavel=input().upper()
    if responsavel== 'SIM':
     print(' O FILME SELECIONADO È PARA MAIORES DE 18 ANOS\n PARA  ACESSO ')
    else:
     print('VOCÊ SÓ PODE VER O FILME ACOMPANHADO DE UM RESPONSÁVEL')

else:
    print(' ACESSO NEGADO!\nVOCÊ É MENOR DE IDADE')




 

