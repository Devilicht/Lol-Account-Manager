from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver
from selenium.webdriver.common.by import By
from re import findall


def updateStats(accounts) -> None:
    for account in accounts:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--log-level=3")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(f'https://www.op.gg/summoners/br/{account[3]}')
        button = driver.find_element(by=By.CLASS_NAME, value='css-4e9tnt')
        button.click()
        driver.close()


def getSummoner(server: str, summoner: str) -> str | None:
    userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0'
    headers = {'User-Agent': userAgent}
    padrao = r">(.*?)<"
    response = get(
        f'https://www.op.gg/summoners/{server}/{summoner}', headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    vr = findall(padrao, str((soup.find('h2', {'class': 'header__title'}))))
    eloa = findall(padrao, str((soup.find('div', {'class': 'tier'}))))
    pdla = findall(padrao, str(soup.find('div', {'class': 'lp'})))
    winRatea = findall(padrao, str(soup.find('div', {'class': 'ratio'})))
    WLa = findall(padrao, str(soup.find('div', {'class': 'win-lose'})))

    separador = " "
    elo = separador.join(eloa)
    pdl = separador.join(pdla)
    winRate = separador.join(winRatea)
    wL = separador.join(WLa)

    elo = " ".join(elo.split())
    pdl = " ".join(pdl.split())
    winRate = " ".join(winRate.split())
    wL = " ".join(wL.split())
    
    if vr == []:
        if eloa == []:
            pp = (f'a conta {summoner} está sem elo').lower()

        else:
            pp = (
                f'a conta {summoner} está {elo}-{pdl} e com {wL} {winRate}').lower()
    else:
        pp = None

    return pp
