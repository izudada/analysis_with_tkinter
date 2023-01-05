import tkinter as tk
import mysql.connector as mysql


def manager_form():

    """
        A function that displays the form
        for editting a manager details
    """
    bg = "white"

    #   labels
    store= tk.Label(frame2, text="Store ID", font=('bold', 10), background=bg)
    store.place(x=20, y=10)

    name = tk.Label(frame2, text="Name", font=('bold', 10), background=bg)
    name.place(x=20, y=40)

    year = tk.Label(frame2, text="Year As Manager", font=('bold', 10), background=bg)
    year.place(x=20, y=70)

    email = tk.Label(frame2, text="Email (xxx.yyy@Walmart.org)", font=('bold', 10), background=bg)
    email.place(x=20, y=100)

    address = tk.Label(frame2, text="Store Address", font=('bold', 10), background=bg)
    address.place(x=20, y=130)

    city = tk.Label(frame2, text="City", font=('bold', 10), background=bg)
    city.place(x=20, y=160)

    state = tk.Label(frame2, text="State", font=('bold', 10), background=bg)
    state.place(x=20, y=190)

    zip = tk.Label(frame2, text="Zip Code", font=('bold', 10), background=bg)
    zip.place(x=20, y=220)

    #   inputs
    store_entry = tk.Entry()
    store_entry.place(x=100, y=10)

    name_entry = tk.Entry()
    name_entry.place(x=100, y=40)

    year_entry = tk.Entry()
    year_entry.place(x=100, y=70)

    email_entry = tk.Entry()
    email_entry.place(x=100, y=100)

    address_entry = tk.Entry()
    address_entry.place(x=100, y=130)

    city_entry = tk.Entry()
    city_entry.place(x=100, y=160)

    state_entry = tk.Entry()
    state_entry.place(x=100, y=190)

    zip_entry = tk.Entry()
    zip_entry.place(x=100, y=40)


def clear_widgets(frame):
    """
        A function that selects all frame widgets and delete them
    """
    for widget in frame.winfo_children():
	    widget.destroy()

def fetch_manager_data_from_db():
    """
        A function that fetches
        sales info data
    """
    #   database connection
    con = mysql.connect(
            host="localhost", 
            user="root", 
            password="",
            database="walmart"
        )

    #   create db connection
    cursor = con.cursor()
    #   pull data from database
    cursor.execute("select * from store_info")
    result = cursor.fetchall()
    con.close()
    return result

def load_manager_frame():
    """
        A function that contains manager frame widgets
    """
    clear_widgets(frame1)
    frame2.tkraise()
    result = fetch_manager_data_from_db()

    #   manager form
    manager_form()
    # create list box for all managers
    list_box= tk.Listbox(frame2, width=int(x/2), height=int(y/2), bg=bg)
    list_box.place(x=20, y=250)
    #   fetch each record
    for item in result:
        data =  f"store: {item[1]} |   manager: {item[2]} |   email:{item[4]} |    address: {item[5]} |   city: {item[6]} |   state: {item[7]} |    zip:{item[8]}"
        list_box.insert(list_box.size()+1, data)


def load_frame_1():
    """
        A function that contains frame 1 widgets
    """
    clear_widgets(frame2)
	# stack frame 1 above frame 2
    frame1.tkraise()
    frame1.pack_propagate(False)

    #   view managers button
    tk.Button(
            frame1,
            text="View Managers",
            font=("TkHeadingFont", 16),
            bg=bg,
            activebackground="#000000",
            activeforeground=bg,
            cursor="hand1",
            command=lambda:load_manager_frame()
        ).pack(pady=50)

#   initialize app
root = tk.Tk()

#   base window title
root.title("Walmart Database GUI")

#   bacgroung color
bg = "#ebc934"

# Centers the root window/screen
x = root.winfo_screenwidth()    
y = root.winfo_screenheight()

frame1 = tk.Frame(root, width=x, height=y, bg=bg)
frame2 = tk.Frame(root, width=x, height=y, bg="white")

for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky="nesw")

load_frame_1()

#   run app
root.mainloop()