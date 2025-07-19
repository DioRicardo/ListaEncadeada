#RU: 4751823 - Dio Ricardo
class CartaoNumerado:
    def __init__(self, cor, numero):
        self.numero = numero
        self.cor = cor
        self.proximo = None

    def __str__(self):
        return f"[{self.cor}, {self.numero}]"

#Exigência de código 1 de 7
class ListaEspera:
    def __init__(self):
        self.head = None
        self.ordA = 201
        self.ordV = 1

    #Exigência de código 2 de 7
    def inserirSemPrioridade(self, paciente):
        if self.head is None:
            self.head = paciente
            return

        pacienteAtual = self.head
        while pacienteAtual.proximo != None:
            pacienteAtual = pacienteAtual.proximo

        pacienteAtual.proximo = paciente
        return

    #Exigência de código 3 de 7
    def inserirComPrioridade(self, paciente):
        if self.head is None:
            self.head = paciente
            return

        if self.head.cor == "V":
            paciente.proximo = self.head
            self.head = paciente
            return

        pacienteAnterior = self.head
        pacienteAtual = self.head.proximo

        while pacienteAtual != None and pacienteAtual.cor != "V":
            pacienteAnterior = pacienteAtual
            pacienteAtual = pacienteAtual.proximo

        pacienteAnterior.proximo = paciente
        paciente.proximo = pacienteAtual
        return

    #Exig&encia de código 4 de 7
    def inserir(self):
        cor = input("Informe a cor do cartão (A/V): ").upper()
        if cor == "A":
            self.inserirComPrioridade(CartaoNumerado(cor, self.ordA))
            self.ordA += 1
        elif cor == "V":
            self.inserirSemPrioridade(CartaoNumerado(cor, self.ordV))
            self.ordV += 1
        else:
            raise Exception("Cor escolhida inválida.")

    #Exigência de código 5 de 7
    def imprimirListaEspera(self):
        if self.head is None:
            print("Ninguém na fila...")
            return

        pacienteAtual = self.head
        print("Lista de espera -> ", end="")
        while pacienteAtual != None:
            print(f"{pacienteAtual} -> ", end="")
            pacienteAtual = pacienteAtual.proximo
        print("Fim da lista...")

    #Exigência de código 6 de 7
    def atenderPaciente(self):
        if self.head is None:
            print("Não há ninguém na fila!")
            return


        pacienteAtendido = self.head
        print(f"Atendendo o paciente com cartão cor {pacienteAtendido.cor} e número {pacienteAtendido.numero}.")

        self.head = pacienteAtendido.proximo

        del(pacienteAtendido)


listaDeEspera = ListaEspera()

#Exigência de código 7 de 7
while True:
    print("1 - adicionar paciente a fila")
    print("2 - mostrar pacientes na fila")
    print("3 - chamar paciente")
    print("4 - sair")

    op = int(input("Digite uma opção para iniciar:"))

    if op == 1:
        listaDeEspera.inserir()
    elif op == 2:
        listaDeEspera.imprimirListaEspera()
    elif op == 3:
        listaDeEspera.atenderPaciente()
    elif op == 4:
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida. Selecione outra opção!\n")
