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

mode = input("\n\nPress 1 to encrypt\nPress 2 to decrypt\nPress 3 to hash\n")


#ENKRIPTIMI

if mode == "1":
    mesazhi = input("Enter a message to Encrypt: ")
    mesazhi_enkryptum = ""

    for letter in mesazhi:
        index = shkr.index(letter)
        mesazhi_enkryptum += qelesi[index]

    print(f"\nNormal Message: {mesazhi}")
    print(f"Encrypted Message: {mesazhi_enkryptum}")
    print("\nEncryption Key: "+"".join(map(str, qelesi)) + "\n")
    
    f = open("enkriptimet.txt", "a")
    f.write(f"\n**ENCRYPTION**\nEncrypted message: {mesazhi_enkryptum}\nDecrypted message: {mesazhi}\n\nEncryption Key: {qelesi}\n\n")
    f.close()

#DEKRIPTIMI
elif mode == "2":
    mesazhi_enkryptum = input("Enter a message to Decrypt: ")
    mesazhi = ""
    qelesi = input("Enter the encryption key: ")
    qelesiprint = qelesi[:]
    qelesi = list(qelesi)
    for letter in mesazhi_enkryptum:
        index = qelesi.index(letter)
        mesazhi += shkr[index]

    print(f"\nMesazhi Enkriptum: {mesazhi_enkryptum}")
    print(f"Mesazhi Origjinal : {mesazhi}")


    f = open("enkriptimet.txt", "a")
    f.write(f"\n**DECRYPTION**\nEncrypted message: {mesazhi_enkryptum}\nDecrypted message: {mesazhi}\nEncryption Key: {qelesiprint}\n\n")
    f.close()


#HASH

elif mode == "3":
    mesazhi_enkryptum = input("Enter a message to hash: ")
    
    password = mesazhi_enkryptum.encode('ascii', errors='ignore')
    
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)

    print(f"Your message was: {mesazhi_enkryptum}\n")
    print(f"Your hashed message is: {hashed}\n")

    f = open("enkriptimet.txt", "a")
    f.write(f"\n**HASHING**\nYour message was: {mesazhi_enkryptum}\nHashed message: {hashed}\n\n")
    f.close()