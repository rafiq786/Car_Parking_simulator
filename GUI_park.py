#import TKinter module to create GUI
import tkinter as tk
#importing class carparkingsimulator
from car_parking import CarParkingSimulator
#Importing module simpledialog
from tkinter import simpledialog

#creating instance for carparkingsimulator
car_simulator = CarParkingSimulator()


def enter_car_park():
    try:
    #Creating a dialog box for user to enter users Car Number
        booking_name = simpledialog.askstring("Enter Registration Number","Enter Registration Number")
        if booking_name is not None:
            if car_simulator.same_booking(booking_name):
                label.config(text=f"Vehicle with Registration Number: '{booking_name}' is already parked.")
            else:
                entry_time,parking_space,ticket_number = car_simulator.enter_car_park(booking_name)
                if entry_time:
                    label.config(text=
                                f"Registeration Number:{booking_name}\nTicket Number {ticket_number}  is being parked in parking.\n"
                                f"Entry Time of Car in parking: {entry_time}.\n"
                                f"Parking Space Assigned to Car: {parking_space}")
        else:
            label.config(text="Error While Parking the Car in Parking Space!!!.")  
    except:
        # print(car_simulator.enter_car_park(booking_name))
        pass

def search_by_ticket_number():
    #Creating a dialog box for user to Ticket Number Provided to Car
    ticket_number = simpledialog.askstring("Enter Ticket Number", "Please Enter a Ticket Number")
    if ticket_number is not None:
        data= car_simulator.search_by_tick_number(ticket_number)
        if data:
            if data[4]:  
                parking_fee = float(data[4])  
                label.config(text="Ticket Number for Car: "+ str(ticket_number)+"\n"
                                      "Car Number of Car: "+ str(data[1])+"\n"
                                      "Enter_time of Car: "+ str(data[2])+"\n"
                                      "Parking Space For Car:"+ str(data[0])+"\n"
                                      "Parking Fees for car: £{:.2f}".format(parking_fee)+"\n"
                                      "Exit_time of Car: "+ str(data[3]))
            else:
                label.config(text="Car with ticket: " + str(ticket_number) + " has not exited.\n"
                                  "Entry Time: " + data[2] + "\n"
                                  "Parking Space: " + data[0] + "\n")    
        else:
            label.config(text="Ticket Number you Provided is being Not in Parking Space!!!.") 

def avaliable_spaces():
    label.config(text=f"Avaliable Spaces for Car parking: {car_simulator.avaliable_spaces}")            

def exit_car_park():
    #Creating a dialog box for user to enter users Car Number          
    booking_name = simpledialog.askstring("Enter Booking Number","Please Enter a Car Number:")
    if booking_name is not None:
        booking_name = booking_name
        exit_time,parking_space,fee = car_simulator.exit_car_park(booking_name)
        if exit_time:
            label.config(text=  f"Car Name:{booking_name} Exited.\n Parking Space: {parking_space} is Vaccant Now!!!\n"
                                f"Parking Fees For Parking Car: £{fee:.2f}\n"
                                f"Exit Time From Car Parking: {exit_time}")
        else:
            label.config(text= "Error While Exiting from the Car Parking Space!!!.")    

def quit():
    label.config(text="Your Data is being Saved Successfully!!! Have a Great day ahead:)")
    car_simulator.saving_parking_record()
    root.quit()

def close():
    #If you close the tab then the records will be save in the csv file
    car_simulator.saving_parking_record()
    root.destroy()    


root = tk.Tk()
root.geometry('1200x600')
root.title("Car Parking Simulator")
root.configure(bg="black")

heading = tk.Label(root,text="Welcome to Car Parking Simulator", font=('Times New Roman', 25, 'bold'), bg="blue",fg="white")



#Creating Button and Configure Them 

Entry_Button = tk.Button(root,text="Enter_The_CarPark", command=enter_car_park,fg="white", bg="blue",height=3,width=18,font=('Times New Roman', 12, 'bold'))
Query_ticket_num = tk.Button(root,text="Query_By_Ticket Number", command=search_by_ticket_number,fg="white",bg="blue",height=3,width=19,font=('Times New Roman', 12, 'bold'))
Spaces = tk.Button(root,text="View_Avaliable-Spaces", command=avaliable_spaces,bg="blue",fg="white",height=3,width=18,font=('Times New Roman', 12, 'bold'))
Exit_CarPark= tk.Button(root,text="Exit_Car_Parking",fg="white", command=exit_car_park,bg="blue",height=3,width=18,font=('Times New Roman', 12, 'bold'))
Quit = tk.Button(root,text="Quit_Car_Park",command=quit,bg="blue",fg="white",height=3,width=18,font=('Times New Roman', 12, 'bold'))
label = tk.Label(root,text="",bg="blue",fg="white",font=('Times New Roman', 15, 'bold'))

# Place GUI elements on the grid
Entry_Button.grid(row=0, column=0)
Query_ticket_num.grid(row=0, column=1)
Spaces.grid(row=0, column=2)
Exit_CarPark.grid(row=0, column=3)
Quit.grid(row=0, column=4)
label.grid(row=1, column=0, columnspan=5)
heading.grid(row=0,column=3)

#place the button according to the position we require
Spaces.place(x=60,y=450)
Query_ticket_num.place(x=1000,y=150)
Exit_CarPark.place(x=1000, y=450)
Quit.place(x=510, y= 450)
label.place(x=350,y=260)
Entry_Button.place(x=70,y=150)
heading.place(x=380, y=50)

#Close the window and the records will be saved in the csv file 
root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()            