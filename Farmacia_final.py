#!/usr/bin/env python
# coding: utf-8

# Projeto: POO
# 
# Grupo: 03
# 
# Nomes:
# 
#       Antonio Henrique Sales Resende Jorge
#       Fabio Barbosa Pinto
#       Leandro Gonçalves Lima
#       Lorrane Cristina Cardozo Bonfim Oliveira
# 
# 

# In[12]:


from datetime import datetime

IDADE_IDOSO = 65

class Cliente:
    lista_cliente = []

    def __init__(self, cpf: str, nome: str, data_nascimento: str)-> None:
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.desconto_idoso = verificar_idoso(datetime.strptime(data_nascimento, '%d/%m/%Y'))
        Cliente.lista_cliente.append(self)

    def __repr__(self) -> str:
        representacao = f"CPF: {self.cpf}, Nome: {self.nome}, Data de Nascimento: {self.data_nascimento}"
        return representacao

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        if len(cpf) != 11:
            print("CPF não é valido.")
        else:
            self._cpf = cpf

    def buscar_cpf(cpf):
        cliente_buscado = None
        for cliente in Cliente.lista_cliente:
            if cpf == cliente.cpf:
                cliente_buscado = cliente
        return cliente_buscado

class Laboratorio:
    lista_de_laboratorios = []
    def __init__(self, nome: str, endereco: str, telefone:int, cidade: str, estado: str)-> None:
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado
        Laboratorio.lista_de_laboratorios.append(self)

    def __repr__(self):
        representacao = f"Laboratorio {self.nome}, tel: {self.telefone}"
        return representacao

    def buscar_laboratorio(nome_laboratorio):
        laboratorio_buscado = None
        for lab in Laboratorio.lista_de_laboratorios:
          if nome_laboratorio == lab.nome:
            laboratorio_buscado = lab
        return laboratorio_buscado

class Medicamento:
    lista_de_medicamentos = []
    id_med = 1
    def __init__(self, nome: str, composto: str, laboratorio:Laboratorio, descricao: str, preco: float)-> None:
        self.nome = nome
        self.composto = composto
        self.laboratorio = laboratorio
        self.descricao = descricao
        self.preco = preco
        self.id_med = Medicamento.id_med
        Medicamento.id_med += 1
        Medicamento.lista_de_medicamentos.append(self)

    def __repr__(self):
        representacao = f"ID: {self.id_med} - Nome: {self.nome} - Preço: {self.preco}"
        return representacao


    def buscar_medicamento(id_med):
        if id_med == 0:
           return 0
        else:
          medicamento_buscado = None
          for medicamento in Medicamento.lista_de_medicamentos:
              if id_med == medicamento.id_med:
                  medicamento_buscado = medicamento
          return medicamento_buscado

class MedicamentoFitoterapico(Medicamento):
    lista_de_fitos = []
    def __init__(self, nome: str, composto: str, laboratorio:Laboratorio, descricao: str, preco: float)-> None:
        super().__init__(nome,composto,laboratorio,descricao,preco)
        MedicamentoFitoterapico.lista_de_fitos.append(self)

class MedicamentoQuimioterapico(Medicamento):
    lista_de_quimios = []
    def __init__(self, nome: str, composto: str, laboratorio: Laboratorio, descricao: str, necessita_receita: str, preco : float)-> None:
        super().__init__(nome, composto, laboratorio, descricao,preco)
        self.necessita_receita = necessita_receita
        MedicamentoQuimioterapico.lista_de_quimios.append(self)

class Venda:
    vendas_realizadas = {}
    ganhos_totais = 0
    clientes_atendidos = []
    quantidade_do_medicamento = {}
    remedios_vendidos = []
    def __init__(self, data_hora: datetime, cliente: Cliente)-> None:
        self.data_hora = data_hora
        self.cliente = cliente
        if self.cliente.nome not in Venda.clientes_atendidos:
            Venda.clientes_atendidos.append(self.cliente.nome)


    def remedio_mais_vendido():
        count_mais_vendido = 0
        nome_mais_vendido = 0
        for medic in Venda.quantidade_do_medicamento:
          if Venda.quantidade_do_medicamento[medic] > count_mais_vendido:
              count_mais_vendido = Venda.quantidade_do_medicamento[medic]
              nome_mais_vendido = medic
          else:
              pass
        return nome_mais_vendido

    def somar_ao_ganhos_totais(valor):
        Venda.ganhos_totais += valor

