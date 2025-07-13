#contactbook
contact_book = {
    "rohin" :92638618373,
    "john":45678901324,
    "alrnold": 95626537263,
    "alex": 59716928631
}
new_num = {"tenx" :2869189739 ,"goldie" :87721567792}#update or new numbers
contact_book.update(new_num)

def search_contact(name):
    if name in contact_book:
        print(name.title(),contact_book[name])
    else:
        print("number not avaiable")

def delete_contact(name):
    if name in contact_book:
        del contact_book[name]
        print("the number is deleted")
    else:
        print("cannot delete,number does not exist")
        
def view_all_contacts():
    print("\n📒 Current Contact Book:")
    for name, number in contact_book.items():
        print(f"- {name.title()}: {number}")
    print()
    
    
view_all_contacts()               # Show full contact list
search_contact("alex")            # Search for Alex's number
delete_contact("john")            # Delete John
search_contact("john")            # Try searching John again
view_all_contacts()

