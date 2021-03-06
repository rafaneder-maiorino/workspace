# -*- coding: utf-8 -*-
"""# CLASSES AUXILIARES"""

######################## CLASSES AUXILIARES ########################
class TipoDePessoa():
  def __init__(self, tipo_de_pessoa):
    if (tipo_de_pessoa != 'JURIDICA' and tipo_de_pessoa != 'FISICA'):
      print('ERRO - VALORES PERMITIDOS PARA PESSOA: "JURIDICA" E "FISICA".')
    else:
      self.tipo_de_pessoa = tipo_de_pessoa

  def GET_tipo_de_pessoa(self):
    return self.tipo_de_pessoa    

class TipoDeOperacao():
  def __init__(self, tipo_de_operacao):
    if (tipo_de_operacao != 'MOVIMENTACAO' and tipo_de_operacao != 'CONSULTAR_SALDO' and tipo_de_operacao != 'EMITIR_EXTRATO' and tipo_de_operacao != 'SAIR' and tipo_de_operacao != 'CRIAR_CONTA'):
      print('ERRO - VALORES PERMITIDOS PARA TIPO DE OPERAÇÃO: "MOVIMENTACAO", "CONSULTAR_SALDO", "EMITIR_EXTRATO" E "SAIR".')
    else:
      self.tipo_de_operacao = tipo_de_operacao

  def GET_tipo_de_operacao(self):
    return self.tipo_de_operacao   

class TipoDeConta():
  def __init__(self, tipo_de_conta):
    if (tipo_de_conta != 'POUPANCA' and tipo_de_conta != 'CORRENTE' and tipo_de_conta != 'SALARIO' and tipo_de_conta != 'UNIVERSITARIA' and tipo_de_conta != 'DIGITAL'):
      print('ERRO - VALORES PERMITIDOS PARA TIPO DE CONTA: "POUPANCA", "CORRENTE", "SALARIO", "UNIVERSITARIA" E "DIGITAL".')
    else:
      self.tipo_de_conta = tipo_de_conta

  def GET_tipo_de_conta(self):
    return self.tipo_de_conta

class StatusDaConta():
  def __init__(self, status_da_conta):
    if (status_da_conta != 'ATIVO' and status_da_conta != 'INATIVO'):
      print('ERRO - VALORES PERMITIDOS PARA PESSOA: "ATIVO" E "INATIVO".')
    else:
      self.status_da_conta = status_da_conta

  def GET_status_da_conta(self):
    return self.status_da_conta   

class TipoDeMovimentacao():
  def __init__(self, tipo_movimentacao):
    if (tipo_movimentacao != 'DEPOSITO' and tipo_movimentacao != 'SAQUE'):
      print('ERRO - VALORES PERMITIDOS PARA TIPO DE OPERAÇÃO: "DEPOSITO", "SAQUE".')
    else:
      self.tipo_movimentacao = tipo_movimentacao

  def GET_tipo_movimentacao(self):
    return self.tipo_movimentacao

"""# POPULANDO CLASSES AUXILIARES"""

######################## POPULANDO CLASSES AUXILIARES ########################

vet_TipoDePessoa = ['FISICA', 'JURIDICA']
vet_TipoDePessoa[0] = TipoDePessoa(vet_TipoDePessoa[0])
vet_TipoDePessoa[1] = TipoDePessoa(vet_TipoDePessoa[1])

vet_TipoDeOperacao = ['MOVIMENTACAO', 'CONSULTAR_SALDO', 'EMITIR_EXTRATO', 'SAIR', 'CRIAR_CONTA']
vet_TipoDeOperacao[0] = TipoDeOperacao(vet_TipoDeOperacao[0])
vet_TipoDeOperacao[1] = TipoDeOperacao(vet_TipoDeOperacao[1])
vet_TipoDeOperacao[2] = TipoDeOperacao(vet_TipoDeOperacao[2])
vet_TipoDeOperacao[3] = TipoDeOperacao(vet_TipoDeOperacao[3])
vet_TipoDeOperacao[4] = TipoDeOperacao(vet_TipoDeOperacao[4])

