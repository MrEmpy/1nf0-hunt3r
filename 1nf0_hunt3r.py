#!/usr/bin/env python3
import requests, sys, os, re, time
from colorama import Fore
from bs4 import BeautifulSoup

def menu():
    print(f'''{Fore.LIGHTRED_EX}
 _        __  ___    _                 _   _____
/ |_ __  / _|/ _ \  | |__  _   _ _ __ | |_|___ / _ __
| | '_ \| |_| | | | | '_ \| | | | '_ \| __| |_ \| '__|
| | | | |  _| |_| | | | | | |_| | | | | |_ ___) | |
{Fore.RED}|_|_| |_|_|  \___/  |_| |_|\__,_|_| |_|\__|____/|_|

{Fore.LIGHTRED_EX}          ╔═════════════════════════╗
          ║{Fore.LIGHTWHITE_EX} Tool Created by Mr Empy {Fore.LIGHTRED_EX}║
          ║{Fore.LIGHTWHITE_EX} Version 2.2             {Fore.LIGHTRED_EX}║
          ╚═════════════════════════╝
{Fore.LIGHTWHITE_EX}https://youtube.co/channel/UCol7qlIUc0o0JKmdrmTWQtA

{Fore.LIGHTRED_EX}[01] {Fore.LIGHTWHITE_EX}Get Social Networks
{Fore.LIGHTRED_EX}[02] {Fore.LIGHTWHITE_EX}Get E-mail
{Fore.LIGHTRED_EX}[03] {Fore.LIGHTWHITE_EX}Get Information Using Number
{Fore.LIGHTRED_EX}[04] {Fore.LIGHTWHITE_EX}Get Information Using File Format
{Fore.LIGHTRED_EX}[05] {Fore.LIGHTWHITE_EX}Get Watched/Commented Videos {Fore.LIGHTRED_EX}[new]
{Fore.LIGHTRED_EX}[06] {Fore.LIGHTWHITE_EX}Get Random Information
{Fore.LIGHTRED_EX}[07] {Fore.LIGHTWHITE_EX}Get Information Using Custom Dork
    ''')
    inputt = input('Select: ')

    if inputt == '1' or inputt == '01':
        print('')
        social_network_information()
    if inputt == '2' or inputt == '02':
        print('')
        email_information()
    if inputt == '3' or inputt == '03':
        print('')
        number_info()
    if inputt == '4' or inputt == '04':
        print('')
        file_format_information()
    if inputt == '5' or inputt == '05':
        print('')
        information_Comments_Made()
    if inputt == '6' or inputt == '06':
        print('')
        random_information()
    if inputt == '7' or inputt == '07':
        print('')
        custom_dork()

