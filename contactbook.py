contact = {}


def view_contact():
    print("name\t\tconatct number \t\tAddress")
    for key in contact:
        print("{}\t\t{}\t\t{}\t\t{}".format(key,contact[key][0],contact [key][1],contact[key][2]))

while True:
    choice = int(input("1.Add new contact\n2.View contact\n3.Search contact\n4.Upadate contact\n5.Delete contact\n6.Exit\nEnter your choice:  "))
    if choice == 1:
      name=input("enter the contact name: ")
      phone=int(input("enter the phone number: "))
      email = input("Enter the Email-ID: ")
      address = input("Enter your address: ")
      contact[name]=phone, email, address



    elif choice == 2:
        if not contact:
            print("empty contact book")
        else:
             view_contact 



    elif choice == 3:
         search_name = input("enter the contact name")
         if search_name in contact:
            print (search_name,'s contact number is',contact[search_name])  
         else:
            print("Name not found in contact")



    elif choice == 4:
         update_contact = input("enter the contact name to be updated: ") 
         if update_contact in contact:
            phone = input("enter phone number: ")
            email = input("enter Email ID: ")
            address = input("Enter the address: ") 
            contact[update_contact]= phone,email,address  
            print("contact updated")
            view_contact()
         else:
            print("Name is not found")


            
    elif choice == 5:
        del_contact = input("enter the contact to be deleted") 
        if del_contact in contact:
            confirmation = input("Do you want to delete this contact (y/n)?")
            if confirmation =="y" or confirmation == "Y":
                contact.pop(del_contact)
                view_contact()  
        else:
                print("Name not found in contact")    
    else:
        break      
         