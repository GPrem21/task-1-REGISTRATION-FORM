import tkinter as tk
from tkinter import messagebox, ttk

# Function to be called when the "Submit" button is clicked
def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    age = entry_age.get()
    gender = gender_var.get()
    phone = entry_phone.get()
    address = entry_address.get()
    course = course_var.get()

    if name and email and age and gender and phone and address and course:
        try:
            age = int(age)
            phone = int(phone)
            messagebox.showinfo("Registration", f"Name: {name}\nEmail: {email}\nAge: {age}\nGender: {gender}\n"
                                                f"Phone: {phone}\nAddress: {address}\nCourse: {course}\n"
                                                "Registration Successful!")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid age and phone number.")
    else:
        messagebox.showerror("Error", "Please fill all the fields.")

# Setting up the main window
root = tk.Tk()
root.title("Registration Form")
root.attributes('-fullscreen', True)
root.configure(bg="#34495e")

# Creating a frame to center the form
frame = tk.Frame(root, bg="#34495e")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Creating and placing the labels and entry fields
font_style = ("Helvetica", 14)
label_color = "#ecf0f1"
entry_bg = "#ecf0f1"
entry_fg = "#2c3e50"

tk.Label(frame, text="Name:", bg="#34495e", fg=label_color, font=font_style).grid(row=0, column=0, padx=20, pady=15, sticky="e")
entry_name = tk.Entry(frame, font=font_style, width=30, bg=entry_bg, fg=entry_fg)
entry_name.grid(row=0, column=1, padx=20, pady=15)

tk.Label(frame, text="Email:", bg="#34495e", fg=label_color, font=font_style).grid(row=1, column=0, padx=20, pady=15, sticky="e")
entry_email = tk.Entry(frame, font=font_style, width=30, bg=entry_bg, fg=entry_fg)
entry_email.grid(row=1, column=1, padx=20, pady=15)

tk.Label(frame, text="Age:", bg="#34495e", fg=label_color, font=font_style).grid(row=2, column=0, padx=20, pady=15, sticky="e")
entry_age = tk.Entry(frame, font=font_style, width=30, bg=entry_bg, fg=entry_fg)
entry_age.grid(row=2, column=1, padx=20, pady=15)

tk.Label(frame, text="Gender:", bg="#34495e", fg=label_color, font=font_style).grid(row=3, column=0, padx=20, pady=15, sticky="e")
gender_var = tk.StringVar(value="Select")
gender_dropdown = ttk.Combobox(frame, textvariable=gender_var, font=font_style, width=28, state="readonly")
gender_dropdown['values'] = ("Male", "Female", "Other")
gender_dropdown.grid(row=3, column=1, padx=20, pady=15)

tk.Label(frame, text="Phone Number:", bg="#34495e", fg=label_color, font=font_style).grid(row=4, column=0, padx=20, pady=15, sticky="e")
entry_phone = tk.Entry(frame, font=font_style, width=30, bg=entry_bg, fg=entry_fg)
entry_phone.grid(row=4, column=1, padx=20, pady=15)

tk.Label(frame, text="Address:", bg="#34495e", fg=label_color, font=font_style).grid(row=5, column=0, padx=20, pady=15, sticky="e")
entry_address = tk.Entry(frame, font=font_style, width=30, bg=entry_bg, fg=entry_fg)
entry_address.grid(row=5, column=1, padx=20, pady=15)

tk.Label(frame, text="Course:", bg="#34495e", fg=label_color, font=font_style).grid(row=6, column=0, padx=20, pady=15, sticky="e")
course_var = tk.StringVar(value="Select")
course_dropdown = ttk.Combobox(frame, textvariable=course_var, font=font_style, width=28, state="readonly")
course_dropdown['values'] = ("Computer Science", "Information Technology", "Electronics", "Mechanical", "Civil")
course_dropdown.grid(row=6, column=1, padx=20, pady=15)

# Creating and placing the submit button
submit_button = tk.Button(frame, text="Submit", command=submit_form, font=font_style, bg="#2980b9", fg="white", width=15)
submit_button.grid(row=7, column=1, pady=40)

# Running the main event loop
root.mainloop()
