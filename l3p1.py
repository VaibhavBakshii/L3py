def GetStory():
    
    #To create a text file named STORY.TXT which contains text lines entered by the user.
 
    with open ("STORY.TXT", "w") as f:
        while True:
            line = input("Enter the line you want to add to STORY.TXT: ")
            f.write(line + "\n")
            cont = input("Do you want to add another line? (y/n): ")
            if cont == "n":
                break

def ViewStory():
  
    #To read and display the entire content of text file STORY.TXT on the screen.
    
    with open ("STORY.TXT", "r") as f:
        for line in f.readlines():
            print(line)

def Words():
    
    #To read and display each word of the text file STORY.TXT in different lines on the screen.
    
    with open("STORY.TXT", "r") as f:
        for line in f.readlines():
            for word in line.split():
                print(word)

def AllWords():
    
    #To read, count and display number of words present in the text file STORY.TXT.
    
    count = 0
    with open("STORY.TXT", "r") as f:
        for line in f.readlines():
            for word in line.split():
                count += 1
                print(word)
        print("The total number of words in STORY.TXT is", count)

while True:
    choice = int(input("1: GetStory\n2: ViewStory\n3: Words\n4: AllWords\n5: End program\n\nWhich function do you want to run?"))
    
    if choice == 1:
        GetStory()
    elif choice == 2:
        ViewStory()
    elif choice == 3:
        Words()
    elif choice == 4:
        AllWords()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
        
print("Program ended")


