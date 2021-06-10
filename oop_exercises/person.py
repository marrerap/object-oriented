# creating the person class for the main page

class Person:
    # this is an instance variable(attribute) added to each instance created
    
    
    
    
    
    
    # creating a funciton to fill in values for name email and phone number
    def __init__(self, name, email, phone):
         # this will fill in with user input
         self.name = name
         self.email = email
         self.phone = phone
         self.friends = []

    def greet(self, other_person):
         print(f"Hello {other_person.name}, I am {self.name}!")

    def print_contact_info(self,):
        print(f"{self.name}'s email: {self.email}")
        print(f"{self.name}'s phone number: {self.phone}")

    def add_friend(self, friend_name):
        self.friends.append(friend_name)

    def num_friends(self):
        return len(self.friends)

