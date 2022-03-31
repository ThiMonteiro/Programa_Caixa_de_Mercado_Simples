from time import sleep
while True:
    dados = dict()
    armazenamento_de_dados = list()
    dados.clear()
    # informações sobre os bancos.
    print('='*41)
    print('          CAIXA DO MERCADINHO ')
    print('='*41)
    print('''BANCOS DISPONVIEIS: 
       0 => Itaú
       1 => Caixa Econômica Federal
       2 => Bradesco
       3 => Santander''')
    print('='*41)
    # Bancos cadastrados no sistema e opção de selecionar o banco.
    bancos = ('ITAÚ', 'CAIXA ECONÔMICA FEDERAL', 'BRADESCO', 'SANTANDER')
    opc = int(input('   Qual banco você deseja acessar (0, 1, 2, 3)? '))
    if opc == 0 or opc == 1 or opc == 2 or opc == 3:
        print('<<< ENTRANDO... >>>')
        sleep(1)
        print(f' ===== BEM-VINDO AO BANCO {bancos[opc]} =====')
        # Local para inserir AG e C/C.
        dados['Ag'] = int(input('   AG: '))
        dados['Cc'] = float(input('   C/C: '))
        dados['Senha'] = int(input('   Senha Eletrônica: '))
        print('<<< ENTRANDO... >>>')
        sleep(1)
        armazenamento_de_dados.append(dados.copy())
        break
    else:
        print('   Por favor, selecione um dos bancos disponíveis: ')
        sleep(2)
        print('=' * 41)
print('=' * 41)
print('{:^38}'.format(f'BANCO {bancos[opc]}'))
print('='*41)
# Valor de saldo fictício
valor = 250
print(f'==> Saldo na conta R$ {valor:.2f}')
print('=' * 41)
# Sistema de sacar o dinheiro
while True:
    opc_de_saque = ' '
    while opc_de_saque not in 'SsNn':
        opc_de_saque = str(input('Deseja sacar algum valor? [S/N] ')).upper()[0]
    if opc_de_saque == 'S':
        opc_valor = float(input('Quanto você deseja sacar? R$ '))
        if valor >= opc_valor:
            valor -= opc_valor
            print('Sancando...')
            sleep(2)
        else:
            if opc_valor > valor:
                print('=' * 41)
                print('O valor solicitado está muito acima do valor em conta!!')
                print(f'==> Saldo disponível {valor}')
        # Mostra o saldo atual
        print('='*41)
        print(f'==> Saldo disponível {valor}')
        print('='*41)
    # Finalização do programa
    else:
        print('='*41)
        print(f'Volte sempre!!Nós do BANCO {bancos[opc]} agradecemos =) !!')
        print('='*41)
        break
