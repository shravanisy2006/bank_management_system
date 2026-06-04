import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open (database) as fs:
                data = json.loads(fs.read())

        else:
            print("No such file exists.")

    except Exception as err:
        print(f"An expection occured as {err}")

    @classmethod
    def __Update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerator(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        nums = random.choices(string.digits,k=3)
        spchar = random.choices("@#$%@._*",k=1)
        id = alpha + nums + spchar
        random.shuffle(id)
        return "".join(id)

    def Createaccount(self):
        info = {
            "name" : input("Tell your name: "),
            "age" : int(input("Tell your age: ")),
            "email" : input("Tell your mail id: "),
            "pin" : int(input("Tell your pin:")),
            "accountNo." : Bank.__accountgenerator(),
            "balance" : 0
        }
        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry you cant create an account.")
        else:
            print("You have successfully created an account.")
            print("The account details are as follows: ")

            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your account number.")

            Bank.data.append(info)

            Bank.__Update()


    def deposit(self):
        accnum = input("Enter yout account number: ")
        pin = int(input("Please enter your pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnum and i['pin'] == pin]

        if userdata == False:
            print("Sorry no data found.")
        
        else:
            amount = int(input("Enter the amount you want to deposit: "))

            if amount > 10000 or amount < 0 :
                print("Sorry amount is not possible to be deposited.")

            else:
                userdata[0]['balance'] += amount
                Bank.__Update()
                print("Amount deposited successfully.")
        

    def withdraw(self):
        accnum = input("Enter yout account number: ")
        pin = int(input("Please enter your pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnum and i['pin'] == pin]

        if userdata == False:
            print("Sorry no data found.")
        
        else:
            amount = int(input("Enter the amount you want to wthdraw: "))

            if userdata[0]['balance'] < amount :
                print("Sorry the ballanced amount is not enough to be withdrawn.")

            else:
                userdata[0]['balance'] -= amount
                Bank.__Update()
                print("Amount withdrawn successfully.")
                

    def showdetails(self):
        accnum = input("Enter yout account number: ")
        pin = int(input("Please enter your pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnum and i['pin'] == pin]
        print("Your information is as follows:\n\n\n ")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")


    def updatedetails(self):
        accnum = input("Enter yout account number: ")
        pin = int(input("Please enter your pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnum and i['pin'] == pin]

        if userdata == False:
            print("No such account found.")

        else:
            print("You can't change the age , account number and the balance.")

            print("Fill the details in case you want to change or else leave it empty.")

            newdata = {
                "name" : input("Please enter the new name: "),
                "email" : input("Please enter the new mail id: "),
                "pin" : input("Please enter the new pin if you want to change: ")
            }


            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']

            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']

            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']

            newdata['age'] = userdata[0]['age']

            newdata['accountNo.'] = userdata[0]['accountNo.']

            newdata['balance'] = userdata[0]['balance']

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])


            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue

                else:
                    userdata[0][i] = newdata[i]

            Bank.__Update()
            print("Account information updated successfully.")
            print("Your updated account information is as follows: ") 
            for i in newdata:
                print(f"{i} : {newdata[i]}")


    def delete(self):
        accnum = input("Enter yout account number: ")
        pin = int(input("Please enter your pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnum and i['pin'] == pin]

        if userdata == False:
            print("No such account found.")

        else:
            check = input("Press y if you actually want to delete the account or press n.")
            if check == 'n' or check == 'N':
                print("bypassed.")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account deleted successfully.")

                Bank.__Update()


user = Bank()

print("Welcome !")

print("""
🏦 ====================================
         BANK MANAGEMENT SYSTEM
====================================

1. Create Account
2. Deposit Money
3. Withdraw Money
4. View Details
5. Update Details
6. Delete Account

====================================
""")


check = int(input("Tell your response: "))

if check == 1:
    user.Createaccount()

if check == 2:
    user.deposit()

if check == 3:
    user.withdraw()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.delete()