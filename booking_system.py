print("Welcome to UniKL Booking System")

input("Press Enter to continue...")
print("This is a simple booking system for UniKL.")
print("You can book rooms and manage your bookings here.")
print("Please follow the instructions to make a booking.")
print("Thank you for using UniKL Booking System!")
print("For any assistance, contact support@unikl.edu.my")
print("Enjoy your experience!")
print("Goodbye!")

input("Press C to continue or Exit to quit: ")
if input().strip().lower() == "c":
    print("Continuing...")
else:
    print("Exiting...")
    exit()

class UserAccount:
    def __init__(self):
        self.username = ""
        self.password = ""

user1 = UserAccount()
user1.username = "admin"
user1.password = "admin123"

username_input = input("Enter your username: ")
if username_input == user1.username:
    print("Username found.")
else:
    print("Username not found.")
    password_input = input("Enter your password: ")
    if password_input == user1.password:
        print("Login successful!")
    else:
        print("Incorrect password.")
    exit()

print("Welcome back, admin!")
print("You can now proceed to book a room.")
