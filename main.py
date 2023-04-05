
from os import system as cmd, name as osname
from database.repository import accountDb
from reqs.requisitions import getSummoner, updateStats
from manag import mangAcc
from time import sleep

db = accountDb()

def clearScreen():
    cmd('cls' if osname == 'nt' else 'clear')

db.cur.execute('CREATE TABLE IF NOT EXISTS accounts(login, password, server, summoner, info)')

def menu():
    clearScreen()
    print('Lol Account Manager!')
    print('Created by Oblivion- github.com/Devilicht')
    global op
    op = input('1- Vizualizar suas contas. 2-Adicionar uma nova conta 3-Remover alguma conta 4-Atualizar dados no OP.GG . 0 - Sair: ')
    print('')
    if op == '1':
        mangAcc.listAccounts(getSummoner=getSummoner)
    elif op == '2':
        mangAcc.addAccount(getSummuner=getSummoner)
    elif op == '3':
        mangAcc.deleteAccount()
    elif op == '4': 
        accounts = db.checkAccount(type="fetchall")
        updateStats(accounts=accounts)             
    elif op == '0':
        exit()
    else:
        print('\nOpção inválida, tente novamente!')
        sleep(1.5)
        menu()
        

if __name__ == '__main__':
    menu()