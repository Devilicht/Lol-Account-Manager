
from time import sleep
from main import clearScreen
from database.repository import accountDb


dbOp = accountDb()

servers = ['br', 'na', 'euw', 'oce', 'kr', 'jp', 'las',
           'lan', 'ru', 'tr', 'sg', 'ph', 'tw', 'vn', 'th', 'eune']



def addAccount(getSummuner):
    clearScreen()

    login = input('Login: ')
    password = input('Senha: ')
    server = input('Server: ').lower()
    while server not in servers:
        print('Server inválido!')
        sleep(1.5)
        clearScreen()
        print(f'Login: {login}')
        print(f'Senha: {password}')
        server = input('Server: ').lower()
    summoner = input('Nick: ')[:16]
    info = getSummuner(server, summoner)
    if info == None:
        print(f'O invocador {summoner} não existe!')
    else:
        dbOp.addAcount(login=login, password=password, server=server, summoner=summoner, info=info)
        print(f'\n Conta {summoner} adicionada com sucesso!')
        sleep(1.5)

def deleteAccount():
    clearScreen()
    summoner = input('Nick da conta a ser removida: ').lower()
    if dbOp.checkAccount(summoner=summoner, type='fetchone'):
        dbOp.delete(summoner=summoner)
        print(f'\n Conta {summoner} removida com sucesso!')
    else:
        print(f'Conta "{summoner}" não encontrada!')
        sleep(1.5)

def listAccounts(getSummoner):
    accounts = dbOp.checkAccount(type='fetchall')
    i = 1
    for account in accounts:
        info = getSummoner(account[2], account[3])
        dbOp.cur.execute('UPDATE accounts SET info=?', (info,))
        print(f'[CONTA #{i}]')
        print(f'Login: {account[0]}')
        print(f'Senha: {account[1]}')
        print(f'Server: {account[2]}')
        print(f'Nick: {account[3]}')
        print(f'Info: {info}')
        print('\n')
        i += 1
    input('Pressione uma tecla para voltar ao menu anterior...')