def verificar_idoso(data: datetime):
    if (datetime.today().year - data.year - ((datetime.today().month, datetime.today().day) < (data.month, data.day))) >= IDADE_IDOSO:
      return True
    else:
      return False

def cadastrar_cliente():
    cpf = input("CPF do cliente: ")
    nome = input("Nome do cliente: ")
    data_nascimento = input("Data de nascimento do cliente: ")
    Cliente(cpf, nome, data_nascimento)
    print("Cliente cadastrado com sucesso.")

def cadastrar_medicamento(Laboratorio):
    nome = input("Nome do medicamento: ")
    composto = input("Principal composto do medicamento: ")
    laboratorio = Laboratorio
    descricao = input("Descrição do medicamento: ")
    preco = float(input("Preço do medicamento: "))
    opcao = input('Digite Q para QUIMIOTERÁOICO  e F para FITOTERÁPICO: ').lower()
    if opcao == 'q':
      necessita_receita = input("Necessita de receita? (S/N): ").lower()
      medicamento = MedicamentoQuimioterapico(nome, composto, laboratorio, descricao, necessita_receita,preco)
      print("Medicamento quimioterápico cadastrado com sucesso.")
    elif opcao == 'f':
      medicamento = MedicamentoFitoterapico(nome, composto, laboratorio, descricao,preco)
      print("Medicamento fitoterápico cadastrado com sucesso.")

def cadastrar_laboratorio():
    nome = input("Nome do laboratório: ")
    endereco = input("Endereço do laboratório: ")
    telefone = input("Telefone do laboratório: ")
    cidade = input("Cidade do laboratório: ")
    estado = input("Estado do laboratório: ")
    laboratorio = Laboratorio(nome, endereco, telefone, cidade, estado)
    print("Laboratório cadastrado com sucesso.")
    return laboratorio

def efetuar_venda():
    compra = []
    fmt = "{:15}|{:^15}|R$ {:<10.2f}"
    comprador = Cliente.buscar_cpf(input("CPF do cliente: "))
    preco_final = 0
    if comprador is None:
        print("Cliente não encontrado.")
        return
    else:
        while True:
            print("\nListagem de Medicamentos:")
            for medicamento in Medicamento.lista_de_medicamentos:
                print(medicamento)
            produto = Medicamento.buscar_medicamento(int(input("Digite o ID do medicamento(Digite '0' para encerrar as vendas): ")))

            if produto == 0:
                break
            elif produto != None:
                quantidade = input('entre com a quantidade - ')
                compra.append((produto.nome,int(quantidade),int(quantidade)*produto.preco,f"{datetime.today().day}/{datetime.today().month}/{datetime.today().year}"))
                if produto.nome in Venda.quantidade_do_medicamento:
                    Venda.quantidade_do_medicamento[produto.nome] += int(quantidade)
                else:
                    Venda.quantidade_do_medicamento[produto.nome] = int(quantidade)
                    Venda.remedios_vendidos.append(produto)
                preco_final += int(quantidade)*produto.preco
            else:
                print("Produto não encontrado.")

    if comprador.cpf in Venda.vendas_realizadas:
        Venda.vendas_realizadas[comprador.cpf].append(compra)
    else:
        Venda.vendas_realizadas[comprador.cpf] = compra

    print('Cliente: {:<45}'.format(comprador.cpf))
    print('-------------------------------------------')
    print('{:15}|{:^15}|R$ {:<10}'.format('Produtos','Quantidade','Valor'))
    print('-------------------------------------------')
    for i, j, k, l_ in compra:
        print(fmt.format(i,j,k))
    print('-------------------------------------------')
    print('{:<31}|R$ {:<.2f}'.format('Sub_TOTAL',preco_final))
    print('-------------------------------------------')
    if comprador.desconto_idoso == True:
        preco_final = preco_final * 0.8
        print(f'Com desconto, o valor da venda foi para {preco_final:.2f}!')
    elif preco_final > 150:
        preco_final = preco_final * 0.9
        print(f'Com desconto, o valor da venda foi para {preco_final:.2f}!')
    else:
        print(f"O valor da venda {preco_final:.2f}")
    Venda(datetime.today(),comprador)
    Venda.somar_ao_ganhos_totais(preco_final)


