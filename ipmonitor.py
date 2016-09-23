import os
import time
import csv
import wyslijEmail
import ipmonitorParams
import datetime
import curses
from curses import wrapper


stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

hosty = csv.reader(open('listaHostow.csv', newline=''), delimiter=';', quotechar='|')



hosty2 = list(hosty)


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
  for rowek in hosty2:
    if rowek[0]!='adres':
      stany[rowek[0]]=-1
  while True:
    wiersz = 0
    for rowek in hosty2:
      wiersz += 1
      x = kbfunc()
      if x == 'q':
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        exit()
      if rowek[0]!='adres':
        #print(rowek)
        stdscr.addstr(wiersz,0,rowek[0])
        stdscr.addstr(wiersz,16,rowek[1]+'                       ')
        stdscr.addstr(wiersz,30,' ---- sprawdzam ----')
        stdscr.refresh()
        resp = ping(rowek[0],1)#os.system('sudo ping -c 1 '+rowek[0]+' > /dev/null')
        prev=stany[rowek[0]]
        #print('prev={}'.format(prev))
        stan = ''
        if resp == 1:
          #print(rowek[0], ' UP')
          stdscr.addstr(wiersz,30,' UP                  ')
          stdscr.refresh()
          stany[rowek[0]]= 1
          stan='UP'
        else:
          if ping(rowek[0],4)==0:
#            print(rowek[0], ' DOWN')
            stdscr.addstr(wiersz ,30, ' DOWN               ')
            stdscr.refresh()
            stany[rowek[0]] =0
            stan='DOWN'
        stdscr.refresh()
        #sprawdzamy czy nastapila zmiana statusu
        #print('prev={} stany[rowek[0]]={} rowek[0]={}'.format(prev, stany[rowek[0]], rowek[0]))
        if (prev!=-1) & (prev != stany[rowek[0]]):
          try:
            wyslijEmail.wyslijEmail(ipmonitorParams.do, datetime.datetime.now().strftime('%y-%m-%d %H-%M-%S')+ ' '+stan + ' '+rowek[1]+' '+rowek[0], '')
          except:
            print("Blad podczas wysylki email")
            stdscr.addstr(0,0,datetime.datetime.now().strftime('%y-%m-%d %H-%M-%S')+'Blad podczas wysylki email              ')
            stdscr.refresh()

    time.sleep(5)
  
     

def main(stdscr):
  
  sprawdzacz()




wrapper(main)
