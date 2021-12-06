import time

def abertura():
    print("\n\n           Tres exploradores se econtram presos por um tribo Maia Antiga             _\n\n")
    print(" Eles se perguntam o que aconteceu? ")
    print(" Margareth Tatcher: Estava correndo tudo bem na expedicao... ")
    print(" Karl Max: Acho que nos fomos atigindos por dados infectados e apagamos...")
    print(" Obama: E nos trousseram para um especie de tribo... ")
    time.sleep(3)
    print("  Como nossos exploradores vao sair dessa?\n")
    print("  Com sua ajudaaa! ")
    time.sleep(2)
    decisao=input("\n Digite (1) para ajuda-los  -  Digite (2) para deixa-los morrer: ")
    while decisao!="1" and decisao!="2":
        print("\n Opcao indisponivel")
        decisao=input("\n Digite (1) para ajuda- los  -  Digite (2) para deixa-los morrer: ")
    if(decisao=="1"):
        continua=True
    else:
        continua=False
        print("Todos os tres viraram comida!!")
    return continua
#FUNÇÃO DE ESCOLHA DE PERSONAGEM PELO USUARIO
def escolha_personagem():
    print("\n      Escolha uma dos tres exploradores para liberta-los    \n")
    print("          (1) Margareth Tatcher (2) Karl Max (3) Obama     \n")
    opcao=input(" Quem e voce?  ")
    print("-*20")
    while opcao !="1" and opcao !="2" :
        print("\n   Escolha entre 1,2 e 3      ")
        opcao=input("    Escolha um explorador: ")
        print('********************************************************************************************\n')
    if(opcao=="1"):
        nome_personagem="Margareth tatcher"
    elif(opcao== "2"):
        nome_personagem="Karl Max"
    else:
        nome_personagem="Obama"
    print(f".\n     Voce escolheu  {nome_personagem}    \n")
    time.sleep(1)
    return nome_personagem

#DEFINE QUAL FUNÇÃO PERSONAGEM VAI SER RODADA DE ACORDO COM A ESCOLHA DO USUARIO
def jogar(nome_personagem):
    if(nome_personagem=="Margareth Tacher"):
        jogando_com_personagem_1(nome_personagem)
    elif(nome_personagem=="Karl Max"):
        jogando_com_personagem_2(nome_personagem)
    elif(nome_personagem=="Obama"):
        jogando_com_personagem_3(nome_personagem)

#DEFINE CENARIO 1
def cenario_1(nome_personagem):
    print(" Tenho uma faca comigo \n")
    time.sleep(1)
    print(" Mas nao posso que deixem ver, se nao estaremos mortos \n")
    time.sleep(1)
    print("\n 'Mas podemos esperar a noite e cortar essas cordar e fugir pela mata'\n")
    time.sleep(1)
    print(" O que vamos fazer?\n")
    time.sleep(1)
    print(" (1) Cortar a corda agora mesmo - (2) Esperar a noite cair")
    decisao=input(f"\n Qual numero {nome_personagem} deve apertar?:  (1) (2)")
    while decisao!="1" and decisao!="2" :
        print(" Os exploradores nao tem essa opcao!!\n")
        time.sleep(2)
        decisao=input("Escolha entre as opcoes (1)  (2)")
    if(decisao=="1"):
        print("\n\n\n\n Os canibais viram, estao todos mortos!! ")
        valida_cenario=False
    elif(decisao=="1"):
        print("\n\n")
        print(" Sabia decisao, sera voce o novo Indiana Jones? \n")
        time.sleep(2)
        print("\n\n")
        valida_cenario=True
    return valida_cenario
#DEFINE CENARIO 2
def cenario_2(nome_personagem):
    time.sleep(3)
    print(" A noite cai, os exploradores conseguem cortar a cordas e fugir para a mata\n ")
    time.sleep(1)
    print(" Sao canibais dorminhocos\n ")
    time.sleep(4)
    print(" Famintos, eles encontram um fruto de cor viva, porem haviam espinhos no caule ")
    print(f" E {nome_personagem} como sabe um pouco de biologia precisa decidir se podem comer\n")
    time.sleep(2)
    decisao=input("(1) Podem comer - (2) Nao podem comer")
    while decisao!="1" and decisao!="2":
        print(" Opção não disponivel, escolha entre as opcoes (1) (2)\n")
        time.sleep(2)
        decisao=input("(1) Podem comer - (2) Nao pode comer")
    if(decisao=="1"):
        print("\n\n O fruto era extremamente venenoso, estao todos mortos")
        valida_cenario=False
    elif(decisao=="2"):
        print(" Uma decisao fria e calculada, seguimos com fome porem vivos. \n")
        time.sleep(2)
        valida_cenario=True
    return valida_cenario
