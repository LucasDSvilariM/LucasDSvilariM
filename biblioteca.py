def piramide(n):
    for i in range(1,n+1):
        for x in range(i):
            print(i, end=" ")
        print()
def piramide2(n):
    for i in range(n+1):
        for x in range(1,i+1):
            print(x, end=" ")
        print()

def vogais(txt):
    cont = 0
    for x in txt:
        if x in "aeiouAEIOU":
            cont+=1
    print(f"O texto tem {cont} vogais")

usuarios = []
senhas = []
senha_bloqueada = False


def cadastrar_usuario():
    while True:
        usuario = input("Digite o seu usuário: ")
        if usuario in usuarios:
            print("Usuário já cadastrado!")
        else:
            senha = input("Digite uma senha: ")
            usuarios.append(usuario)
            senhas.append(senha)
            print("Cadastro feito com sucesso!")

        dnv = int(input("Você deseja cadastrar mais um usuário?\n(1 - sim // 2 - não): "))
        if dnv != 1:
            break


def login():
    global senha_bloqueada
    tentativa = 3
    while tentativa > 0:
        usuario = input("Digite o nome de usuário: ")

        if senha_bloqueada:
            print("A senha está bloqueada. Programa encerrado.")
            return  # Encerra a função login

        if usuario in usuarios:
            indice = usuarios.index(usuario)
            for _ in range(tentativa):
                senha = input("Digite sua senha: ")
                if senhas[indice] == senha:
                    print(f"Bem-vindo, {usuario}!")
                    return
                else:
                    tentativa -= 1
                    print(f"Senha incorreta. Você tem {tentativa} tentativas restantes.")
            print("Número máximo de tentativas alcançado. Senha bloqueada.")
            senha_bloqueada = True  # Bloqueia a senha
            return
        else:
            print("Usuário não encontrado.")
            return

def mostrar():
    print("Os usuários cadastrados e suas senhas são: ")
    for i in range(len(usuarios)):
        print(f"Usuário: {usuarios[i]} e Senha: {senhas[i]}")


def menu():
    while True:
        print(f"BEM VINDO!!\n"
              f"DIGITE 1 PARA REALIZAR CADASTRO\n"
              f"DIGITE 2 PARA REALIZAR LOGIN\n"
              f"DIGITE 3 PARA MOSTRAR OS USUÁRIOS\n"
              f"DIGITE 4 PARA SAIR\n")

        entrada = int(input("Digite a opção que deseja executar: "))
        if entrada == 1:
            cadastrar_usuario()
        elif entrada == 2:
            login()
            if senha_bloqueada:
                print("Programa encerrado.")
                break  # Encerra o loop do menu se a senha estiver bloqueada
        elif entrada == 3:
            mostrar()
        elif entrada == 4:
            print("Encerrado")
            break  # Encerra a execução do programa
        else:
            print("Opção inválida")


# Iniciar o programa

class pessoa:
    def __init__(self, nome):
       self.nome = nome
       self.comendo = False
       self.falando = False
       self.dormindo = False

    def comer(self):
        if not self.comendo:
            self.comendo = True
            print(f"{self.nome} começou a comer.")
        else:
            print(f"{self.nome} já estava comendo.")
        if self.comendo:
            self.comendo =False
            print(f"{self.nome} parou de comer para falar")
        else:
            print(f"{self.nome} já se alimentou, começou a falar")

    def falar(self):
        if not self.falando:
            self.falando = True
            print(f"{self.nome} agora está falando.")
        else:
            print(f"{self.nome} já estava falando.")
        if self.falando:
            self.falando = False
            print(f"{self.nome} agora parou de falar.")
        else:
            print(f"{self.nome} não quer mais falar.")

    def dormir(self):
        if not self.dormindo:
            self.dormindo = True
            print(f"{self.nome} foi dormir.")
        else:
            print(f"{self.nome} já estava dormindo.")
        if self.dormindo:
            self.dormindo = False
            print(f"{self.nome} acordou.")
        else:
            print(f"{self.nome} já estava acordado.")

class vendedor:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0

    def vendeu(self, vendas):
        self.vendas = vendas

    def bateu_meta(self, meta):
        if self.vendas >= meta:
            print(f"Vendedor {self.nome} bateu meta")
        else:
            print(f"Vendedor {self.nome} não bateu meta")

class animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        if not self.comer:
            self.comer = True
        print(f"{self.nome} foi comer")

class gato(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f"O {self.nome} está miando...")

class Vaquinha(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def mugir(self):
        print(f"{self.nome} está mugindo")

class Cachorro(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def latir(self):
        print(f"{self.nome} está latindo")

class coelho(animal):
    def __init__(self,nome,cor):
        super().__init__(nome, cor)
    def pulando(self):
        print(f"{self.nome} está pulando")

class atleta():
    def __init__(self,nome, peso):
        self.nome = nome
        self.peso = peso
        self.aposentado = False
        self.aquecido = False

    def aquecer(self):
        if self.aquecido == False:
            print(F"O {self.nome} foi aquecer.")
            self.aquecido = True
    def aposentar(self):
        if self.aposentado:
            print(f"{self.nome} foi aposentado")
            self.aposentado = True
class corredor(atleta):
    def __init__(self,nome,peso):
        super().__init__(nome, peso)
    def correr(self):
        if self.aquecido == True:
            if self.aposentado == False:
                print(f"O {self.nome} foi correr.")
            else:
                print(f"O {self.nome} não pode correr, porque está aposentado.")
        else:
            print(f"O {self.nome} não pode correr, porque não aqueceu.")

    def aposentou(self):
        if self.aquecido == False:
            if self.aposentado == True:
                print(f"O {self.nome} está aposentado.")
            else:
                print(f"O {self.nome} não pode aquecer, porque está aposentado.")
        else:
            print(f"O {self.nome} já está aposentado.")