def information_Comments_Made():
    search=input('Name or Nick: ')
    print(f'\n{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Searching...\n')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q=intext:{search}%20inurl:kzclip.com')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q=intext:{search}%20inurl:mavuong.com')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q=intext:{search}%20inurl:trshow.info')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q=intext:{search}%20inurl:ts-parfum.ru')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q=intext:{search}%20inurl:ukposts.info')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q=intext:{search}%20inurl:ukblow.info')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q=intext:{search}%20inurl:brlike.net')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q=intext:{search}%20inurl:br-it.info')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q=intext:{search}%20inurl:npvideos.info')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q=intext:{search}%20inurl:tr-cam.com')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q=intext:{search}%20inurl:videomuzik.biz')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q=intext:{search}%20inurl:viveos.net')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q=intext:{search}%20inurl:faceclips.net\n')



    time.sleep(1.5)

    def comments_1():
        page=requests.get(f'https://www.google.com/search?q=intext:{search} inurl:kzclip.com')
        soup=BeautifulSoup(page.content, "html.parser")
        for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
            result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
            result_1=result.partition('&')[0].strip()
            result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
            result_3=result_2.partition('https://accounts')[0].strip()
            result_finished=result_3.partition('https://www.google.com')[0].strip()
            a=str(print(result_finished))

    def comments_2():
        page=requests.get(f'https://www.google.com/search?q=intext:{search} inurl:mavuong.com')
        soup=BeautifulSoup(page.content, "html.parser")
        for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
            result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
            result_1=result.partition('&')[0].strip()
            result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
            result_3=result_2.partition('https://accounts')[0].strip()
            result_finished=result_3.partition('https://www.google.com')[0].strip()
            a=str(print(result_finished))

    def comments_3():
        page=requests.get(f'https://www.google.com/search?q=intext:{search} inurl:trshow.info')
        soup=BeautifulSoup(page.content, "html.parser")
        for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
            result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
            result_1=result.partition('&')[0].strip()
            result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
            result_3=result_2.partition('https://accounts')[0].strip()
            result_finished=result_3.partition('https://www.google.com')[0].strip()
            a=str(print(result_finished))

    def comments_4():
        page=requests.get(f'https://www.google.com/search?q=intext:{search} inurl:ts-parfum.ru')
        soup=BeautifulSoup(page.content, "html.parser")
        for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
            result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
            result_1=result.partition('&')[0].strip()
            result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
            result_3=result_2.partition('https://accounts')[0].strip()
            result_finished=result_3.partition('https://www.google.com')[0].strip()
            a=str(print(result_finished))

    def comments_5():
        page=requests.get(f'https://www.google.com/search?q=intext:{search} inurl:ukposts.info')
        soup=BeautifulSoup(page.content, "html.parser")
        for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
            result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
            result_1=result.partition('&')[0].strip()
            result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
            result_3=result_2.partition('https://accounts')[0].strip()
            result_finished=result_3.partition('https://www.google.com')[0].strip()
            a=str(print(result_finished))

    def comments_6():
        page=requests.get(f'https://www.google.com/search?q=intext:{search} inurl:ukblow.info')
        soup=BeautifulSoup(page.content, "html.parser")
        for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
            result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
            result_1=result.partition('&')[0].strip()
            result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
            result_3=result_2.partition('https://accounts')[0].strip()
            result_finished=result_3.partition('https://www.google.com')[0].strip()
            a=str(print(result_finished))

    def comments_7():
        page=requests.get(f'https://www.google.com/search?q=intext:{search} inurl:brlike.net')
        soup=BeautifulSoup(page.content, "html.parser")
        for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
            result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
            result_1=result.partition('&')[0].strip()
            result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
            result_3=result_2.partition('https://accounts')[0].strip()
            result_finished=result_3.partition('https://www.google.com')[0].strip()
            a=str(print(result_finished))

    def comments_8():
        page=requests.get(f'https://www.google.com/search?q=intext:{search} inurl:br-it.info')
        soup=BeautifulSoup(page.content, "html.parser")
        for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
            result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
            result_1=result.partition('&')[0].strip()
            result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
            result_3=result_2.partition('https://accounts')[0].strip()
            result_finished=result_3.partition('https://www.google.com')[0].strip()
            a=str(print(result_finished))

    def comments_9():
        page=requests.get(f'https://www.google.com/search?q=intext:{search} inurl:npvideos.info')
        soup=BeautifulSoup(page.content, "html.parser")
        for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
            result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
            result_1=result.partition('&')[0].strip()
            result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
            result_3=result_2.partition('https://accounts')[0].strip()
            result_finished=result_3.partition('https://www.google.com')[0].strip()
            a=str(print(result_finished))

    def comments_10():
        page=requests.get(f'https://www.google.com/search?q=intext:{search} inurl:tr-cam.com')
        soup=BeautifulSoup(page.content, "html.parser")
        for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
            result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
            result_1=result.partition('&')[0].strip()
            result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
            result_3=result_2.partition('https://accounts')[0].strip()
            result_finished=result_3.partition('https://www.google.com')[0].strip()
            a=str(print(result_finished))

    def comments_11():
        page=requests.get(f'https://www.google.com/search?q=intext:{search} inurl:videomuzik.biz')
        soup=BeautifulSoup(page.content, "html.parser")
        for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
            result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
            result_1=result.partition('&')[0].strip()
            result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
            result_3=result_2.partition('https://accounts')[0].strip()
            result_finished=result_3.partition('https://www.google.com')[0].strip()
            a=str(print(result_finished))

    def comments_12():
        page=requests.get(f'https://www.google.com/search?q=intext:{search} inurl:viveos.net')
        soup=BeautifulSoup(page.content, "html.parser")
        for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
            result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
            result_1=result.partition('&')[0].strip()
            result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
            result_3=result_2.partition('https://accounts')[0].strip()
            result_finished=result_3.partition('https://www.google.com')[0].strip()
            a=str(print(result_finished))

    def comments_13():
        page=requests.get(f'https://www.google.com/search?q=intext:{search} inurl:faceclips.net')
        soup=BeautifulSoup(page.content, "html.parser")
        for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
            result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
            result_1=result.partition('&')[0].strip()
            result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
            result_3=result_2.partition('https://accounts')[0].strip()
            result_finished=result_3.partition('https://www.google.com')[0].strip()
            a=str(print(result_finished))
            back=input(f'\n{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Back? (Y/n): ')

            if back == 'y' or back == 'Y':
                os.system('clear')
                menu()

            if back == 'n' or back == 'N':
                break

    comments_1()
    comments_2()
    comments_3()
    comments_4()
    comments_5()
    comments_6()
    comments_7()
    comments_8()
    comments_9()
    comments_10()
    comments_11()
    comments_12()
    comments_13()


