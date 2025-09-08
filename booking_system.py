print("Welcome to UniKL Booking System")

input("Press Enter to continue...")
print("This is a simple booking system for UniKL.")
print("You can book rooms and manage your bookings here.")
print("Please follow the instructions to make a booking.")
print("Thank you for using UniKL Booking System!")
print("For any assistance, contact support@unikl.edu.my")
print("Enjoy your experience!")
print("Goodbye!")

class UserAccount:
    def __init__(self):
        self.username = ""
        self.password = ""

user1 = UserAccount()
user1.username = "admin"
user1.password = "admin123"

input = input("Enter your username: ")
if input == user1.username:
    print("Username found.")
else:
    print("Username not found.")
    input_pass = input("Enter your password: ")
    if input_pass == user1.password:
        print("Login successful!")
    else:
        print("Incorrect password.")
    exit()

print("Welcome back, admin!")
print("You can now proceed to book a room.")
