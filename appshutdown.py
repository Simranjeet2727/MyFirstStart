from tkinter import *
import os

def restart():
    os.system("sudo shutdown -r now")

def restart_time():
    os.system("sudo shutdown -r +20")

def logout():
    os.system("sudo pkill -KILL -u $USER")

def shutdown():
    os.system("sudo shutdown -h now")

# Creating the Tkinter window
st = Tk()
st.title("ShutDown App")
st.geometry("500x600")
st.config(bg="green")

# Creating buttons for different actions
restart_button = Button(st, text="Restart", font=("Times New Roman", 15, "bold"), relief=RAISED, cursor="plus", command=restart)
restart_button.place(x=10, y=10, height=20, width=110)

restart_time_button = Button(st, text="Restart Time", font=("Times New Roman",15, "bold"), relief=RAISED, cursor="plus", command=restart_time)
restart_time_button.place(x=10, y=50, height=20, width=110)

logout_button = Button(st, text="LogOut", font=("Times New Roman", 15, "bold"), relief=RAISED, cursor="plus", command=logout)
logout_button.place(x=10, y=90, height=20, width=110)

shutdown_button = Button(st, text="ShutDown", font=("Times New Roman", 15, "bold"), relief=RAISED, cursor="plus", command=shutdown)
shutdown_button.place(x=10, y=130, height=20, width=110)

st.mainloop()  # Running the Tkinter event loop to display the window and handle user interactions
