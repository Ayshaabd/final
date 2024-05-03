# Define the Employee class
class Employee:
    # Constructor to initialize employee attributes
    def __init__(self, name, employeeID, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails):
        self.name = name
        self.employeeID = employeeID
        self.department = department
        self.jobTitle = jobTitle
        self.basicSalary = basicSalary
        self.age = age
        self.dateOfBirth = dateOfBirth
        self.passportDetails = passportDetails

# Define the Manager class, which inherits from Employee
class Manager(Employee):
    # Constructor to initialize manager attributes
    def __init__(self, name, employeeID, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails):
        # Call the constructor of the superclass (Employee)
        super().__init__(name, employeeID, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails)

# Define the Salesperson class, which inherits from Employee
class Salesperson(Employee):
    # Constructor to initialize salesperson attributes
    def __init__(self, name, employeeID, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails):
        # Call the constructor of the superclass (Employee)
        super().__init__(name, employeeID, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails)

# Define the Event class
class Event:
    # Constructor to initialize event attributes
    def __init__(self, eventID, type, theme, date, time, duration, venueAddress, clientID, guestList, cateringCompany, cleaningCompany, decorationsCompany, entertainmentCompany, furnitureSupplyCompany, invoice):
        self.eventID = eventID
        self.type = type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venueAddress = venueAddress
        self.clientID = clientID
        self.guestList = guestList
        self.cateringCompany = cateringCompany
        self.cleaningCompany = cleaningCompany
        self.decorationsCompany = decorationsCompany
        self.entertainmentCompany = entertainmentCompany
        self.furnitureSupplyCompany = furnitureSupplyCompany
        self.invoice = invoice

# Define the Client class
class Client:
    # Constructor to initialize client attributes
    def __init__(self, clientID, name, address, contactDetails, budget):
        self.clientID = clientID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails
        self.budget = budget

# Define the Guest class
class Guest:
    # Constructor to initialize guest attributes
    def __init__(self, guestID, name, address, contactDetails):
        self.guestID = guestID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails

# Define the Supplier class
class Supplier:
    # Constructor to initialize supplier attributes
    def __init__(self, supplierID, name, address, contactDetails):
        self.supplierID = supplierID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails

# Define the Venue class
class Venue:
    # Constructor to initialize venue attributes
    def __init__(self, venueID, name, address, contact, minGuests, maxGuests):
        self.venueID = venueID
        self.name = name
        self.address = address
        self.contact = contact
        self.minGuests = minGuests
        self.maxGuests = maxGuests

# Test Cases
if __name__ == "__main__":
    # Create Employees
    manager1 = Manager("Aysha Abdullah", "001", "Sales", "Manager", 50000, 35, "1999-04-35", "ABC123")
    salesperson1 = Salesperson("Shamma Mohammed", "002", "Sales", "Salesperson", 30000, 28, "1995-08-06", "XYZ456")

    # Create Clients
    client1 = Client("C001", "ABC Corp", "123 Main St", "123-456-7890", 10000)

    # Create Guests
    guest1 = Guest("G001", "Guest1", "456 Elm St", "456-789-0123")
    guest2 = Guest("G002", "Guest2", "789 Oak St", "789-012-3456")

    # Create Suppliers
    supplier1 = Supplier("S001", "Catering Inc", "789 Maple St", "789-456-1230")

    # Create Venue
    venue1 = Venue("V001", "Event Hall", "100 Pine St", "555-123-4567", 50, 100)

    # Create Event
    event1 = Event("E001", "Wedding", "Romantic", "2024-06-15", "18:00", 4, "100 Pine St", "C001", [guest1, guest2], supplier1, None, None, None, None, 15000)

    # Display Test Case Results
    print("Employee:", manager1.name, "-", manager1.jobTitle)
    print("Client:", client1.name)
    print("Guests:", [guest.name for guest in event1.guestList])
    print("Supplier:", supplier1.name)
    print("Venue:", venue1.name)
    print("Event:", event1.theme, event1.type, "on", event1.date, "at", event1.venueAddress)