vet_TipoDeConta = ['POUPANCA', 'CORRENTE', 'SALARIO', 'UNIVERSITARIA', 'DIGITAL']
vet_TipoDeConta[0] = TipoDeConta(vet_TipoDeConta[0])
vet_TipoDeConta[1] = TipoDeConta(vet_TipoDeConta[1])
vet_TipoDeConta[2] = TipoDeConta(vet_TipoDeConta[2])
vet_TipoDeConta[3] = TipoDeConta(vet_TipoDeConta[3])
vet_TipoDeConta[4] = TipoDeConta(vet_TipoDeConta[4])

vet_StatusDaConta = ['ATIVO', 'INATIVO']
vet_StatusDaConta[0] = StatusDaConta(vet_StatusDaConta[0])
vet_StatusDaConta[1] = StatusDaConta(vet_StatusDaConta[1])

vet_TipoDeMovimentacao = ['DEPOSITO', 'SAQUE']
vet_TipoDeMovimentacao[0] = TipoDeMovimentacao(vet_TipoDeMovimentacao[0])
vet_TipoDeMovimentacao[1] = TipoDeMovimentacao(vet_TipoDeMovimentacao[1])

"""# CLASSES PRINCIPAIS"""

######################## OPERAÇÃO ########################
class Operacao(TipoDeOperacao):
  def __init__(self, tipo_de_operacao_FK, conta_FK):
    self.tipo_de_operacao_FK = tipo_de_operacao_FK
    self.conta_FK = conta_FK

  def GET_tipo_de_operacao_FK(self):
    return self.tipo_de_operacao_FK
  
  def GET_conta_FK(self):
    return self.conta_FK


######################## CLIENTE ########################
class Cliente(TipoDePessoa):
  def __init__(self, nome, tipo_de_pessoa_FK, documento, email, telefone, endereco):
    self.nome = nome
    self.tipo_de_pessoa_FK = tipo_de_pessoa_FK
    self.documento = documento
    self.email = email
    self.telefone = telefone
    self.endereco = endereco

  def GET_nome(self):
    return self.nome

  def GET_tipo_de_pessoa_FK(self):
    return self.tipo_de_pessoa_FK

  def GET_documento(self):
    return self.documento

  def GET_email(self):
    return self.email

  def GET_telefone(self):
    return self.telefone

  def GET_endereco(self):
    return self.endereco


######################## CONTA ########################
class Conta(TipoDeConta, StatusDaConta, Cliente):
  def __init__(self, numero_conta, agencia, tipo_de_conta_FK, saldo, status_da_conta_FK, documento_cliente_FK):
    self.numero_conta = numero_conta
    self.agencia = agencia
    self.tipo_de_conta_FK = tipo_de_conta_FK
    self.saldo = saldo
    self.status_da_conta_FK = status_da_conta_FK
    self.documento_cliente_FK = documento_cliente_FK

  def SET_novo_saldo(self, saldo):
    self.saldo = saldo

  def GET_numero_conta(self):
    return self.numero_conta

  def GET_agencia(self):
    return self.agencia

  def GET_tipo_de_conta_FK(self):
    return self.tipo_de_conta_FK

  def GET_saldo(self):
    return self.saldo

  def GET_status_da_conta_FK(self):
    return self.status_da_conta_FK

  def GET_documento_cliente_FK(self):
    return self.documento_cliente_FK


######################## MOVIMENTAÇÃO ########################
class Movimentacao(TipoDeMovimentacao, Conta):
  def __init__(self, tipo_movimentacao_FK, data, valor, descricao, conta_FK, saldo_suficiente, ID_movimentacao):
    self.tipo_movimentacao_FK = tipo_movimentacao_FK
    self.data = data
    self.valor = valor
    self.descricao = descricao
    self.conta_FK = conta_FK
    self.saldo_suficiente = saldo_suficiente
    self.ID_movimentacao = ID_movimentacao

  def GET_tipo_movimentacao_FK(self):
    return self.tipo_movimentacao_FK

  def GET_data(self):
    return self.data

  def GET_valor(self):
    return self.valor

  def GET_descricao(self):
    return self.descricao

  def GET_conta_FK(self):
    return self.conta_FK

  def GET_saldo_suficiente(self):
    return self.saldo_suficiente

  def GET_ID_movimentacao(self):
    return self.ID_movimentacao

