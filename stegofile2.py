import cv2
import os

def encrypt_image(msg):
    char_to_int = {}
    int_to_char = {}

    for i in range(255):
        char_to_int[chr(i)] = i
        int_to_char[i] = chr(i)

    img = cv2.imread("mypic.jpg")

    m = 0
    n = 0
    z = 0

    for i in range(len(msg)):
        img[n, m, z] = char_to_int[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    cv2.imwrite("Encryptedmsg.jpg", img)

    os.system("start Encryptedmsg.jpg")

    return img

def decrypt_image(img, password):
    message = ""
    n = 0
    m = 0
    z = 0

    pas = input("Enter passcode for Decryption: ")

    if password == pas:
        for i in range(len(msg)):
            message = message + int_to_char[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        print("Decrypted message:", message)
    else:
        print("Not valid key")

msg = input("Enter secret message: ")
password = input("Enter password: ")

encrypted_img = encrypt_image(msg)

char_to_int = {}
int_to_char = {}
for i in range(255):
    char_to_int[chr(i)] = i
    int_to_char[i] = chr(i)

decrypt_image(encrypted_img, password)