def custom_dork():
    search=input('Dork (ex: intext, inurl): ')
    page=requests.get(f'https://www.google.com/search?q={search}')
    soup=BeautifulSoup(page.content, "html.parser")
    print(f'\n{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Searching...\n')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q={search}\n')
    time.sleep(1.5)

    for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
        result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
        result_1=result.partition('&')[0].strip()
        result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
        result_3=result_2.partition('https://accounts')[0].strip()
        result_finished=result_3.partition('https://www.google.com')[0].strip()
        a=str(print(result_finished))
        back = input(f'\n{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Back? (Y/n): ')

        if back == 'y' or back == 'Y':
            os.system('clear')
            menu()

        if back == 'n' or back == 'N':
            break

def number_info():
    ddd = input('Country (ex: +55) (without +): ')
    number = input('Number (with DDD): ')
    api = f'http://apilayer.net/api/validate?access_key=c38a73e8ce41dcee3768965af513192b&number={ddd}{number}&country_code=&format=1'
    info_number=requests.get(api.format(ddd + number)).text

    rm_symb_1=info_number.replace("{", "")
    rm_symb_2=rm_symb_1.replace("}", "")
    rm_symb_3=rm_symb_2.replace('  "', Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTWHITE_EX)
    rm_symb_4=rm_symb_3.replace(",", "")
    rm_symb_5=rm_symb_4.replace(":", ": ")
    rm_symb_6=rm_symb_5.replace('"', "")
    info_number_finish=rm_symb_6.replace('_', " ")

    print(f'\n{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Searching...\n')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q=intext:{ddd}{number}')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q=intext:{number}')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q=intext:+{ddd}{number}')
    time.sleep(1.5)

    print(info_number_finish + '\n')

    def number_search():
        page=requests.get(f'https://www.google.com/search?q=intext:{ddd}{number}')
        soup=BeautifulSoup(page.content, "html.parser")

        for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
            result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
            result_1=result.partition('&')[0].strip()
            result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
            result_3=result_2.partition('https://accounts')[0].strip()
            result_finished=result_3.partition('https://www.google.com')[0].strip()
            a=str(print(result_finished))

    def number_search_2():
        page=requests.get(f'https://www.google.com/search?q=intext:{number}')
        soup=BeautifulSoup(page.content, "html.parser")

        for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
            result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
            result_1=result.partition('&')[0].strip()
            result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
            result_3=result_2.partition('https://accounts')[0].strip()
            result_finished=result_3.partition('https://www.google.com')[0].strip()
            a=str(print(result_finished))

    def number_search_3():
        page=requests.get(f'https://www.google.com/search?q=intext:+{ddd}{number}')
        soup=BeautifulSoup(page.content, "html.parser")

        for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
            result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
            result_1=result.partition('&')[0].strip()
            result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
            result_3=result_2.partition('https://accounts')[0].strip()
            result_finished=result_3.partition('https://www.google.com')[0].strip()
            a=str(print(result_finished))
            back=input(f'\n{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Back? (Y/n): ')

            if back == 'y' or back == 'Y':
                os.system('clear')
                menu()

            if back == 'n' or back == 'N':
                break

    number_search()
    number_search_2()
    number_search_3()

def email_information():
    search=input('Name or Nick: ')
    email=input('Email Domain (ex: @gmail.com): ')
    page=requests.get(f'https://www.google.com/search?q=intext:{search}%20intext:{email}')
    soup=BeautifulSoup(page.content, "html.parser")
    print(f'\n{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Searching...\n')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q=intext:{search}%20intext:{email}\n')
    time.sleep(1.5)

    for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
        result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
        result_1=result.partition('&')[0].strip()
        result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
        result_3=result_2.partition('https://accounts')[0].strip()
        result_finished=result_3.partition('https://www.google.com')[0].strip()
        a=str(print(result_finished))
        back=input(f'\n{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Back? (Y/n): ')

        if back == 'y' or back == 'Y':
            os.system('clear')
            menu()

        if back == 'n' or back == 'N':
            break

def file_format_information():
    search=input('Name or Nick: ')
    format_file=input('Format File (ex: pdf): ')
    page=requests.get(f'https://www.google.com/search?q=intext:{search}%20ext:{format_file}')
    soup=BeautifulSoup(page.content, "html.parser")
    print(f'\n{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Searching...\n')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q=intext:{search}%20ext:{format_file}\n')
    time.sleep(1.5)

    for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
        result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
        result_1=result.partition('&')[0].strip()
        result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
        result_3=result_2.partition('https://accounts')[0].strip()
        result_finished=result_3.partition('https://www.google.com')[0].strip()
        a=str(print(result_finished))
        back=input(f'\n{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Back? (Y/n): ')

        if back == 'y' or back == 'Y':
            os.system('clear')
            menu()

        if back == 'n' or back == 'N':
            break

