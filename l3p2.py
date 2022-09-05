def CreateNotes():
    '''
    To create a text file NOTES.TXT to have text entered by user as lines of text.
    '''
    with open ("NOTES.TXT", "w") as f:
        while True:
            line = input("Enter the line you want to add to NOTES.TXT: ")
            f.write(line + "\n")
            cont = input("Do you want to add another line? (y/n): ")
            if cont == "n":
                break

def CountAVD():
    '''
    To read the contents of the text file NOTES.TXT and count and print the number of 
    Alphabets, Vowels and Digits present in the file.
    '''
    alphabets = 0
    vowels = 0
    digits = 0

    with open("NOTES.TXT", "r") as f:
        for char in f.read():

            if char.isdigit():
                digits += 1
            elif char.lower() in 'aeiou':
                vowels += 1
                alphabets
            elif char.isalpha():
                alphabets += 1
            
        print("Number of alphabets present in the file:", alphabets)
        print("Number of vowels present in the file:", vowels)
        print("Number of digits present in the file:", digits)

def ShowNotes():
    '''
    To display the contents of text file NOTES.TXT.
    '''
    with open ("NOTES.TXT", "r") as f:
        for line in f.readlines():
            print(line.strip('\n'))

def RevText():
    '''
    To read the contents of the text file NOTES.TXT, and print reverse of those lines which start 
    with an alphabet ‘T’.
    '''
    with open ("NOTES.TXT", "r") as f:
        for line in f.readlines():
            if line.lower().startswith('t'):
                print(line[::-1].lstrip('\n'))

def CountLines():
    '''
    To read, count and display the number of lines present in the text file NOTES.TXT.
    '''
    count = 0
    with open ("NOTES.TXT", "r") as f:
        for line in f.readlines():
            count += 1
    print("Number of lines in NOTES.TXT:", count)

while True:
    choice = int(input("1: CreateNotes\n2: CountAVD\n3: ShowNotes\n4: RevText\n5: CountLines\n6: End program\n\nWhich function do you want to run? "))
    
    if choice == 1:
        CreateNotes()
    elif choice == 2:
        CountAVD()
    elif choice == 3:
        ShowNotes()
    elif choice == 4:
        RevText()
    elif choice == 5:
        CountLines()
    elif choice == 6:
        break
    else:
        print("Invalid choice")
        
print("Program ended")
