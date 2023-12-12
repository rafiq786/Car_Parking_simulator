#import functions from function car parking
from car_parking import CarParkingSimulator

#created a instance for carparking simulator 
carpark = CarParkingSimulator()

#option to select from the given menu
while True:
    print("\n Menu: ")
    print("1: Entry to Car Parking(Hour Rate 2£)")#entry to car park
    print("2: Query for Car Number by using the Ticket number")#search by ticket number for information of data
    print("3: View the Remaining Parking Spaces")#Remaining Parking spaces for car parking
    print("4: Exit From Car Parking Space")#to exit from car park
    print("5: Quit the Program and save the Data ")#to quit program & save file in data

    #Created a input to select from the menu
    option = input("Please Enter Your Option From the Menu: ")

    #Option to enter the Car park
    if option == '1':
        booking_name = input("Enter a Booking Name of Car: ")#Created  input for a booking name of car
        #using try and exception error handling
        try:
            #Assigning value to the enter car park function
            entry_time, parking_space, ticket_number = carpark.enter_car_park(booking_name)
            print(f"Car Booking Name: {booking_name}")
            print(f"Entry Time of Car: {entry_time}")
            print(f"Space Assigned for Car: {parking_space}")
            print(f'Total Avaliable Spaces: {carpark.avaliable_spaces}')
            print(f'Ticket Number: {ticket_number}')
        except:
            print(carpark.enter_car_park(booking_name))
       
    #option to search car info by ticket number
    elif option == '2':
        ticket_number = input("Enter a Ticket Number of Car: ")#Created input for searching car info of car by ticket_num
        #Assigning value to find information by ticket number & unpacking the values
        [*parking_space, registration_number,entry_time,exit_time,fees, ticket_num] = carpark.search_by_tick_number(ticket_number)
        print(f"Car Booking Name: {registration_number}")
        print(f"Entry Time of Car: {entry_time}")
        print(f"Space Assigned for Car: {parking_space}")
        print(f'Total Avaliable Spaces: {carpark.avaliable_spaces}')
        print(f'Ticket Number: {ticket_number}')
        print(f'Exit Time: {exit_time}')
        print(f'Parking Fees : {fees}')

    #to see toal avaliable spaces for car parking
    elif option == '3':
        print(f'Total Avaliable Spaces: {carpark.avaliable_spaces}')#total parking spaces for remaining parking cars

    #option to exit the car from parking space
    elif option == '4':
        try:
            booking_name = input("Enter a Booking Name of Car: ")#Created input to booking number assigned to car for exiting
            #Assigning values to exit from the car park
            exit_time, parking_space, fees = carpark.exit_car_park(booking_name)
            print(f"Car Booking Name: {booking_name}")
            print(f"Exit Time of Car: {exit_time}")
            print(f"Space Assigned for Car: {parking_space}")
            print(f'Total Avaliable Spaces: {carpark.avaliable_spaces}')
            print(f'Fees: {fees}')
        except:
            print(carpark.exit_car_park(booking_name))    
    
    #to quit program and save the park record in the csv file after quitting the program
    elif option == '5':
        carpark.saving_parking_record()
        print("Your Data is being Saved Successfully!!! Have a Great day ahead:)")
        break

    else:
        #If there is any invalid choice other than given menu
        print("Invalid Choice Please Select from the Menu")