def social_network_information():
    search = input('Name or Nick: ')
    print(f'\n{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Searching...\n')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q=intext:{search}%20inurl:facebook.com')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q=intext:{search}%20inurl:instagram.com')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q=intext:{search}%20inurl:youtube.com')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q=intext:{search}%20inurl:tiktok.com')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q=intext:{search}%20inurl:twitter.com')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q=intext:{search}%20inurl:reddit.com\n')
    time.sleep(1.5)

    def facebook():
        page=requests.get(f'https://www.google.com/search?q=intext:{search}%20inurl:facebook.com')
        soup=BeautifulSoup(page.content, "html.parser")

        for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
            result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
            result_1=result.partition('&')[0].strip()
            result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
            result_3=result_2.partition('https://accounts')[0].strip()
            result_finished=result_3.partition('https://www.google.com')[0].strip()
            a=str(print(result_finished))

    def instagram():
        page=requests.get(f'https://www.google.com/search?q=intext:{search}%20inurl:instagram.com')
        soup=BeautifulSoup(page.content, "html.parser")

        for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
            result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
            result_1=result.partition('&')[0].strip()
            result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
            result_3=result_2.partition('https://accounts')[0].strip()
            result_finished=result_3.partition('https://www.google.com')[0].strip()
            a=str(print(result_finished))

    def youtube():
        page=requests.get(f'https://www.google.com/search?q=intext:{search}%20inurl:youtube.com')
        soup=BeautifulSoup(page.content, "html.parser")

        for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
            result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
            result_1=result.partition('&')[0].strip()
            result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
            result_3=result_2.partition('https://accounts')[0].strip()
            result_finished=result_3.partition('https://www.google.com')[0].strip()
            a=str(print(result_finished))

    def tiktok():
        page=requests.get(f'https://www.google.com/search?q=intext:{search}%20inurl:tiktok.com')
        soup=BeautifulSoup(page.content, "html.parser")

        for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
            result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
            result_1=result.partition('&')[0].strip()
            result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
            result_3=result_2.partition('https://accounts')[0].strip()
            result_finished=result_3.partition('https://www.google.com')[0].strip()
            a=str(print(result_finished))

    def twitter():
        page=requests.get(f'https://www.google.com/search?q=intext:{search}%20inurl:twitter.com')
        soup=BeautifulSoup(page.content, "html.parser")

        for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
            result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
            result_1=result.partition('&')[0].strip()
            result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
            result_3=result_2.partition('https://accounts')[0].strip()
            result_finished=result_3.partition('https://www.google.com')[0].strip()
            a=str(print(result_finished))

    def reddit():
        page=requests.get(f'https://www.google.com/search?q=intext:{search}%20inurl:reddit.com')
        soup=BeautifulSoup(page.content, "html.parser")

        for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
            result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
            result_1=result.partition('&')[0].strip()
            result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
            result_3=result_2.partition('https://accounts')[0].strip()
            result_finished=result_3.partition('https://www.google.com')[0].strip()
            a=str(print(result_finished))
            back=input(f'\n{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Back? (Y/n): ')

            if back == 'y' or back == 'Y':
                os.system('clear')
                menu()

            if back == 'n' or back == 'N':
                break

    facebook()
    instagram()
    tiktok()
    youtube()
    twitter()
    reddit()

def random_information():
    search = input('Name or Nick: ')
    page = requests.get(f'https://www.google.com/search?q=intext:{search}')
    soup = BeautifulSoup(page.content, "html.parser")
    print(f'\n{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Searching...\n')
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Reference Link: https://www.google.com/search?q=intext:{search}\n')
    time.sleep(1.5)

    for link in soup.find_all("a", href=re.compile('(?<=/url\?q=)(htt.*://.*)')):
        result=str(re.split(":(?=http)", link["href"].replace('/url?q=', "")))
        result_1=result.partition('&')[0].strip()
        result_2=result_1.replace("['", f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} ')
        result_3=result_2.partition('https://accounts')[0].strip()
        result_finished=result_3.partition('https://www.google.com')[0].strip()
        a=str(print(result_finished))
        back=input(f'\n{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Back? (Y/n): ')

        if back == 'y' or back == 'Y':
            os.system('clear')
            menu()

        if back == 'n' or back == 'N':
            break

if __name__ == '__main__':
    os.system('clear')
    menu()