def emitir_relatorios():
    # Listagem de clientes em ordem alfabética
    print("\nListagem de Clientes:")
    for cliente in sorted(Cliente.lista_cliente, key=lambda x: x.nome):
        print(cliente)

    # Listagem de medicamentos em ordem alfabética
    print("\nListagem de Medicamentos:")
    for medicamento in sorted(Medicamento.lista_de_medicamentos, key=lambda x: x.nome):
        print(f"Nome: {medicamento.nome}, Composto: {medicamento.composto}, Laboratório: {medicamento.laboratorio.nome}")

    # Listagem de medicamentos quimioterápicos
    print("\nListagem de Medicamentos Quimioterápicos:")
    for medicamento in MedicamentoQuimioterapico.lista_de_quimios:
        necessita_receita = "Sim" if medicamento.necessita_receita else "Não"
        print(f"Nome: {medicamento.nome}, Laboratório: {medicamento.laboratorio.nome}, Necessita Receita: {necessita_receita}")

    print("\nListagem de Medicamentos Fitoterápicos:")
    for medicamento in MedicamentoFitoterapico.lista_de_fitos:
        print(f"Nome: {medicamento.nome}, Laboratório: {medicamento.laboratorio.nome}")

    # Estatísticas dos atendimentos
    total_pessoas_atendidas = len(Venda.clientes_atendidos)
    total_vendas = len(Venda.vendas_realizadas)
    med_mais_vendido = Venda.remedio_mais_vendido()
    total_qt_quimioterapicos = sum(1 for venda in Venda.remedios_vendidos if isinstance(venda, MedicamentoQuimioterapico))
    total_valor_quimioterapicos = sum(float(remedio.preco*Venda.quantidade_do_medicamento[remedio.nome]) for remedio in Venda.remedios_vendidos if isinstance(remedio, MedicamentoQuimioterapico))
    total_qt_fitoterapicos = sum(1 for venda in Venda.remedios_vendidos if isinstance(venda, MedicamentoFitoterapico))
    total_valor_fitoterapicos = sum(float(remedio.preco*Venda.quantidade_do_medicamento[remedio.nome]) for remedio in Venda.remedios_vendidos if isinstance(remedio, MedicamentoFitoterapico))

    print("\nEstatísticas dos Atendimentos:")
    print(f"Total de pessoas atendidas: {total_pessoas_atendidas}")
    print(f"Total de vendas realizadas: {total_vendas}")
    print(f'Remédio mais vendido do dia: {med_mais_vendido}')
    print(f"Total de medicamentos quimioterápicos vendidos: {total_qt_quimioterapicos} (Valor Total: R${total_valor_quimioterapicos:.2f})")
    print(f"Total de medicamentos fitoterápicos vendidos: {total_qt_fitoterapicos} (Valor Total: R${total_valor_fitoterapicos:.2f})")

Cliente('12345678911', "Lorrane",'15/08/1945')
Cliente('11111111111','Antonio',"25/02/1930")
bronstein = Laboratorio('Bronstein','Rua joaquin','2188994545','Rio de Janeiro','RJ')
medley = Laboratorio('Medley','Rua Sao Paulo', '1196658741', 'Sao Paulo', 'SP')
MedicamentoFitoterapico('Neosaldina','N',bronstein, 'Dor de cabeça', 10.99)
MedicamentoQuimioterapico('Calmix','NaCl', medley, 'Para ansiedade', 'Sim', 40.00,)
MedicamentoFitoterapico('Eno','Es',medley, 'Para dor de estomago', 5.00)
MedicamentoQuimioterapico("Quimex",'Au',bronstein,'Para cancer', 'Sim', 100.00)

while True:
    print("\nMenu:")
    print("1. Cadastrar Cliente")
    print("2. Cadastrar Medicamento")
    print("3. Cadastrar Laboratório")
    print("4. Efetuar Venda")
    print("5. Emitir Relatórios")
    print("6. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_cliente()
    elif opcao == '2':
        laboratorio = Laboratorio.buscar_laboratorio(input('De qual laboratorio é o medicamento? '))
        if laboratorio != None:
            pass
        else:
            print('Laboratorio ainda não cadastrado, por favor cadastre-o')
            laboratorio = cadastrar_laboratorio()
        cadastrar_medicamento(laboratorio)
    elif opcao == '3':
        cadastrar_laboratorio()
    elif opcao == '4':
        efetuar_venda()
    elif opcao == '5':
        emitir_relatorios()
    elif opcao == '6':
        print("Saindo...")
        break
    else:
        print("Opção inválida.")


# In[9]:


Venda.vendas_realizadas


# In[ ]:




