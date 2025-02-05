#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("FİGLET PORT TARAMA")
print(""" 

PORT TARAMA ARACINA HOŞGELDİNİZ :)

1) Hızlı Tarama
2) Servis ve Versiyon Tarama
3) İsletim Sistemi Bilgisi

""")
islemno = raw_input ("islem numarası girin:")

if(islemno=="1"):
      hedefip = raw_input ("Hedef ip girin:")
            os.system("nmap " + hedefip)
if(islemno=="2")
      
      hedefip = raw_input ("Hedef ip girin:")
      os.system("nmap -sS -sV " +hedefip )

(islemno=="3")
      
      hedefip = raw_input ("Hedef ip girin:")
               os.system("nmap -0" + hedefip)
else:
    
    print("SAMİ BUNU HATALI BULDU :( ")
