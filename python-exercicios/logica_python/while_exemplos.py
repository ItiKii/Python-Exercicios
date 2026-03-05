#lista de Usuarios e senhas cadastradas.

usuarios = [
   "italo", "gustavo", "italo gustavo",
   "kauan", "jhun enzo", "enzo"
]

senhas = [
   "1234", "1212", "2004", "2026",
   "2000", "2020"
]

nome = ""
senha = ""
numero_secreto = ""
erros = 0

print("============================================================")
print("|    BEM VINDO AO MINI GAME PARA VER SUAS ESTATISTICAS!     |")
print("============================================================")

#---> Pede o nome do usuario cadastrado valida e deixa passar.

while nome not in usuarios:
     nome = input("Nome de usuário: ").strip().lower()

     if nome not in usuarios:
      print("Nome não encontrado na lista, digite um nome valido. ")

print("Nome válido!... Bem vindo ",nome,".")

#---> Pede senha do usuario cadastrado valida e deixa passar.

while senha not in senhas:
    senha = input(" ---> Senha do usuário de 4 digitos: ")

    if senha not in senhas:
       print("A", senha, "não foi encontrada na lista, digite uma senha valida de 4 numeros.")

print("---> Bem vindo ao jogo <--- \n Entre 1 e 10 existe um numero premiado.")



while numero_secreto != "7":
    numero_secreto = input("Digite um numero: ")
    
    if numero_secreto != "7":
       erros += 1
       print("O numero premiado não e o",numero_secreto,"tente outro numero.")

print("---------------------------------------------------------------------------------------------------------")
print("Parabens!!!! Vocé acertou o numero premiado 7, pode seguir para ver suas informações! tentativas:",erros)    
print("---------------------------------------------------------------------------------------------------------")

# Sistema basico com while, if, elif e else.

hora_estudo = "18:30"
hora_trabalho = "07:00"
sair = ""

while sair != "3":
    sair = input("----> Digite um numero: 1 > Horario de estudo.    2> Horario de trbalho.    3> sair.  <----")

    if sair == "1":
     print("Estudar:",hora_estudo)

    elif sair == "2":
     print("Trabalhar:",hora_trabalho)

    else:
       print("Digite um numero entre 1 e 3!")

 
print("Saindo do programa!...")
    




    

   
   
    





