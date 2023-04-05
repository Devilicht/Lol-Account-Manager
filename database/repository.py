import sqlite3 as sql


class accountDb:
    def __init__(self,) -> None:
        db = sql.connect('database.db')
        cur = db.cursor()
        self.cur = cur
        self.db = db
    
    def checkAccount(self,summoner='', type='') -> tuple | list:
        if type == 'fetchone':
            result = self.cur.execute('SELECT * FROM accounts WHERE summoner=?', (summoner,))
            return result.fetchone()
        elif type == 'fetchall':
            result = self.cur.execute('SELECT * FROM accounts')
            return result.fetchall()


    def  addAcount(self,login: str ,password: str ,server: str ,summoner: str ,info: str) -> None:
        self.cur.execute(
        'INSERT INTO accounts (login, password, server, summoner, info) VALUES (?,?,?,?,?)', (login, password, server, summoner, info)
        )
        self.db.commit()

    def updateAccount(self,info: str) -> None:
        self.db.execute('UPDATE accounts SET info=?', (info,))

    def delete(self, summoner: str) -> None:
        self.cur.execute('DELETE FROM accounts WHERE summoner=?', (summoner,))
        self.db.commit()