import tkinter as tk
from tkinter import messagebox
import pickle


class EventManagementSystemGUI:
    def __init__(self, master):
        # Initialize the GUI
        self.master = master
        self.master.title("Event Management System")

        # Create the GUI components
        self.create_widgets()

        # Load data from binary files
        self.load_data()

    def create_widgets(self):
        # Create buttons for various functionalities
        self.add_button = tk.Button(self.master, text="Add", command=self.add_data)
        self.add_button.grid(row=0, column=0, padx=10, pady=5)

        self.delete_button = tk.Button(self.master, text="Delete", command=self.delete_data)
        self.delete_button.grid(row=0, column=1, padx=10, pady=5)

        self.modify_button = tk.Button(self.master, text="Modify", command=self.modify_data)
        self.modify_button.grid(row=0, column=2, padx=10, pady=5)

        self.display_button = tk.Button(self.master, text="Display", command=self.display_data)
        self.display_button.grid(row=0, column=3, padx=10, pady=5)

        # Create entry and label for ID input
        self.id_label = tk.Label(self.master, text="Enter ID:")
        self.id_label.grid(row=1, column=0, padx=10, pady=5)

        self.id_entry = tk.Entry(self.master)
        self.id_entry.grid(row=1, column=1, padx=10, pady=5)

        # Create display text area
        self.display_text = tk.Text(self.master, height=20, width=80)
        self.display_text.grid(row=2, column=0, columnspan=4, padx=10, pady=5)

    def load_data(self):
        # Load data from binary files and store in class variables
        try:
            with open("employees.pkl", "rb") as file:
                self.employees = pickle.load(file)
        except FileNotFoundError:
            self.employees = []

        try:
            with open("events.pkl", "rb") as file:
                self.events = pickle.load(file)
        except FileNotFoundError:
            self.events = []

        try:
            with open("clients.pkl", "rb") as file:
                self.clients = pickle.load(file)
        except FileNotFoundError:
            self.clients = []

        try:
            with open("guests.pkl", "rb") as file:
                self.guests = pickle.load(file)
        except FileNotFoundError:
            self.guests = []

        try:
            with open("suppliers.pkl", "rb") as file:
                self.suppliers = pickle.load(file)
        except FileNotFoundError:
            self.suppliers = []

        try:
            with open("venues.pkl", "rb") as file:
                self.venues = pickle.load(file)
        except FileNotFoundError:
            self.venues = []

    def save_data(self):
        # Save data to binary files
        with open("employees.pkl", "wb") as file:
            pickle.dump(self.employees, file)

        with open("events.pkl", "wb") as file:
            pickle.dump(self.events, file)

        with open("clients.pkl", "wb") as file:
            pickle.dump(self.clients, file)

        with open("guests.pkl", "wb") as file:
            pickle.dump(self.guests, file)

        with open("suppliers.pkl", "wb") as file:
            pickle.dump(self.suppliers, file)

        with open("venues.pkl", "wb") as file:
            pickle.dump(self.venues, file)

    def add_data(self):
        # Functionality to add data to the system
        pass  # Implement adding data functionality

    def delete_data(self):
        # Functionality to delete data from the system
        pass  # Implement deleting data functionality

    def modify_data(self):
        # Functionality to modify data in the system
        pass  # Implement modifying data functionality

    def display_data(self):
        # Functionality to display data based on ID
        pass  # Implement displaying data functionality


# Main function
def main():
    root = tk.Tk()
    app = EventManagementSystemGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()