# _*_ coding: utf-8 _*

Nascimento = "19 de agosto de 2018"
Pai_do_Junior = "Gustavo Soares de Lima"

class Familia:
    def Parente(Membro):
        if Membro == Pai:
            print("Meu pai é",Pai_do_Junior)

class Omega:
    def Iniciar():
        print("Olá, meu nome é Junior")
    def Desligar():
        print("Vou desligar, tchau!")

Omega.Iniciar()
Pai = ""
Familia.Parente(Pai)
Omega.Desligar()
