import smtplib
import os.path
import wyslijEmailParams #plik z parametrami konta pocztowego

from email.mime.text import MIMEText


def wyslijEmail(do, temat, tresc):
  msg = MIMEText(tresc)
  msg['Subject'] = temat
  msg['From'] = wyslijEmailParams.od
  s = smtplib.SMTP_SSL(wyslijEmailParams.serwersmtp)
  s.login(wyslijEmailParams.login,wyslijEmailParams.haslo)
  s.sendmail(wyslijEmailParams.od, do, msg.as_string())
  print('Email do ',do, ' temat: ', temat)
  s.quit




##przykladUzycia
#wyslijEmail('stefan.potylica@poczta.fm','test','tresc')


