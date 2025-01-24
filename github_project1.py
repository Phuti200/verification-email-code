# 1. FIRST CREATE A EMPTY NOTEPAD ON YOU COMPUTER
#2. USE THAT SAME NOTEPAD FILE USE THE FILE PATH TO THE CODE BELOW UNDER file_path

import random
import string

chars= string.digits + string.ascii_letters 

chars= list(chars)
steam_key=chars.copy()

random.shuffle(steam_key)

owner_email="tshepoman"
email_pass="012345"
verify_code=""
balance=2000


def file_with_code():
    file_path="C\\......."# PASTE THE FILE PATH FROM YOU COMPUTER OF THE NOTEPAD
    file=open(file_path,"w+")
    file.write(verify_code)
    file.seek(0)
    file.close()



for i in range (4):
    type_email=input("Please enter the user email address below \n")
    type_pass=input("Please enter the the user password \n")
    if type_email != owner_email or type_pass!=email_pass:
        print("please try again either the user email/ password is incorrect \n")
        if i==3:
            print("you have inserted the email and password too many times")
    elif type_email==owner_email and type_pass == email_pass:
        print("GOOD IT WAS CORRECT \n")
        for code in email_pass:
            index=chars.index(code)
            verify_code+=steam_key[index]
        file_with_code()
        print("the verification code has been sent please check you email\n")
        for i in range(4):
            verify2=input("\n please enter enter the verifaction code that has been displayed \n")
            if verify2!=verify_code:
                print("Please enter the correct verification code \n")
                if i==3:
                    print("you have entered the too many incorrect attempts for the code Goodbye")
            elif verify2== verify_code:
                print("congrats you successfully signed in TSHEPO MANAKA great code you just did ;) \n")
             
        break
