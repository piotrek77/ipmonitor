import os
import time
import csv
import wyslijEmail
import ipmonitorParams
import datetime
import curses
from curses import wrapper
import threading
from queue import Queue


stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

hosty = csv.reader(open('listaHostow.csv', newline=''), delimiter=';', quotechar='|')



hosty2 = list(hosty)
lock = threading.Lock()

class maszyna:
  adres = ''
  nazwa = ''
  wiersz = 0
  stan = -1
  #def __maszyna__(self):
  #  self.adres =''
  #  self.nazwa=''
  #  self.wiersz=0
  #  self.stan=-1



def kbfunc():
  
  stdscr.nodelay(True)
  try:
    x = stdscr.getkey()
  except:
    x = ''
  
  return x


##funkcja zwraca ilosc poprawnych pingow
def ping(adres, powtorz):
  ile = 0
  for i in range(powtorz):
    resp2 = os.system('sudo ping -c 1 '+adres+' > /dev/null')
    if resp2 == 0:
      ile+=1
  return ile

def sprawdzacz():

  #while True:
    #while True:
    #w pierwszej linii jest nagloweK
  stany = {}
  maszyny = []
  wiersz = 0
#napelniamy liste maszyny obiektami typu maszyna
  for rowek in hosty2:
    if rowek[0]!='adres':
      wiersz += 1
      maszynaTmp = maszyna()
      maszynaTmp.wiersz = wiersz
      maszynaTmp.nazwa = rowek[1]
      maszynaTmp.adres = rowek[0]
      maszynaTmp.stan = -1
      maszyny.append(maszynaTmp)
      #stany[rowek[0]]=-1
  while True:
    #wiersz = 0
    #for rowek in hosty2:
    for m in maszyny:
      #wiersz += 1
      x = kbfunc()
      if x == 'q':
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        exit()
      #if rowek[0]!='adres':
      if 1==1:
        #print(rowek)
        stdscr.addstr(m.wiersz,0,m.adres)
        stdscr.addstr(m.wiersz,16,m.nazwa+'                       ')
        stdscr.addstr(m.wiersz,30,' ---- sprawdzam ----')
        stdscr.refresh()
        resp = ping(m.adres,1)#os.system('sudo ping -c 1 '+rowek[0]+' > /dev/null')
        prev=m.stan
        #print('prev={}'.format(prev))
        stan = ''
        if resp == 1:
          #print(rowek[0], ' UP')
          stdscr.addstr(m.wiersz,30,' UP                  ')
          stdscr.refresh()
          m.stan = 1
          stan='UP'
        else:
          if ping(m.adres,4)==0:
#            print(rowek[0], ' DOWN')
            stdscr.addstr(m.wiersz ,30, ' DOWN               ')
            stdscr.refresh()
            m.stan =0
            stan='DOWN'
        stdscr.refresh()
        #sprawdzamy czy nastapila zmiana statusu
        #print('prev={} stany[rowek[0]]={} rowek[0]={}'.format(prev, stany[rowek[0]], rowek[0]))
        if (prev!=-1) & (prev != m.stan):
          try:
            wynik = wyslijEmail.wyslijEmail(ipmonitorParams.do, datetime.datetime.now().strftime('%y-%m-%d %H-%M-%S')+ ' '+stan + ' '+m.nazwa+' '+m.adres, '')
            stdscr.addstr(0,0, datetime.datetime.now().strftime('%H-%M-%S')+' '+wynik)
          except:
            #print("Blad podczas wysylki email")
            stdscr.addstr(0,0,datetime.datetime.now().strftime('%H-%M-%S')+' Blad podczas wysylki email              ')
            stdscr.refresh()

    time.sleep(5)
  
     

def main(stdscr):
  
  sprawdzacz()




wrapper(main)