######################## HISTORICO DE MOVIMENTAÇÃO ########################
class HistoricoDeMovimentacao(Movimentacao):
  def __init__(self, movimentacao_FK, saldo_anterior, saldo_atual, conta_FK, data_FK):
    self.movimentacao_FK = movimentacao_FK
    self.saldo_anterior = saldo_anterior
    self.saldo_atual = saldo_atual
    self.conta_FK = conta_FK
    self.data_FK = data_FK

  def GET_movimentacao_FK(self):
    return self.movimentacao_FK

  def GET_saldo_anterior(self):
    return self.saldo_anterior

  def GET_saldo_atual(self):
    return self.saldo_atual

  def GET_conta_FK(self):
    return self.conta_FK

  def GET_data_FK(self):
    return self.data_FK

"""# LISTAS PARA ARMAZENAMENTO DE DADOS"""

######################## LISTAS PARA ARMAZENAMENTO DE DADOS ########################
vet_Contas = []
vet_Movimentacoes = []
vet_Historicos = []
vet_Clientes = []

"""# SIMULADOR"""

######################## BANK SIMULADOR ########################
import datetime
from datetime import date
from datetime import datetime
# INICIO #
print('Começando simulação..\n')

print('Bem Vindo ao Banco QSD (Queremos Seu Dinheiro)!')

# conta_atual = input('DIGITE O NÚMERO DA CONTA:')
# i = 0

operacao_atual = input('\nOPERAÇÕES:\n'
                       '0 - Fechar Conta\n'
                       '1 - Movimentação\n'
                       '2 - Consultar Saldo\n'
                       '3 - Emitir Extrato\n'
                       '4 - Sair\n'
                       '5 - Criar Conta\n'
                       'DIGITE O CÓDIGO DA OPERAÇÃO DESEJADA:')

while operacao_atual not in ('0', '1', '2', '3', '4', '5'):
    operacao_atual = input('CÓDIGO DE OPERAÇÃO INVALIDO! '
                         'DIGITE NOVAMENTE:')
if operacao_atual == '0':
  conta_a_ser_fechada = input('DIGITE O NÚMERO DA CONTA A SER FECHADA:')
  i=0
  conta_existente = 0
  
  while i < len(vet_Contas):
      if conta_a_ser_fechada == vet_Contas[i].GET_numero_conta():  
        id_conta = i  
        conta_existente = conta_existente + 1
      i=i+1

  if conta_existente == 0:
    print('Verifique os dados!\nNúmero de Conta não registrado.')
  else:
    print('Fechando Conta...')
    vet_Contas.pop(id_conta)
    print('Sua conta não existe mais em nosso registro!')

    
