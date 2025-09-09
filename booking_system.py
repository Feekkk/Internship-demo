import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class BookingApp:

    def __init__(self, root):
        self.root = root
        self.root.title("UniKL Laboratory Booking System")
        self.root.geometry("400x300")

        # Login frame
        login_frame = ttk.Frame(root, padding=20)
        login_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(login_frame, text="UniKL Booking System", font=("Arial", 16, "bold")).pack(pady=10)

        ttk.Label(login_frame, text="Username:").pack(pady=5)
        self.username_entry = ttk.Entry(login_frame, width=25)
        self.username_entry.pack(pady=5)

        ttk.Label(login_frame, text="Password:").pack(pady=5)
        self.password_entry = ttk.Entry(login_frame, show="*", width=25)
        self.password_entry.pack(pady=5)

        ttk.Button(login_frame, text="Login", command=self.login).pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "user" and password == "user123":
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            self.open_booking_window()
        else:
            messagebox.showerror("Login Failed", "Please enter a valid username and password.")

    def open_booking_window(self):
        # Clear the login window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Create booking menu
        self.root.geometry("500x400")
        self.root.title("UniKL Class System - Main Menu")
        
        menu_frame = ttk.Frame(self.root, padding=20)
        menu_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(menu_frame, text="Booking Class", font=("Arial", 16, "bold")).pack(pady=10)
        
        ttk.Button(menu_frame, text="📅 Book a Class", width=25, 
                  command=self.book_class_window).pack(pady=10)

        ttk.Button(menu_frame, text="📖 Booking Description", width=25,
                  command=lambda: messagebox.showinfo("Info", "Booking Description feature coming soon!")).pack(pady=10)

        ttk.Button(menu_frame, text="👀 View My Bookings", width=25,
                  command=lambda: messagebox.showinfo("Info", "View Bookings feature coming soon!")).pack(pady=10)
        
        ttk.Button(menu_frame, text="❌ Cancel Booking", width=25,
                  command=lambda: messagebox.showinfo("Info", "Cancel Booking feature coming soon!")).pack(pady=10)
        
        ttk.Button(menu_frame, text="🚪 Exit", width=25, command=self.root.quit).pack(pady=10)

    def book_class_window(self):
        """"Open a new window to book a class"""

        # clear current window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # booking interface
        self.root.geometry("600x500")
        self.root.title("UniKL Class System - Book a Class")

        booking_frame = ttk.Frame(self.root, padding=20)
        booking_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(booking_frame, text="Book a Class", font=("Arial", 16, "bold")).pack(pady=10)

        # Class selection
        ttk.Label(booking_frame, text="Select Class:").pack(pady=5)
        self.class_var = tk.StringVar()
        class_combo = ttk.Combobox(booking_frame, textvariable=self.class_var, state="readonly")
        class_combo['values'] = ("Math 101", "Physics 201", "Chemistry 301", "Biology 401")
        class_combo.pack(pady=5)

        # Date selection
        ttk.Label(booking_frame, text="Select Date (DD/MM/YYYY):").pack(pady=5)
        self.date_var = tk.StringVar()
        self.date_entry = ttk.Entry(booking_frame, textvariable=self.date_var, width=25)
        self.date_entry.pack(pady=5)

        # Time selection
        ttk.Label(booking_frame, text="Select Time:").pack(pady=5)
        self.time_var = tk.StringVar()
        self.time_entry = ttk.Entry(booking_frame, textvariable=self.time_var, width=25)
        self.time_entry.pack(pady=5)

        # Buttons
        button_frame = ttk.Frame(booking_frame)
        button_frame.pack(pady=20)

        ttk.Button(button_frame, text="Submit Booking", command=self.submit_booking).grid(row=0, column=0, padx=10)
        ttk.Button(button_frame, text="Back to Menu", command=self.open_booking_window).grid(row=0, column=1, padx=10)

    def submit_booking(self):
        selected_class = self.class_var.get()
        selected_date = self.date_var.get()
        selected_time = self.time_var.get()

        if not selected_class or not selected_date or not selected_time:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Here you would normally save the booking to a database or file
        messagebox.showinfo("Booking Confirmed", f"You have booked {selected_class} on {selected_date} at {selected_time}.")
        self.open_booking_window()

if __name__ == "__main__":
    root = tk.Tk()
    app = BookingApp(root)
    root.mainloop()