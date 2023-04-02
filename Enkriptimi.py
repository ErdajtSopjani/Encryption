import random
import string
import bcrypt

shkr = " " + string.punctuation + string.digits + string.ascii_letters
qelesiprint = shkr[:]
shkr = list(shkr)
#print(shkr)
qelesi = list(qelesiprint[:])
random.shuffle(qelesi)



#print(qelesi)

mode = input("\n\nShtyp 1 per te enkryptuar\nShtyp 2 per te dekryptuar\nShtyp 3 per te kthyer ne hash\n")


#ENKRIPTIMI

if mode == "1":
    mesazhi = input("Shkruaj nje mesazh per ta enkryptuar: ")
    mesazhi_enkryptum = ""

    for letter in mesazhi:
        index = shkr.index(letter)
        mesazhi_enkryptum += qelesi[index]

    print(f"\nMesazhi Origjinal: {mesazhi}")
    print(f"Mesazhi Enkriptum: {mesazhi_enkryptum}")
    print("\nQelesi i enkriptimit: "+"".join(map(str, qelesi)) + "\n")
    
    f = open("enkriptimet.txt", "a")
    f.write(f"\n**ENKRIPTIM**\nMesazhi i enkriptum: {mesazhi_enkryptum}\nMesazhi i dekryptum: {mesazhi}\n\nQelesi i enkriptimit: {qelesi}\n\n")
    f.close()

#DEKRIPTIMI
elif mode == "2":
    mesazhi_enkryptum = input("Shkruaj nje mesazh per ta dekryptuar: ")
    mesazhi = ""
    qelesi = input("Shkruani qelesin e enkriptimit: ")
    qelesiprint = qelesi[:]
    qelesi = list(qelesi)
    for letter in mesazhi_enkryptum:
        index = qelesi.index(letter)
        mesazhi += shkr[index]

    print(f"\nMesazhi Enkriptum: {mesazhi_enkryptum}")
    print(f"Mesazhi Origjinal : {mesazhi}")


    f = open("enkriptimet.txt", "a")
    f.write(f"\n**DEKRIPTIM**\nMesazhi i enkriptum: {mesazhi_enkryptum}\nMesazhi i dekryptum: {mesazhi}\nQelesi i enkriptimit: {qelesiprint}\n\n")
    f.close()


#HASH

elif mode == "3":
    mesazhi_enkryptum = input("Shkruaj nje mesazh per ta kthyer ne hash: ")
    
    password = mesazhi_enkryptum.encode('ascii', errors='ignore')
    
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)

    print(f"Mesazhi juaj origjinal eshte: {mesazhi_enkryptum}\n")
    print(f"Mesazhi juaj hashed eshte: {hashed}\n")

    f = open("enkriptimet.txt", "a")
    f.write(f"\n**HASHING**\nMesazhi i normal: {mesazhi_enkryptum}\nMesazhi hashed: {hashed}\n\n")
    f.close()