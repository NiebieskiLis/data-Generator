from typing import Tuple


from datetime import timedelta
import random
import barnum as Ba
import names



def main () :

 rok = 1
 iloscbiur = 10
 IloscAdresow=20
 IloscHoteli = 20
 IloscTransportu = 20
 IloscOsob = 10
 lives = 10
 Wycieczki =10
 transports =10
 rezyduje = 10
 participate = 10
 Employee= 10
 typHotelu=['*' , '**' , '***','****','*****' , 'motel']
 typTransportu=['statek' , 'pociag' , 'autokar']
 typWycieczki=['Objazdowa' , 'Wypoczynkowa' , 'Planowana']
 MaxDiscount=30
 trip_notes = ['transport delay' , 'natural catastrophy' , 'none' , 'none']
 typ_zaplaty = ['cash', 'card', 'bank transfer']
 pozycja = ['biurowy' , 'manager' , 'CEO']
 Teryt = ['02', '04' , '06' , '08' , '10' , '12' , '14' , '16' , '18' , '20 ' , '22' , '28']

 random.seed()
 ##Hotel (addres , nazwa , typ E_mal , phone
 file = open("hotel.txt", "w")
 for x in range(IloscHoteli):
  rekord = str(random.randint(1, IloscAdresow)) + ('|') + Ba.create_company_name() + ('|') + random.choice(typHotelu) + ('|') + Ba.create_email() + ('|') + Ba.create_phone() + ('|')
  file.write(rekord + '\n')
 file.close()

 print('Koniec ładowania hotelu')

 random.seed()
 # Transport (addres ID , nazwa , typTransportu, discount , E_mail , phone
 file = open("transport.txt", "w")
 for x in range(IloscTransportu):
  rekord = str(random.randint(1, IloscAdresow)) + ('|') + Ba.create_company_name() + ('|') + random.choice(typTransportu) + ('|') + str(random.randint(0, MaxDiscount)) + ('|') + Ba.create_email() + ('|') + Ba.create_phone() + ('|')
  file.write(rekord + '\n')
 file.close()

 ##Transports (Trip , Company)

 file = open("Transports.txt", "w")
 for x in range(transports):
  rekord = str(random.randint(1, Wycieczki)) + ('|') + str(random.randint(1, IloscTransportu)) + ('|')
  file.write(rekord + '\n')
 file.close()

 ##Osoby (name , surname , Age , e-mail , PhoneNo)

 random.seed()
 file = open("osoby.txt", "w")
 for x in range(IloscOsob):
  rekord = names.get_first_name() + ('|') + names.get_last_name() + ('|') + str(Ba.create_birthday(3, 80)) + ('|') + Ba.create_email() + ('|') + Ba.create_phone() + ('|')
  file.write(rekord + '\n')
  if x%13 == 0 :
      file1 = open("Employee.txt", "a")
      rozpocz=Ba.create_birthday(0, 2)
      if x%3 == 0 :
         finish = str(rozpocz+timedelta(days= (random.randint(1 , 300))))
      else :
         finish = 'none'
      rekord1 = str(x) + ('|') + str(rozpocz) + ('|')+ str(finish) +('|') + str(random.choice(pozycja))+('|') +random.choice(Teryt) + str(random.randint(1, 10))+('|')
      file1.write(rekord1 + '\n')
      file1.close()
 file.close()
##Lives (osoba , adres)

 file = open("lives.txt", "w")
 for x in range(lives):
  rekord =str(random.randint(1, IloscOsob)) + ('|') + str(random.randint(1, IloscAdresow))+('|')
  file.write(rekord + '\n')
 file.close()



 ##rezyduje (Trip , Company)

 file = open("Residences.txt", "w")
 for x in range(rezyduje):
  rekord = str(random.randint(1, Wycieczki)) + ('|') + str(random.randint(1, IloscHoteli)) + ('|')
  file.write(rekord + '\n')
 file.close()

 ##Trips
 file = open("Trips.txt", "w")
 for x in range(Wycieczki):
  data = Ba.create_birthday(rok,rok+1)
  rekord = str(data)+('|')+str(data+timedelta(days=(random.randint(1,14)))) +('|')+random.choice(typWycieczki) +('|')+random.choice(trip_notes)+('|')
  file.write(rekord + '\n')
  file1 = open("Participate.txt", "w")
  file2 = open("Bill.txt", "w")
  partisiopanty=random.randint(8, 30)
  for x in range(partisiopanty):
   invoice_date=data-timedelta(days=(random.randint(70,120)))
   rekord1 = str(random.randint(1, IloscOsob)) + ('|') + str(random.randint(1, Wycieczki)) + ('|')+str(x)+('|')
   rekord2 = str(random.randint(1, Employee)) + ('|') + str(invoice_date) + ('|')+ str(invoice_date+timedelta(days=(random.randint(2,30))))+('|') + str(random.randint(300 , 3000)) + ('|')+ str(random.choice(typ_zaplaty))+('|')
   file1.write(rekord1 + '\n')
   file2.write(rekord2 + '\n')
  file1.close()
  file2.close()

 file.close()


 ##Employee
 ##
main()