import tkinter as tk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import re


def fetch_manager_data_from_db():
    """
        A function that fetches
        sales info data
    """
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


def validate_email(email):
    """
        a function that validates the email
        of a walmart manager
    """
    pat = "^[a-zA-Z]+[.]+[a-zA-Z]+@Walmart.org$"
    if re.match(pat, email):
        return True
    return False


def manager_form():

    """
        A function that displays the form
        for editting a manager details
    """

    def populate():
        """
            A function that populates
            the manager form
        """
        con = mysql.connect(
            host="localhost", 
            user="root", 
            password="",
            database="walmart"
        )

        row_id = id_entry.get();
        #   create db connection
        cur = con.cursor()
        #   pull data from database
        if row_id == "":
            MessageBox.showinfo("Form Error","You must enter ID")
        else:
            try:
                cur.execute("SELECT * FROM store_info WHERE id=%s", [row_id])
                store_result = cur.fetchone()
                con.close()

                store_entry.insert(0, store_result[1])
                name_entry.insert(0, store_result[2])
                year_entry.insert(0, store_result[3])
                email_entry.insert(0, store_result[4])
                address_entry.insert(0, store_result[5])
                city_entry.insert(0, store_result[6])
                state_entry.insert(0, store_result[7])
                zip_entry.insert(0, store_result[8])
            except Exception as e:
                print(e)
                MessageBox.showinfo("Invalid ID","Enter a valid ID")


    def update():
        """
            A function that updates a 
            manager record
        """
        con = mysql.connect(
            host="localhost", 
            user="root", 
            password="",
            database="walmart"
        )
        #   get fields
        row_id = id_entry.get()
        store = store_entry.get()
        name = name_entry.get()
        year = year_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        city = city_entry.get()
        state = state_entry.get()
        zip_code = zip_entry.get()

        if store == "" or name == "" or year == "" or email == "" or address == "" or city == "" or state == "" or zip_code == "":
            MessageBox.showinfo("Form Error","All fields must be filled before updating")

        #   update if email is valid
        if validate_email(email) == True:
            #   create db connection
            cur = con.cursor()
            cur.execute("UPDATE store_info SET store=%s, manager=%s, year_as_manager=%s, email=%s, address=%s, city=%s, state=%s, zip_code=%s WHERE id = %s", (store, name, year, email, address, city, state, zip_code, int(row_id)))
            con.commit()
            con.close()

            #   clear form
            id_entry.delete(0, 'end')
            store_entry.delete(0, 'end')
            name_entry.delete(0, 'end')
            year_entry.delete(0, 'end')
            email_entry.delete(0, 'end')
            address_entry.delete(0, 'end')
            city_entry.delete(0, 'end')
            state_entry.delete(0, 'end')
            zip_entry.delete(0, 'end')

            #   reload list box
            result = fetch_manager_data_from_db()
            show(result) 
            MessageBox.showinfo("Success","Record updated successfully")
        else:
            MessageBox.showinfo("Form Error","Email is invalid, use appropriate format")

    label_bg = "white"

    #   labels
    note_info = """
                    Note: To populate the form with a manager details enter 
                    record ID and click on populate button
                """
    note= tk.Label(frame2, text=note_info, font=('bold', 7), background=label_bg, fg="red")
    note.place(x=0, y=0)

    row_id= tk.Label(frame2, text="ID", font=('bold', 10), background=label_bg)
    row_id.place(x=20, y=40)

    store= tk.Label(frame2, text="Store ID", font=('bold', 10), background=label_bg)
    store.place(x=20, y=70)

    name = tk.Label(frame2, text="Name:", font=('bold', 10), background=label_bg)
    name.place(x=20, y=100)

    year = tk.Label(frame2, text="Year As Manager:", font=('bold', 10), background=label_bg)
    year.place(x=20, y=130)

    email = tk.Label(frame2, text="Email:", font=('bold', 10), background=label_bg)
    email.place(x=20, y=160)
    email_helper = tk.Label(frame2, text="(eg: xxx.yyy@Walmart.org)", font=('small', 8), background=label_bg)
    email_helper.place(x=20, y=185)

    address = tk.Label(frame2, text="Store Address:", font=('bold', 10), background=label_bg)
    address.place(x=20, y=210)

    city = tk.Label(frame2, text="City:", font=('bold', 10), background=label_bg)
    city.place(x=20, y=240)

    state = tk.Label(frame2, text="State:", font=('bold', 10), background=label_bg)
    state.place(x=20, y=270)

    zip_code = tk.Label(frame2, text="Zip Code:", font=('bold', 10), background=label_bg)
    zip_code.place(x=20, y=300)

    #   inputs
    id_entry = tk.Entry()
    id_entry.place(x=200, y=40)

    store_entry = tk.Entry()
    store_entry.place(x=200, y=70)

    name_entry = tk.Entry()
    name_entry.place(x=200, y=100)

    year_entry = tk.Entry()
    year_entry.place(x=200, y=130)

    email_entry = tk.Entry()
    email_entry.place(x=200, y=160)

    address_entry = tk.Entry()
    address_entry.place(x=200, y=210)

    city_entry = tk.Entry()
    city_entry.place(x=200, y=240)

    state_entry = tk.Entry()
    state_entry.place(x=200, y=270)

    zip_entry = tk.Entry()
    zip_entry.place(x=200, y=300)

    result = fetch_manager_data_from_db()
    show(result)

    #   populate button
    tk.Button(
            frame2,
            text="Get",
            font=("TkHeadingFont", 12),
            bg=bg,
            activebackground="#ffffff",
            activeforeground="#000000",
            cursor="hand1",
            command=lambda:populate()
        ).place(x=20, y=350)

    #   populate button
    tk.Button(
            frame2,
            text="Update",
            font=("TkHeadingFont", 12),
            bg="white",
            activebackground=bg,
            activeforeground="black",
            cursor="hand1",
            command=lambda:update()
        ).place(x=100, y=350)

    # 'back' button widget
    tk.Button(
		frame2,
		text="Back",
		font=("TkHeadingFont", 12),
		bg="black",
		fg="white",
		cursor="hand2",
		activebackground=bg,
		activeforeground="black",
		command=lambda:load_frame_1()
		).place(x=200, y=350)


def clear_widgets(frame):
    """
        A function that selects all frame widgets and delete them
    """
    for widget in frame.winfo_children():
	    widget.destroy()


def load_manager_frame():
    """
        A function that contains manager frame widgets
    """
    clear_widgets(frame1)
    frame2.tkraise()
    # result = fetch_manager_data_from_db()

    #   manager form
    manager_form()



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
    

def show(result):
    # create list box for all managers
    list_box= tk.Listbox(frame2, width=int(x/2), height=30, bg=bg, font=('normal', 8))
    list_box.place(x=400, y=10)
    #   fetch each record
    for item in result:
        data =  f"id: {item[0]} |   store: {item[1]} |   manager: {item[2]} |   email:{item[4]} |    address: {item[5]} |   city: {item[6]} |   state: {item[7]} |    zip:{item[8]}"
        list_box.insert(list_box.size()+1, data)

load_frame_1()

#   run app
root.mainloop()