#DEFINE CENARIO 3
def cenario_3(nome_personagem):
    print(" Fracos e cansados, feito largados e pelados\n")
    time.sleep(2)
    print(' Nossos exploradores precisam sair dessa ilha, os canibais ja estao em busca do seu almoco \n')
    time.sleep(1)
    print(f" E, {nome_personagem} Avista um penhasco de mais ou menos 100 mts de altura, e no fundo ha um lago" )
    print(" Parece ser o fim da linha\n")
    time.sleep(2)
    print(" Ou irao voltar para a mata?\n")
    time.sleep(3)
    print(f" Qual dificil decisao {nome_personagem} deve tomar agora? \n")
    time.sleep(3)
    decisao=input(" (1) Voltar para a mata (2) Pular do penhasco")
    while decisao!="1" and decisao!="2" :
        print(" Opção não disponivel, escolha entre as opcoes (1) (2) \n")
        time.sleep(2)
        decisao=input(" Escolha entre: (1) Voltar a mata (2) Pular do penhasco ")
    if(decisao=="1"):
        print("\n\n\n\n  A covardia nunca sera premiada, ao voltar a mata deram de cara com os canibais, os exploraores serao servidos ainda no Almoco \n ")
        valida_cenario=False
    elif(decisao=="2"):
        print(f"    A coragem deveria pautar nossas vidas e {nome_personagem} exala coragem   \n")
        print(" Os exploradores saltam, e conseguem sobreviver caindo na agua, e quando olham pra cima, la estavam os famintos canibais \n")
        time.sleep(2)
        print("\n\n")
        valida_cenario=True
    return valida_cenario
#DEFINE CENARIO FINAL
def cenario_Final(nome_personagem):
    print(" Os exploradores estao enfim, livres de serem degustados\n")
    time.sleep(2)
    print(" Mas, ainda nao estao a salvo \n")
    time.sleep(1)
    print(f"{nome_personagem}: Estamos famintos!! Cansados!! Precisamos sair logo daqui!! \n")
    time.sleep(1)
    print("Um dos exploraores diz que e melhor desitir e usar a faca para acabar com o sofrimento \n")
    print(f" Mas{nome_personagem} diz, NOS SOMOS EXPLORADORES!!!!! \n")
    time.sleep(2)
    print("A decisao agora e se vamos continuar ou desistir \n")
    time.sleep(3)
    decisao=input(" (1) Desistir   (2) Persistir")
    while decisao!="1" and decisao!="2" :
        print(" Opção não disponivel, escolha entre as opcoes (1) (2) \n")
        time.sleep(2)
        decisao = input(" Escolha entre: (1) Disistir (2) Persistir ")
    if(decisao=="1"):
        print("\n\n\n\n COVARDE!!!")
        time.sleep(1)
        print("Os personagens dao fim a propria vida utilizando a faca! ")
        valida_cenario=False
    elif(decisao=="2"):
        print(" Peristir, Persistir, nunca desistir, voce e um Resiliente !!")
        time.sleep(2)
        print("Os nossos exploradores encontram uma tribo amigavel, conseguem comida e abrigo, para conseguirem seguir o caminho")
        print("Nossos exploradores estao a salvo")
        print("\n\n")
        valida_cenario=True
    return valida_cenario
#DEFINE CENARIOS PARA O JOGADOR 1
def jogando_com_personagem_1(nome_personagem):
    fase_1=cenario_1(nome_personagem)
    if fase_1==True:
        fase_2=cenario_2(nome_personagem)
        if(fase_2==True):
            fase_3=cenario_3(nome_personagem)
            if (fase_3==True):
                fase_final=cenario_Final(nome_personagem)
                if(fase_final==True):
                    mensagem_vencedor()
                else:
                    mensagem_perdedor()
            else:
                mensagem_perdedor()
        else:
            mensagem_perdedor()
    else:
        mensagem_perdedor()
#DEFINE CENARIOS PARA PERSONAGEM 2
def jogando_com_personagem_2(nome_personagem):
    fase_1=cenario_2(nome_personagem)
    if fase_1==True:
        fase_2=cenario_1(nome_personagem)
        if(fase_2==True):
            fase_3=cenario_3(nome_personagem)
            if (fase_3==True):
                fase_final=cenario_Final(nome_personagem)
                if(fase_final==True):
                    mensagem_vencedor()
                else:
                    mensagem_perdedor()
            else:
                mensagem_perdedor()
        else:
            mensagem_perdedor()
    else:
        mensagem_perdedor()
#DEFINE CENARIOS PARA O JOGADOR 3
def jogando_com_personagem_3(nome_personagem):
    fase_1=cenario_1(nome_personagem)
    if fase_1==True:
        fase_2=cenario_3(nome_personagem)
        if(fase_2==True):
            fase_3=cenario_2(nome_personagem)
            if (fase_3==True):
                fase_final=cenario_Final(nome_personagem)
                if(fase_final==True):
                    mensagem_vencedor()
                else:
                    mensagem_perdedor()
            else:
                mensagem_perdedor()
        else:
            mensagem_perdedor()
    else:
        mensagem_perdedor()
def mensagem_perdedor():
    print("\n//////////////// VOCÊ PERDEU !! ")
    time.sleep(3)
    reinicio=input("Deseja jogar novamente? (1) Sim (2) Não: ")
    if(reinicio=="1"):
        andamento_do_jogo()
    elif(reinicio=="2"):
        print("FIM DO JOGO")
    else:
        mensagem_perdedor()

def andamento_do_jogo():
    continua=abertura()

    if continua==True:
        opcao=escolha_personagem()
        jogar(opcao)
    else:
        print("FIM DO JOGO")

andamento_do_jogo()
