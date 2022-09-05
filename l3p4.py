import pickle

def Register():
    with open("ACCOUNTS.DAT", "wb") as F:
        List = []
        while True:
            Ano = int(input("Enter Account Number: "))
            Name = input("Enter Account Holder's Name: ")
            while True:
                Balance = float(input("Enter Balance: "))
                if Balance < 500: print("The Balance should be atleast Rs. 500")
                else: break
            List.append([Ano, Name, Balance])
            cont = input("More account holders ?(Y/N): ").lower()
            if cont in ['n', 'N']: break
        pickle.dump(List, F)


def Transact():
    try:
        with open("ACCOUNTS.DAT", "rb+") as F:
            List = pickle.load(F)
            ind = -1
            Ano = int(input("Enter Account Number: "))
            for i in range(len(List)):
                if List[i][0]==Ano:
                    ind = i
                    break
            else:
                print("Account number not found.")
                return

            option = input("Deposit (D) / Withdraw (W): ").lower()
            if option in ['deposit', 'd']:
                AmountD = int(input("Enter Amount to deposit: "))
                List[ind][2] += AmountD
            elif option in ['withdraw', 'w']:
                while True:
                    AmountW = int(input("Enter Amount to withdraw: "))
                    if List[ind][2]-AmountW < 500:
                        print("The account must have a minimum balance of Rs. 500")
                    else:
                        List[ind][2] -= AmountW
                        break
            else:
                print("Invalid Input")

            F.seek(0)
            pickle.dump(List, F)
    except FileNotFoundError:
        print("ACCOUNTS.DAT not found.")


def DisplayAll():
    try:
        with open("ACCOUNTS.DAT", "rb") as F:
            List = pickle.load(F)
            for i in List:
                print(i)
    except FileNotFoundError:
        print("ACCOUNTS.DAT not found.")

def BankBalance():
    try:
        with open("ACCOUNTS.DAT", "rb") as F:
            List = pickle.load(F)
            T = 0
            for i in List:
                T += i[2]
            print("Sum Of Balance Of All Accounts:", T)
    except FileNotFoundError:
        print("ACCOUNTS.DAT not found.")


while True:
    Option = int(input("1: Register\n2: DisplayAll\n3: Transact\n4: BankBalance\n5: End program\n\nChoose the funtion you wish to run? "))
    
    if Option == 1:
        Register()
    elif Option == 2:
        DisplayAll()
    elif Option == 3:
        Transact()
    elif Option == 4:
        BankBalance()
    elif Option == 5:
        break
    else:
        print("Invalid Choice")
        
print("Program Ended")


'''
Output
1: Register
2: DisplayAll
3: Transact
4: BankBalance
5: End program

Choose the funtion you wish to run? 1
Enter Account Number: 550
Enter Account Holder's Name: Vibz
Enter Balance: 10000
More account holders ?(Y/N): Y
Enter Account Number: 500
Enter Account Holder's Name: Si
Enter Balance: 1000
More account holders ?(Y/N): N
1: Register
2: DisplayAll
3: Transact
4: BankBalance
5: End program

Choose the funtion you wish to run? 2
[550, 'Vibz', 10000.0]
[500, 'Si', 1000.0]
1: Register
2: DisplayAll
3: Transact
4: BankBalance
5: End program

Choose the funtion you wish to run? 3
Enter Account Number: 550
Deposit (D) / Withdraw (W): D
Enter Amount to deposit: 10000
1: Register
2: DisplayAll
3: Transact
4: BankBalance
5: End program

Choose the funtion you wish to run? 2
[550, 'Vibz', 20000.0]
[500, 'Si', 1000.0]
1: Register
2: DisplayAll
3: Transact
4: BankBalance
5: End program

Choose the funtion you wish to run? 3
Enter Account Number: 500
Deposit (D) / Withdraw (W): W
Enter Amount to withdraw: 100
1: Register
2: DisplayAll
3: Transact
4: BankBalance
5: End program

Choose the funtion you wish to run? 2
[550, 'Vibz', 20000.0]
[500, 'Si', 900.0]
1: Register
2: DisplayAll
3: Transact
4: BankBalance
5: End program

Choose the funtion you wish to run? 4
Sum Of Balance Of All Accounts: 20900.0
1: Register
2: DisplayAll
3: Transact
4: BankBalance
5: End program

Choose the funtion you wish to run? 5
Program Ended
'''
