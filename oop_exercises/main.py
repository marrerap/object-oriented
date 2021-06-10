from vehicle import Vehicle
from person import Person



sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny_car = Vehicle("Lexus", "LFA", "2012")
jordan_car = Vehicle('Geo', 'Metro', "2000")





Person.greet(sonny, jordan)
sonny_car.car_info()

Person.greet(jordan, sonny)
jordan_car.car_info()
#another way to call on the function "jordan.greet(sonny)""

#the following code was commented out due to new function print_contact_info
#print(sonny.email, sonny.phone,"\n" ,jordan.email, jordan.phone)

sonny.print_contact_info()
jordan.print_contact_info()

# created a method for appending friends in the person class
# jordan.friends.append(sonny)
# sonny.friends.append(jordan)

# print(len(jordan.friends))
# print(len(jordan.friends))

jordan.add_friend(sonny)
sonny.add_friend(jordan)

print(jordan.num_friends())
print(sonny.num_friends())


