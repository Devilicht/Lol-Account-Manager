# Lol-Account-Manager
É um BOT gerenciador de conta do LOL, ele tem as opções de armazenar as contas, deletar, listar e atualizar os dados. 

-Armazenamento :  partir de login, senha, server, nick . Com base em nick e server ele faz um webscraping no OP.GG e captura as informações de Elo, Pdl e Winrate e coloca num banco de dados (sqlite).

-Listagem : Toda vez que essa opção é acionada ele vai no OP.GG e busca pelo nick e server faz um webscraping e atualiza as informações no banco de dados(sqlite) e printa na tela.

-Delete : solicita um nick e vai no banco de dados conferir, caso houver o nick ele busca no banco de dados e deleta todas info do nick.

-Atualizar dados : Ele busca todos os nick no banco de dados e faz um request em cada page e interage com o botão "ATUALIZAR DADOS" para que as informações no site sejam atualizadas utilizando selenium.

LIB essenciais : requests, selenium, sqlite.
