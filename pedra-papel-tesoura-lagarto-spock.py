# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 17:13:43 2015

@author: Vitor
"""
from random import randint
print("Bem-vindo ao jogo Pedra-papel-tesoura-lagarto-Spock")
lista= ["pedra", "papel", "tesoura", "lagarto", "spock"]
placar_com=0 
placar_p1=0
while placar_com <= 3 or placar_p1 <= 3:
    escolha_p1.lower= (input("Escolha sua arma"))
    escolha_com= random.choice(lista)
    if escolha_p1== "pedra" and escolha_com== "pedra"
        print("Deu empate! Jogue novamente. Placar: P1 %d x Com %d" (placar_p1, placar_com))
    elif escolha_p1== "spock" and escolha_com== "spock":
       print("Deu empate! Jogue novamente. Placar: P1 %d x Com %d" (placar_p1, placar_com)
    elif escolha_p1== "papel" and escolha_com== "papel":
        print("Deu empate! Jogue novamente. Placar: P1 %d x Com %d" (placar_p1, placar_com)
    elif escolha_p1== "tesoura" and escolha_com== "tesoura":
        print("Deu empate! Jogue novamente. Placar: P1 %d x Com %d" (placar_p1, placar_com)
    elif escolha_p1== "lagarto" and or escolha_com== "lagarto":
         print("Deu empate! Jogue novamente. Placar: P1 %d x Com %d" (placar_p1, placar_com)
    elif escolha_p1== "pedra" and (escolha_com== "tesoura" or escolha_com== "lagarto"):
         placar_p1= placar_p1+1
         print("Voce venceu a batalha! Placar: P1 %d x Com %d" (placar_p1, placar_com)
    elif escolha_p1== "pedra" and (escolha_com== "spock" or escolha_com== "papel"):
         placar_p1= 0 and placar_com= placar_com+1
         print("Voce perdeu a batalha! Placar: P1 %d x Com%d" (placar_p1, placar_com)
    elif escolha_p1== "papel" and (escolha_com== "spock" or escolha_com== "pedra"):
          placar_com= 0 and placar_p1= placar_p1+1
         print("Voce venceu a batalha! Placar: P1 %d x Com %d" (placar_p1, placar_com)
    elif escolha_p1== "papel" and (escolha_com== "tesoura" or escolha_com== "lagarto"):
         placar_p1= 0 and placar_com= placar_com+1
         print("Voce perdeu a batalha! Placar: P1 %d x Com%d" (placar_p1, placar_com)
    elif escolha_p1== "lagarto" and (escolha_com== "papel" or escolha_com== "spock"):
         placar_com= 0 and placar_p1= placar_p1+1
         print("Voce venceu a batalha! Placar: P1 %d x Com %d" (placar_p1, placar_com)
    elif escolha_p1== "lagarto") and (escolha_com== "tesoura"or escolha_com== "pedra"):
          placar_p1= 0 and placar_com= placar_com+1
         print("Voce perdeu a batalha! Placar: P1 %d x Com%d" (placar_p1, placar_com)
    elif escolha_p1== "spock") and (escolha_com== "pedra" or escolha_com== "tesoura"):
         placar_com= 0 and placar_p1= placar_p1+1
         print("Voce venceu a batalha! Placar: P1 %d x Com %d" (placar_p1, placar_com)
    elif escolha_p1== "spock") and (escolha_com== "papel" or escolha_com== "lagarto"):
          placar_p1= 0 and placar_com= placar_com+1
         print("Voce perdeu a batalha! Placar: P1 %d x Com%d" (placar_p1, placar_com)
    elif  escolha_p1== "tesoura") and (escolha_com== "lagarto" or escolha_com== "papel"):
         placar_com= 0 and placar_p1= placar_p1+1
         print("Voce venceu a batalha! Placar: P1 %d x Com %d" (placar_p1, placar_com)
    elif escolha_p1== "tesoura") and (escolha_com== "pedra" or escolha_com== "spock"):
         placar_p1= 0 and placar_com= placar_com+1
         print("Voce perdeu a batalha! Placar: P1 %d x Com%d" (placar_p1, placar_com)
     elif escolha_p1 != "spock" or escolha_p1 != "lagarto" or escolha_p1 != "papel" or escolha_p1 != "tesoura" or escolha_p1 != "pedra"
     print("Comando inválido. Por favor, digite uma arma conhecida.")
         if placar_p1== 3:
             break 
         print("Voce derrotou o inimigo e venceu a guerra, Parabens!")
         if placar_com== 3:
             break
         print("Seu inimigo o derrotou. Recupere-se e volte a guerra!")