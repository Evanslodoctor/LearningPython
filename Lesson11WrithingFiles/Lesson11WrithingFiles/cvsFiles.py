import csv

# Creating a CSV file
def create_csv():
    data = [
        ['Name', 'Age', 'City'],
        ['Alice', 25, 'New York'],
        ['Bob', 30, 'San Francisco'],
        ['Charlie', 22, 'Los Angeles']
    ]

    with open('example.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)

    print("CSV file created successfully.")

# Reading from a CSV file
def read_csv():
    with open('example.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)

# Writing to a CSV file
def write_csv():
    new_data = [
        ['David', 28, 'Chicago'],
        ['Eve', 35, 'Seattle']
    ]

    with open('example.csv', 'a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(new_data)

    print("Data written to CSV file.")

# Main function
if __name__ == "__main__":
    # Create CSV file
    create_csv()

    # Read from CSV file
    print("\nReading from CSV file:")
    read_csv()

    # Write to CSV file
    print("\nWriting to CSV file:")
    write_csv()