if operacao_atual == '1':
  tipo_movimentacao_atual = input('\nMOVIMENTAÇÕES:\n'
                       '1 - Depósito\n'
                       '2 - Saque\n'
                      'DIGITE O CÓDIGO DA MOVIMENTAÇÃO DESEJADA:')
  while tipo_movimentacao_atual not in ('1', '2'):
    tipo_movimentacao_atual = input('CÓDIGO DE MOVIMENTAÇÃO INVALIDO! '
                                    'DIGITE NOVAMENTE:')
  if tipo_movimentacao_atual == '1':
    numero_conta_atual = input('NÚMERO DA CONTA DE DEPÓSITO: ')
    i=0
    conta_existente = 0
    
    while i < len(vet_Contas):
        if numero_conta_atual == vet_Contas[i].GET_numero_conta():  
          id_conta = i  
          conta_existente = conta_existente + 1
        i=i+1

    if conta_existente == 0:
      print('Verifique os dados!\nNúmero de Conta não registrado.')
    else:
      valor_atual = float(input('\nVALOR DO DEPÓSITO:'))
      descricao_atual = input('DESCRIÇÃO DA MOVIMENTAÇÃO:')
      data_atual = datetime.now()
      data_atual = data_atual.strftime('%d/%m/%Y %H:%M:%S')
      saldo_suficiente_atual = 1
      conta_atual_FK = numero_conta_atual

      length_movimentacoes = len(vet_Movimentacoes)
      ID_movimentacao_atual = length_movimentacoes - 1

      # CRIANDO MOVIMENTACAO #
      movimentacao_atual = Movimentacao(vet_TipoDeMovimentacao[1].GET_tipo_movimentacao(), data_atual, valor_atual, descricao_atual, conta_atual_FK, saldo_suficiente_atual, ID_movimentacao_atual) 
      vet_Movimentacoes.insert((length_movimentacoes+1), movimentacao_atual)

      # SET NOVO SALDO #
      vet_Contas[id_conta].SET_novo_saldo(float(str(vet_Contas[id_conta].GET_saldo())) + valor_atual)

      # CRIANDO HISTÓRICO DE MOVIMENTACAO #
      historico_atual = HistoricoDeMovimentacao(movimentacao_atual.GET_ID_movimentacao(), vet_Contas[id_conta].GET_saldo() - valor_atual, vet_Contas[id_conta].GET_saldo(), vet_Contas[id_conta].GET_numero_conta(), movimentacao_atual.GET_data())
      length_historico = len(vet_Historicos)
      vet_Historicos.insert((length_historico+1), historico_atual)

      print('\nOperação Encerrada!\nObrigado')
      print('\nCOMPROVANTE:')
      print('\nOperação realizada em: ' + data_atual +
            '\nDepósito no valor de: ' + str(valor_atual) +
            '\nDescrição: ' + descricao_atual +
            '\nConta: '+ vet_Contas[id_conta].GET_numero_conta())

  if tipo_movimentacao_atual == '2':
    numero_conta_atual = input('NÚMERO DA CONTA DE SAQUE: ')
    i=0
    conta_existente = 0
    while i < len(vet_Contas):
      if numero_conta_atual == vet_Contas[i].GET_numero_conta():
        id_conta=i
        conta_existente = conta_existente + 1
      i=i+1
    if conta_existente == 0:
      print('Verifique os dados!\nNúmero de Conta não registrado.')
    else:
      saldo_atual_da_conta = vet_Contas[id_conta].GET_saldo()
      valor_atual = float(input('\nVALOR DO SAQUE:'))
      while valor_atual > saldo_atual_da_conta:
        print('Seu Saldo atual é de: ' + str(saldo_atual_da_conta))
        print('Você não pode sacar um valor superior ao seu saldo.')
        valor_atual = float(input('\nVALOR DO SAQUE:'))
        saldo_suficiente_atual = 0
      descricao_atual = input('DESCRIÇÃO DA MOVIMENTAÇÃO:')
      data_atual = datetime.now()
      data_atual = data_atual.strftime('%d/%m/%Y %H:%M:%S')
      saldo_suficiente_atual = 1
      conta_atual_FK = conta_atual.GET_numero_conta()

      length_movimentacoes = len(vet_Movimentacoes)
      ID_movimentacao_atual = length_movimentacoes - 1

      # CRIANDO MOVIMENTACAO #
      movimentacao_atual = Movimentacao(vet_TipoDeMovimentacao[1].GET_tipo_movimentacao(), data_atual, valor_atual, descricao_atual, conta_atual_FK, saldo_suficiente_atual, ID_movimentacao_atual) 
      vet_Movimentacoes.insert((length_movimentacoes+1), movimentacao_atual)

      # SET NOVO SALDO #
      vet_Contas[id_conta].SET_novo_saldo(float(str(vet_Contas[id_conta].GET_saldo())) - valor_atual)

      # CRIANDO HISTÓRICO DE MOVIMENTACAO #
      historico_atual = HistoricoDeMovimentacao(movimentacao_atual.GET_ID_movimentacao(), vet_Contas[id_conta].GET_saldo() + valor_atual, vet_Contas[id_conta].GET_saldo(), vet_Contas[id_conta].GET_numero_conta(), movimentacao_atual.GET_data())
      length_historico = len(vet_Historicos)
      vet_Historicos.insert((length_historico+1), historico_atual)

      print('\nOperação Encerrada!\nObrigado')
      print('\nCOMPROVANTE:')
      print('\nOperação realizada em: ' + data_atual +
            '\nSaque no valor de: ' + str(valor_atual) +
            '\nDescrição: ' + descricao_atual +
            '\nConta: '+ vet_Contas[id_conta].GET_numero_conta())

