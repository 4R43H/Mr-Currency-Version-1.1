#!/bin/python3
"""
This My mini project for crypto currencys
coder --> Eliot Elderson (EE)
Email --> N0000000!
Created in --> 31 Jan 2023
Update in --> 31 Jan 2023
support time --> forever :)
Please Email:((((( --> arashkianidev@gmail.com
"""

"""
in this section we import needs for run the program!
"""
import requests as req
from bs4 import BeautifulSoup as bs
from colorama import Fore as color
import mysql.connector
import sys
import os


"""
In this section we define some variables for program.
"""

bold = '\033[1m'
endbold = '\033[0m'


cr_list = [
    'bitcoin',
    'ethereum',
    'dogecoin',
    'shiba-inu',
    'xrp',
    'binance-coin',
    'cardano',
    'solana',
    'stellar',
    'chainlink',
    'uniswap',
    'decentraland',
    'filecoin',
    'apecoin',
    'hedera',
    'eos',
    'tezos',
    'the-sandbox',
    'aave',
    'axie-infinity',
    'elrond',
    'theta',
    'chiliz',
    'ecash',
    'neo',
    'synthetix',
    'polygon',
    'avalanche',
    'tron',
    'litecoin',
    'cosmos',
    'monero',
    'quant',
    'algorand',
    'flow',
    'vechain']


"""This section clear the screen."""
os.system("clear")


"""
In this section I define the functions and this function, Show the bannar in command line of your computer.
"""

cnx = mysql.connector.connect(user='root',
                              password='',
                              host='127.0.0.1',
                              database = 'maindb')


cursor = cnx.cursor()

def ban():
    #banner!
    print(bold+color.MAGENTA+'''                                                                 
  _ __ ___  _ __ ______ ___ _   _ _ __ _ __ ___ _ __   ___ _   _ 
 | '_ ` _ \| '__|______/ __| | | | '__| '__/ _ \ '_ \ / __| | | |
 | | | | | | |        | (__| |_| | |  | | |  __/ | | | (__| |_| |
 |_| |_| |_|_|         \___|\__,_|_|  |_|  \___|_| |_|\___|\__, |
                                                            __/ |
                                                           |___/ 
    '''+endbold)

    print("Welcome to Mr currncy app!")
    print("You can type list to see list!")
    print("You can type exit to exit of this app!")
    print("You can type help to see help list!")
    print("You can see supported crypto currencys with see command!")
    print("service-1 to use service-1")
    print("----------------------------------")


"""
In this section I define The main function and I will more explain later.
"""
def cons():
    """This try block and try some codes."""
    try:
        """first try call the banner function."""
        ban()
        """than with for loop print all of supported crypto currencys."""
        for x in cr_list:
            print(color.CYAN+x+endbold)

        """In here I define While loop for my input becuse i want this run to infinity(until user enter Ctrl-C or exit command)."""
        while True:
            """Input for user."""
            arz_avalie = input("Enter your crypto currency! : ")
            """
            some checks and define some command for program.
            """
            if arz_avalie == "list":
                print(cr_list)

            if arz_avalie == "exit":
                print("")
                print(color.GREEN+"have good time!"+endbold)
                print(color.GREEN+"good bye!"+endbold)
                sys.exit()

            if arz_avalie == "help":
                ban()

            if arz_avalie == "service-1":
                print("you can go to service-1.py file and run it and use it!")

            if arz_avalie == "see":
                print(cr_list)

            if arz_avalie == "clear":
                os.system("clear")
            """
            In this section if input be in the list of crypto currency and if status code of target site be 200, this section scrap the url and,
            return the result to me.
            """
            if arz_avalie in cr_list:
                r = req.get("https://www.coindesk.com/price/"+arz_avalie+"/")

                if r.status_code == 200:
                    soup = bs(r.text, 'html.parser')
                    valx = soup.find("span", class_="currency-pricestyles__Price-sc-1rux8hj-0 jIzQOt")
                    print(valx.text)

                    i = input("Enter date like that YYYY-MM-DD: ")
                    f = req.get("https://www.timeanddate.com/worldclock/iran/tehran")
                    if f.status_code == 200:
                        soup = bs(f.text, 'html.parser')
                        val1 = soup.find("span", class_="h1")
                        v = str(val1.text)

                        q1 = "INSERT INTO PandTXX VALUES (%s, %s, %s, %s)"
                        parameters = (str(arz_avalie), str(valx.text), str(v), str(i))

                        cursor.execute(q1, parameters)

                    
                    cnx.commit()
                    cnx.close()
                
                elif r.status_code == 404:
                    """if status code of site be 404 this section will return the text."""
                    print("Oops! Not found.")
                

                elif arz_avalie not in cr_list:
                    """If input was not in cr list program will return this text"""
                    print("Sorry\n We are not supported this crypto currency!")

    
    except KeyboardInterrupt:
        """In this section if user click on Ctrl+C program will return this text."""
        print("\nBye :/")
        sys.exit()


if __name__ == "__main__":
    cons()
