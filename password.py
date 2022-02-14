from cgitb import text
import string
import random
out = open("output.txt","w+")
#string module
letters = string.ascii_letters #upper and lowercase letters
numbers = string.digits #digits 0-9
characters = string.punctuation #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

def user_input():
    try:
        lenght = int(input(" Password Lenght (8-16): "))
        if (lenght < 8):
            print("Number is too small (min. 8)")
            user_input()
        if (lenght > 32):
            print("Number way too big (max.32)")
            user_input()
        else:
            pass_generator(lenght)

    except ValueError:
        print("Expected a number!")
    except Exception as err:
        print(err)
    

def pass_generator(lenght):
    combine = letters + numbers + characters
    temp = random.sample(combine,lenght)
    rand_password = "".join(temp)

    print(rand_password)
    out.write("\n")
    text = rand_password
    out.write(text)

    check = input("Generate new? (Y/N) \n")
    try:
        if check.upper() == "Y":
            pass_generator(lenght)
        if check.upper() == "N":
            out.close()
            exit()
        else:
            out.close()
            exit()

    except Exception as err:
        out.close()
        print(err)
        exit()
