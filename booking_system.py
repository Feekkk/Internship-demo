import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class BookingApp:

    def __init__(self, root):
        self.root = root
        self.root.title("UniKL Booking System")
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
        if username == "admin" and password == "unikl123":
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
        self.root.title("UniKL Booking System - Main Menu")
        
        menu_frame = ttk.Frame(self.root, padding=20)
        menu_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(menu_frame, text="Booking Menu", font=("Arial", 16, "bold")).pack(pady=10)
        
        ttk.Button(menu_frame, text="📅 Book a Room", width=25, 
                  command=lambda: messagebox.showinfo("Info", "Book Room feature coming soon!")).pack(pady=10)
        
        ttk.Button(menu_frame, text="👀 View My Bookings", width=25,
                  command=lambda: messagebox.showinfo("Info", "View Bookings feature coming soon!")).pack(pady=10)
        
        ttk.Button(menu_frame, text="❌ Cancel Booking", width=25,
                  command=lambda: messagebox.showinfo("Info", "Cancel Booking feature coming soon!")).pack(pady=10)
        
        ttk.Button(menu_frame, text="🚪 Exit", width=25, command=self.root.quit).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = BookingApp(root)
    root.mainloop()