if operacao_atual == '2':
  numero_conta_atual = input('NÚMERO DA CONTA PARA CONSULTA DE SALDO: ')
  i=0
  conta_existente = 0
    
  while i < len(vet_Contas):
    if numero_conta_atual == vet_Contas[i].GET_numero_conta():  
      id_conta = i  
      conta_existente = conta_existente + 1
    i=i+1

  if conta_existente == 0:
    print('Verifique os dados!\nNúmero de Conta não registrado.')
  else:
    print('SALDO ATUAL DA CONTA ' + str(vet_Contas[id_conta].GET_numero_conta()) + ': ' + str(vet_Contas[id_conta].GET_saldo()))

if operacao_atual == '3':
  numero_conta_atual = input('NÚMERO DA CONTA PARA EMISSÃO DE EXTRATO: ')
  i=0
  conta_existente = 0
    
  while i < len(vet_Contas):
    if numero_conta_atual == vet_Contas[i].GET_numero_conta():  
      id_conta = i  
      conta_existente = conta_existente + 1
    i=i+1

  if conta_existente == 0:
    print('Verifique os dados!\nNúmero de Conta não registrado.')
  else:
    i=0
    count_historico = 0
    while i < len(vet_Historicos):
      if vet_Historicos[i].GET_conta_FK() == vet_Contas[id_conta].GET_numero_conta():
        print('-------------------------------------')
        print('Data: ' + str(vet_Historicos[i].GET_data_FK()))
        print('Saldo Antes da Movimentação: ' + str(vet_Historicos[i].GET_saldo_anterior()))
        print('Saldo Após a Movimentação: ' + str(vet_Historicos[i].GET_saldo_atual()))
        count_historico = count_historico + 1
      i=i+1
    if count_historico == 0:
      print('\nNenhum dado a ser exibido no seu extrato')

if operacao_atual == '4':
  print('\nEncerrando Operação...')

