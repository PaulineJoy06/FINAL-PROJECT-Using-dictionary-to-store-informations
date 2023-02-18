print("\n\t\t ********PROGRAMMED BY:******** ")
print("\t\t ***Pauline Joy R. Mingo***\n ")
print("****FINAL PROJECT FOR DSA****")

# Write a python program for storing students' personal information.
# Display a menu of options.
# Perform the selected options.
# Use dictionary to store the info and the full name as key.

Informations = []
Person1 = {"FullName": "Jenna Ortega", 
            "Age": "19", 
            "Gender":"Female",
            "Number": "09123456789",
            "Address": "Rizal"}
Person2 = {"FullName": "Paul Klein", 
            "Age": "20",
            "Gender":"Male","Number": "09543677689",
            "Address": "Tokyo"}
Person3 = {"FullName": "Taylor Swift", 
            "Age": "25", 
            "Gender":"Female",
            "Number": "09433659879",
            "Address": "New York"}
Person4 = {"FullName": "Thomas Scott",
            "Age": "19", 
            "Gender":"Male",
            "Number": "09712436879",
            "Address": "Manila"}

Informations.append(Person1)
Informations.append(Person2)
Informations.append(Person3)
Informations.append(Person4)
def menu():
    print("""
             >>>>> WELCOME TO MY PROGRAM <<<<<
                _________________________________
              ||          MENU OPTIONS          ||
              ||________________________________||  
              ||                                ||
              ||        1. ADD AN ITEM          ||
              ||        2. SEARCH INFORMATION   ||   
              ||        3. VIEW INFORMATION     ||
              ||        4. EXIT                 ||
              ||________________________________||
        """)
def end():
    print(">>>>> THANK YOU FOR USING THIS PROGRAM! <<<<<")

menu()
Options = int(input("\t\nSELECT AN OPTION (Choose from 1-3): "))


while True:
    if Options == 1:
        print("\t\t\t>>>>> PLEASE ENTER YOUR PERSONAL DATA <<<<<")
        Name = (input("\n\tPLEASE ENTER YOUR FULL NAME:      "))
        Age = int(input("\tPLEASE ENTER YOUR AGE:            "))
        Gender = (input("\tPLEASE ENTER YOUR GENDER(F/M):    "))
        PhoneNumber = (int(input("\tPLEASE ENTER YOUR NUMBER:         ")))
        CityAddress = (input("\tPLEASE ENTER YOU CITY ADDRESS:    "))
        print("\t>>>>> INFORMATIONS ARE SAVED! <<<<<")
        person = {"Name": Name, "A": Age, "G": Gender, "Add": CityAddress, "Num": PhoneNumber}
        print("\n\tThese are the informations: \n\t", person)
        

    elif Options == 2:
        search = input("ENTER THE NAME YOU WANT TO SEARCH: ")
        for i in range(len(Informations)):
            person = Informations[i]
            if person['FullName'] == search:
                print("\n\t\t\t\t\t>>>>> RESULTS <<<<<")
                print(person)
                 
    elif Options == 3:   
        for i in range(len(Informations)):
            print("\n\t\t\t\t\t>>>>> THESE ARE THE INFORMATIONS <<<<<")
            print(Informations[i])

    elif Options == 4:
        exit = input("\tDO YOU WANT TO EXIT THE PROGRAM? (YES / NO): ")
        if exit == "NO":
            menu
        else:
            print("\n\t\t>>>>>> Thank you so much for using this program! <<<<<<")
            break
    menu()
    Options = int(input("\t\nSELECT AN OPTION (Choose from 1-4): "))
                
