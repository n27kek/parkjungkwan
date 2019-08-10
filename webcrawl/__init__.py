
from webcrawl.controller import Controller
if __name__ == '__main__':

    print('a. 국회 크롤링: ')
    print('b. 벅스 크롤링: ')
    print('k. 주가 크롤링: ')
    print('ns. 주가 크롤링: ')
    print('nm. 네이버 영화 크롤링: ')
    print('nl. 네이버 자동 로그인: ')
    print('0. 종료 ')
    flag=input('크롤링할 사이트')
    ctr=Controller()
    ctr.exec(flag)