if operacao_atual == '5':
  print('\nCriação de Conta...')
  print('O cliente já possui cadastro no banco?')
  confere_cliente = input('(S/N)')
  while confere_cliente not in ('S', 'N'):
    print('CÓDIGO DIGITADO INVÁLIDO! Digite novamente:')
    confere_cliente = input('(S/N)')

  if confere_cliente == 'N':
    nome_cliente_criado = input('Nome do Cliente:')
    print('Escolha o tipo de Pessoa:'
          '\n1 - FISICA'
          '\n2 - JURIDICA')
    tipo_pessoa_cliente_criado = input('Tipo de Pessoa: ')
    while tipo_pessoa_cliente_criado not in ('1', '2'):
      print('Código digitado inválido!\nDigite Novamente')
      tipo_pessoa_cliente_criado = input('Tipo de Pessoa: ')

    if tipo_pessoa_cliente_criado == '1':
      tipo_pessoa_cliente_criado = vet_TipoDePessoa[0].GET_tipo_de_pessoa()
    if tipo_pessoa_cliente_criado == '2':
      tipo_pessoa_cliente_criado = vet_TipoDePessoa[1].GET_tipo_de_pessoa()

    tipo_documento_cliente_criado = 'CPF'
    if tipo_pessoa_cliente_criado == 'JURIDICA':
      tipo_documento_cliente_criado = 'CNPJ'

    documento_cliente_da_conta_criada = input(tipo_documento_cliente_criado + ': ')
    email_cliente_da_conta_criada = input('E-mail: ')
    telefone_cliente_da_conta_criada = input('Telefone: ')
    endereco_cliente_da_conta_criada = input('Endereço: ')

    # CRIANDO CLIENTE #
    cliente_atual_criado = Cliente(nome_cliente_criado, tipo_pessoa_cliente_criado, documento_cliente_da_conta_criada, email_cliente_da_conta_criada, telefone_cliente_da_conta_criada, endereco_cliente_da_conta_criada)
    length_clientes = len(vet_Clientes)
    vet_Clientes.insert((length_clientes+1), cliente_atual_criado)

    print('Cliente Cadastrado...')
    print('\nNOME: ' + nome_cliente_criado +
          '\nPESSOA: ' + tipo_pessoa_cliente_criado +
          '\n'+tipo_documento_cliente_criado+': ' + documento_cliente_da_conta_criada +
          '\nE-MAIL: ' +email_cliente_da_conta_criada+
          '\nTELEFONE: '+telefone_cliente_da_conta_criada+
          '\nENDEREÇO: '+endereco_cliente_da_conta_criada)

  if confere_cliente == 'S':
    numero_da_conta_criada = input('Digite um número para sua conta: ')
    i=0
    while i < len(vet_Contas):
      while numero_da_conta_criada == vet_Contas[i].GET_numero_conta():
        print('O número da conta digitado ( '+numero_da_conta_criada+' ) já existe!\n')
        numero_da_conta_criada = input('Digite outro número: ')

      i=i+1

    import random
    agencia_random = random.randint(2500, 3000)
    agencia_da_conta_criada = str(agencia_random)

    print('\nEscolha seu Tipo de Conta...'
          '\n1 - POUPANCA'
          '\n2 - CORRENTE'
          '\n3 - SALARIO'
          '\n4 - UNIVERSITARIA'
          '\n5 - DIGITAL')
    tipo_de_conta_da_conta_criada = int(input('Tipo de Conta: '))
    if tipo_de_conta_da_conta_criada == 1:
      tipo_de_conta_da_conta_criada = vet_TipoDeConta[0].GET_tipo_de_conta()
    if tipo_de_conta_da_conta_criada == 2:
      tipo_de_conta_da_conta_criada = vet_TipoDeConta[1].GET_tipo_de_conta()
    if tipo_de_conta_da_conta_criada == 3:
      tipo_de_conta_da_conta_criada = vet_TipoDeConta[2].GET_tipo_de_conta()
    if tipo_de_conta_da_conta_criada == 4:
      tipo_de_conta_da_conta_criada = vet_TipoDeConta[3].GET_tipo_de_conta()
    if tipo_de_conta_da_conta_criada == 5:
      tipo_de_conta_da_conta_criada = vet_TipoDeConta[4].GET_tipo_de_conta()

    status_da_conta_criada = 'ATIVO'

    documento_cliente_da_conta_criada = input('Documento do Cliente:')
    i=0
    documento_igual = 0

    while i < len(vet_Clientes):
      if documento_cliente_da_conta_criada == vet_Clientes[i].GET_documento():
        documento_igual = documento_igual + 1
      i=i+1

    if documento_igual == 0:
      print('Falha na Abertura de Conta!\nRevise os dados: Nenhum Cliente com este documento cadastrado no sistema.')
    else:

      # CRIANDO CONTA #
      conta_atual_criada = Conta(numero_da_conta_criada, agencia_da_conta_criada, tipo_de_conta_da_conta_criada, 0, status_da_conta_criada, documento_cliente_da_conta_criada)
      length_contas = len(vet_Contas)
      vet_Contas.insert((length_contas+1), conta_atual_criada)

      i=0
      while i < len(vet_Clientes):
        if documento_cliente_da_conta_criada == vet_Clientes[i].GET_documento():
          nome_cliente_da_conta_criada = vet_Clientes[i].GET_nome()
          if vet_Clientes[i].GET_tipo_de_pessoa_FK == 'FISICA':
            tipo_documento = 'CPF'
          else:
            tipo_documento = 'CNPJ'
        i=i+1

      print('Conta Criada com sucesso!')
      print('\nNÚMERO DA CONTA: ' + numero_da_conta_criada +
            '\nAGENCIA: ' + agencia_da_conta_criada +
            '\nTIPO DE CONTA: ' + tipo_de_conta_da_conta_criada +
            '\nSALDO: 0' +
            '\nSTATUS DA CONTA: ' + status_da_conta_criada +
            '\nCLIENTE: ' + nome_cliente_da_conta_criada +
            '\n' + tipo_documento+': ' + documento_cliente_da_conta_criada)
