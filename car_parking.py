#Importing different Modules
from datetime import datetime
import os 
import csv
from math import ceil
from uuid import uuid4

#Creatig Carparkingsimulator class for handling the function
class CarParkingSimulator:
    def __init__(self):
        #To store car information
        self.park_information = []
        self.ticket_num = None
        #To create parking instance and spaces for parking
        self.parking_spaces = list(range(1,20))
        self.avaliable_spaces = 20
        #File Location of csv 
        self.file_location = "parking_records.csv"
        self.loading_parking_record()

    #created function for loading the parking information in the csv file
    def loading_parking_record(self):
        #using try and exception error handling
        try:    
            if not os.path.isfile(self.file_location):
              with open(self.file_location,'w',newline='') as new_file:
                  write = csv.writer(new_file)
                  write.writerow(["parking_space", "Car_name", "Entry_time", "Exit_time","parking_fees","Ticket_number"]) 
            else:
                #If file is present this will open and read the file 
                with open(self.file_location,'r') as file:
                    read = csv.reader(file)
                    for row in read:
                        self.park_information.append(row)
                        if row[3] == '':
                            self.parking_spaces.remove(int(row[0]))
                            self.avaliable_spaces -=1
        #if File not found This error will be printed                  
        except FileNotFoundError:
            print(f"File '{self.file_location}' is being not Found. Creating new file")

    #saving the records in the file location and writing in the file
    def saving_parking_record(self):
        #used try and exception error handling
        try:
            with open(self.file_location, 'w', newline='\n') as file:
                write = csv.writer(file)    
                for data in self.park_information:
                    write.writerow(data)
        #if not able to save file it will print this            
        except Exception as e:
            print(f"Error saving the record to file:{e}")

    #Created function if the same number of car registeration number is been entered
    def same_booking(self, registration_number):
        for data in self.park_information:
            if len(data)>1 and data[1].lower() == registration_number.lower() and data[3]=='':
                return True
        return False
    #function to create instance to enter car in parking space    
    def enter_car_park(self, registration_number):
        #using try and exception error handling
        try:
            if self.same_booking(registration_number):
                return (f"Vehicle, with Registration Number: '{registration_number}' is being already parked in parking space.") 
                # return None, None
            elif self.avaliable_spaces == 0:
                return 'The Parking Space is Full'
                # return 0
            #entry time of the car in parking space
            entry_time = datetime.now().strftime("Dt: %m:%d:%y:%Y Time: %H:%M:%S")
            #created to use random ticket number and slicing is being used in this
            self.ticket_num = str(uuid4())[-8:]
            parking_space = None
            #for loop used to see the parking space avaliable 
            for i in range(1,51):
                if i in self.parking_spaces:
                    parking_space = str(i)
                    self.parking_spaces.remove(i)
                    break
            #used to append the information in the csv file    
            self.park_information.append([parking_space, registration_number,entry_time,None,None, self.ticket_num])
            #if any car is been parked it will reduce the parking space  
            self.avaliable_spaces -=1 
            #to return entry time,parking space & ticket number for car
            return (entry_time,parking_space,self.ticket_num)
        except Exception as e:
            #if not able to park the car in parking space it will print this
            print(f"Error while parking car: {e}")
            return None, None, None,None

    #function to create instance to exit car in parking space
    def exit_car_park(self, registration_number):
        #using try and exception error handling
        try:
            #To check data in parking information 
            for data in self.park_information:
                if len(data)>1 and data[1] == registration_number:
                    #exit time of the car in parking space
                    exit_time = datetime.now().strftime("Dt: %m:%d:%y:%Y Time: %H:%M:%S")
                    #assigning parking space for getting data from csv file
                    parking_space = data[0]
                    #assigning exit time for getting data from csv file
                    data[3] = exit_time
                    #To add parking space in the parking information
                    self.parking_spaces.append(parking_space)
                    #if car exited from car park then the parking space will be incremented
                    self.avaliable_spaces +=1
                    #Calculating difference between enter time & exit time
                    fees =  ceil((datetime.strptime(exit_time,"Dt: %m:%d:%y:%Y Time: %H:%M:%S")  - datetime.strptime(data[2],"Dt: %m:%d:%y:%Y Time: %H:%M:%S")).total_seconds() / 3600) *2
                    #Assigning fees in the csv file
                    data[4] = fees
                    return (exit_time, parking_space, fees)
            return None,None,None    
        #if not able to exit the car in parking space it will print this        
        except Exception as e:
            print(f"Error while exiting car: {e}")
            return None, None, None

    #created function instance to search data of particular with the ticket number
    def search_by_tick_number(self, ticket_number):
        #using try and exception error handling
        try:
            #to see if data is being present in parking information
            for data in self.park_information:
                if data[5] == ticket_number:
                    return data
        #if not able to exit the car in parking space it will print this
        except Exception as e:
            print(f"Error while searching by ticket number: {e}")


    