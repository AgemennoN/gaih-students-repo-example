#Explain your work
"""
Kullanıcıdan Username ve Password istedim, Ardından bunları tekrardan girmesini isteyip doğruluğunu
karşılaştırdım. Extra kısmında bunları Login_infos isimli dictionary oluşturup ilk istediğim username
ve passwordu içine attım. ikinci sorduklarımı bunlarla karşılaştırdım.
"""
#Question
"""
Username = input("Enter an Username: ")
Password = input("Enter an Password: ")

Username_toCheck = input("\nEnter Your Username: ")

if Username == Username_toCheck:
    Password_toCheck = input("Enter Your Password: ")
    if Password == Password_toCheck:
        print("Logined Succesfully")
    else:
        print("Your Password is incorrect")
else:
    print(f'\nYour Username "{Username_toCheck}" does not exist')
"""
#Extra Part
Login_infos = {"Username": "","Password": ""}  #Initilazing the dictionary
Login_infos["Username"] = input("Enter an Username: ")
Login_infos["Password"] = input("Enter an Password: ")

Username_toCheck = input("\nEnter Your Username: ")

if Login_infos["Username"] == Username_toCheck:
    if Login_infos["Password"] == input("Enter Your Password: "):
        print("Logined Succesfully")
    else:
        print("Your Password is incorrect")
else:
    print(f'\nYour Username "{Username_toCheck}" does not exist')
