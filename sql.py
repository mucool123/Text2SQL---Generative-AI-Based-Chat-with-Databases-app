import sqlite3

# Connect to sqlite
connection = sqlite3.connect("patient.db")

# Create a cursor object to insert, update, delete instances or retrieve
cursor = connection.cursor()

# Create the table
table_info = """ 
CREATE TABLE IF NOT EXISTS PATIENT(
    PatientID INT PRIMARY KEY,
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    DateOfBirth DATE,
    Gender CHAR(1),
    Phone VARCHAR(20),
    Email VARCHAR(100),
    Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    ZipCode VARCHAR(10),
    EmergencyContactName VARCHAR(100),
    EmergencyContactPhone VARCHAR(20),
    DateRegistered TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

# Execute the CREATE TABLE command
cursor.execute(table_info)


insert_queries = [
    "INSERT INTO PATIENT VALUES (1, 'John', 'Doe', '1980-01-01', 'M', '123-456-7890', 'johndoe@example.com', '123 Elm Street', 'Anytown', 'Anystate', '12345', 'Jane Doe', '987-654-3210', CURRENT_TIMESTAMP)",
    "INSERT INTO PATIENT VALUES (2, 'Jane', 'Smith', '1982-02-02', 'F', '234-567-8901', 'janesmith@example.com', '456 Oak Street', 'Othertown', 'Otherstate', '23456', 'John Smith', '876-543-2109', CURRENT_TIMESTAMP)",
    "INSERT INTO PATIENT VALUES (3, 'Emily', 'Johnson', '1975-03-03', 'F', '345-678-9012', 'emilyjohnson@example.com', '789 Pine Street', 'Sometown', 'Somestate', '34567', 'Evan Johnson', '765-432-1098', CURRENT_TIMESTAMP)",
    "INSERT INTO PATIENT VALUES (4, 'Michael', 'Williams', '1988-04-04', 'M', '456-789-0123', 'michaelwilliams@example.com', '123 Birch Street', 'Newtown', 'Newstate', '45678', 'Michelle Williams', '654-321-0987', CURRENT_TIMESTAMP)",
    "INSERT INTO PATIENT VALUES (5, 'Emma', 'Brown', '1990-05-05', 'F', '567-890-1234', 'emmabrown@example.com', '456 Redwood Street', 'Oldtown', 'Oldstate', '56789', 'Ethan Brown', '543-210-9876', CURRENT_TIMESTAMP)",
    "INSERT INTO PATIENT VALUES (6, 'William', 'Jones', '1978-06-06', 'M', '678-901-2345', 'williamjones@example.com', '789 Cedar Street', 'Cooltown', 'Coolstate', '67890', 'Wendy Jones', '432-109-8765', CURRENT_TIMESTAMP)",
    "INSERT INTO PATIENT VALUES (7, 'Olivia', 'Garcia', '1985-07-07', 'F', '789-012-3456', 'oliviagarcia@example.com', '123 Maple Street', 'Warmtown', 'Warmstate', '78901', 'Oscar Garcia', '321-098-7654', CURRENT_TIMESTAMP)",
    "INSERT INTO PATIENT VALUES (8, 'Ethan', 'Miller', '1972-08-08', 'M', '890-123-4567', 'ethanmiller@example.com', '456 Elm Street', 'Brighttown', 'Brightstate', '89012', 'Eva Miller', '210-987-6543', CURRENT_TIMESTAMP)",
    "INSERT INTO PATIENT VALUES (9, 'Ava', 'Davis', '1992-09-09', 'F', '901-234-5678', 'avadavis@example.com', '789 Oak Street', 'Darktown', 'Darkstate', '90123', 'Adam Davis', '109-876-5432', CURRENT_TIMESTAMP)",
    "INSERT INTO PATIENT VALUES (10, 'Alexander', 'Wilson', '1983-10-10', 'M', '012-345-6789', 'alexanderwilson@example.com', '123 Pine Street', 'Lighttown', 'Lightstate', '01234', 'Alexa Wilson', '098-765-4321', CURRENT_TIMESTAMP)",
    "INSERT INTO PATIENT VALUES (11, 'Sophia', 'Martinez', '1993-11-11', 'F', '123-456-7891', 'sophiamartinez@example.com', '456 Birch Street', 'Midtown', 'Midstate', '12345', 'Sam Martinez', '987-654-3212', CURRENT_TIMESTAMP)",
    "INSERT INTO PATIENT VALUES (12, 'Matthew', 'Anderson', '1984-12-12', 'M', '234-567-8902', 'matthewanderson@example.com', '789 Redwood Street', 'Uptown', 'Upstate', '23456', 'Mia Anderson', '876-543-2108', CURRENT_TIMESTAMP)",
    "INSERT INTO PATIENT VALUES (13, 'Isabella', 'Thomas', '1981-01-13', 'F', '345-678-9013', 'isabellathomas@example.com', '123 Cedar Street', 'Downtown', 'Downstate', '34567', 'Ian Thomas', '765-432-1097', CURRENT_TIMESTAMP)",
    "INSERT INTO PATIENT VALUES (14, 'Jacob', 'Jackson', '1979-02-14', 'M', '456-789-0124', 'jacobjackson@example.com', '456 Maple Street', 'Easttown', 'Eaststate', '45678', 'Jade Jackson', '654-321-0986', CURRENT_TIMESTAMP)",
    "INSERT INTO PATIENT VALUES (15, 'Mia', 'Harris', '1994-03-15', 'F', '567-890-1235', 'miaHarris@example.com', '789 Elm Street', 'Westtown', 'Weststate', '56789', 'Miles Harris', '543-210-9875', CURRENT_TIMESTAMP)",
    "INSERT INTO PATIENT VALUES (16, 'Noah', 'Clark', '1976-04-16', 'M', '678-901-2346', 'noahclark@example.com', '123 Oak Street', 'Northtown', 'Northstate', '67890', 'Natalie Clark', '432-109-8764', CURRENT_TIMESTAMP)",
    "INSERT INTO PATIENT VALUES (17, 'Charlotte', 'Rodriguez', '1989-05-17', 'F', '789-012-3457', 'charlotterodriguez@example.com', '456 Pine Street', 'Southtown', 'Southstate', '78901', 'Charles Rodriguez', '321-098-7653', CURRENT_TIMESTAMP)",
    "INSERT INTO PATIENT VALUES (18, 'Liam', 'Lewis', '1986-06-18', 'M', '890-123-4568', 'liamlewis@example.com', '789 Birch Street', 'Eastertown', 'Easterstate', '89012', 'Lily Lewis', '210-987-6542', CURRENT_TIMESTAMP)",
    "INSERT INTO PATIENT VALUES (19, 'Amelia', 'Walker', '1974-07-19', 'F', '901-234-5679', 'ameliawalker@example.com', '123 Redwood Street', 'Westertown', 'Westerstate', '90123', 'Aaron Walker', '109-876-5431', CURRENT_TIMESTAMP)",
    "INSERT INTO PATIENT VALUES (20, 'James', 'Perez', '1987-08-20', 'M', '012-345-6780', 'jamesperez@example.com', '456 Cedar Street', 'Northeasttown', 'Northeaststate', '01234', 'Jamie Perez', '098-765-4320', CURRENT_TIMESTAMP)",
]

# Execute each insert query
for query in insert_queries:
    cursor.execute(query)

# Commit the changes to the database
connection.commit()

# Display all records
print("The inserted records are")
data = cursor.execute('''SELECT * FROM PATIENT''')
for row in data:
    print(row)

# Close the connection
connection.close()


