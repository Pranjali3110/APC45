import tkinter as tk
from tkinter import ttk, messagebox


def submit():
    name = name_entry.get()
    mobile = mobile_entry.get()
    email = email_entry.get()
    college = college_entry.get()
    branch = branch_entry.get()

    if name == "" or mobile == "" or email == "" or college == "" or branch == "":
        messagebox.showwarning("Warning", "Please fill all fields")
        return

    # Save data in text file
    with open("student.txt", "a") as file:
        file.write(name + "," + mobile + "," + email + "," +
                   college + "," + branch + "\n")

    messagebox.showinfo("Success", "Record saved successfully")

    # Clear
    name_entry.delete(0, tk.END)
    mobile_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    college_entry.delete(0, tk.END)
    branch_entry.delete(0, tk.END)


def read_data():
    window = tk.Toplevel(app)
    window.title("Student Records")
    window.geometry("900x400")

    columns = ("Name", "Mobile No", "Email ID", "College Name", "Branch")

    table = ttk.Treeview(
        window,
        columns=columns,
        show="headings"
    )

    for column in columns:
        table.heading(column, text=column)
        table.column(column, width=170)

    table.pack(fill="both", expand=True)

    try:
        with open("student.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")

                if len(data) == 5:
                    table.insert("", tk.END, values=data)

    except FileNotFoundError:
        messagebox.showinfo("Information", "No records found")


# Application
app = tk.Tk()
app.title("Student Application")
app.geometry("500x450")

tk.Label(
    app,
    text="Student Application",
    font=("Arial", 20, "bold")
).pack(pady=20)


frame = tk.Frame(app)
frame.pack()


# Name
tk.Label(frame, text="Name").grid(row=0, column=0, padx=10, pady=8)
name_entry = tk.Entry(frame, width=30)
name_entry.grid(row=0, column=1)


# Mobile
tk.Label(frame, text="Mobile No").grid(row=1, column=0, padx=10, pady=8)
mobile_entry = tk.Entry(frame, width=30)
mobile_entry.grid(row=1, column=1)


# Email
tk.Label(frame, text="Email ID").grid(row=2, column=0, padx=10, pady=8)
email_entry = tk.Entry(frame, width=30)
email_entry.grid(row=2, column=1)


# College
tk.Label(frame, text="College Name").grid(row=3, column=0, padx=10, pady=8)
college_entry = tk.Entry(frame, width=30)
college_entry.grid(row=3, column=1)


# Branch
tk.Label(frame, text="Branch").grid(row=4, column=0, padx=10, pady=8)
branch_entry = tk.Entry(frame, width=30)
branch_entry.grid(row=4, column=1)


# Submit Button
tk.Button(
    app,
    text="Submit",
    command=submit,
    width=15
).pack(pady=15)


# Read Button
tk.Button(
    app,
    text="Read",
    command=read_data,
    width=15
).pack()


app.mainloop()