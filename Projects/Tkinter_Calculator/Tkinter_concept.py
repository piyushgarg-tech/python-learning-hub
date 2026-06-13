import tkinter as tk
from tkinter import ttk
import tkinter.font as tfont

# ==================================================
# Tkinter Revision Playground
# Single Window + Single mainloop()
# Uses only pack()
# Covers:
# Label, Button, Entry, ttk, Frames,
# Text, Separator
# ==================================================

window = tk.Tk()
window.title("Tkinter Revision Playground")
window.geometry("1000x700")                                                  # minsize(1000,700) -- only sets the minimum size.                                                                            
window.resizable(True, True)                                                # geometry("1000x700") -- sets the actual starting size.

# --------------------------------------------------
# Output Area Function
# --------------------------------------------------
def show_output(message):
    output_label.config(text=message)
    print(message)

# --------------------------------------------------
# Title Section
# --------------------------------------------------
title_font = tfont.Font(
    family="Times New Roman",
    size=18,
    slant="italic"
)

title = tk.Label(
    window,
    text="Tkinter Revision Playground",
    font=title_font
)
title.pack(pady=10)

# ==================================================
# 1. Label Demo
# ==================================================
label_frame = ttk.LabelFrame(window, text="1. Label Demo", padding=10)          #padding → space inside the frame
label_frame.pack(fill="x", padx=10, pady=5)                                        #padx/pady → space outside the frame                                  

demo_label = tk.Label(
    label_frame,
    text="I'm gonna be The King of the Pirates"
)
demo_label.pack()

# ==================================================
# 2. Button Demo
# ==================================================
button_frame = ttk.LabelFrame(window, text="2. Button Demo", padding=10)
button_frame.pack(fill="x", padx=10, pady=5)

counter = 0

def button_click():
    global counter
    counter += 1
    show_output(f"Button clicked {counter} times")

ttk.Button(
    button_frame,
    text="Click Me",
    command=button_click
).pack()

# ==================================================
# 3. Entry Demo
# ==================================================
entry_frame = ttk.LabelFrame(window, text="3. Entry Demo", padding=10)
entry_frame.pack(fill="x", padx=10, pady=5)

ttk.Label(entry_frame, text="Username").pack()

username_entry = ttk.Entry(entry_frame, width=30)
username_entry.pack()

ttk.Label(entry_frame, text="Password").pack()

password_entry = ttk.Entry(
    entry_frame,
    width=30,
    show="*"
)
password_entry.pack()

def get_username():
    show_output(f"Username: {username_entry.get()}")

ttk.Button(
    entry_frame,
    text="Submit",
    command=get_username
).pack(pady=5)

# ==================================================
# 4. ttk Demo
# ==================================================
ttk_frame = ttk.LabelFrame(window, text="4. ttk Widgets", padding=10)
ttk_frame.pack(fill="x", padx=10, pady=5)

ttk.Label(ttk_frame, text="This is a ttk.Label").pack()

# ==================================================
# 5. Frame + Background Colors
# ==================================================
color_frame = ttk.LabelFrame(window, text="5. Frames & Colors", padding=10)
color_frame.pack(fill="x", padx=10, pady=5)

tk.Label(color_frame, text="Line 1", bg="red").pack(side="left", padx=5)
tk.Label(color_frame, text="Line 2", bg="green").pack(side="left", padx=5)
tk.Label(color_frame, text="Line 3", bg="yellow").pack(side="left", padx=5)

# ==================================================
# 6. Text Widget + Separator + Padding
# ==================================================
text_frame = ttk.LabelFrame(window, text="6. Text Widget", padding=10)
text_frame.pack(fill="x", padx=10, pady=5)

text_box = tk.Text(text_frame, height=4, width=40)
text_box.pack()
text_box.insert("1.0", "Enter your comments")

def enable_text():
    text_box["state"] = "normal"
    show_output("Text box enabled")

def get_text():
    show_output(text_box.get("1.0", "end").strip())

ttk.Button(
    text_frame,
    text="Enable Text Box",
    command=enable_text
).pack(pady=5)

ttk.Button(
    text_frame,
    text="Get Text",
    command=get_text
).pack()

ttk.Separator(window, orient="horizontal").pack(
    fill="x",
    padx=10,
    pady=10
)

# ==================================================
# Output Area
# ==================================================
output_label = ttk.Label(
    window,
    text="Output will appear here",
    padding=10
)
output_label.pack(fill="x", padx=10, pady=10)

window.mainloop()






# Imports
import tkinter as tk
from tkinter import ttk
import tkinter.font as tfont


# ==================================================
# Tkinter Revision Playground
# Single Window + Single mainloop()
# Uses only pack()
# Covers:
# Separator, Checkbutton, Radiobutton,
# Combobox, Listbox, Spinbox, Variables, Events
# ==================================================

# Window
window = tk.Tk()
window.title("Tkinter Interactive Widgets Playground")
window.geometry("900x700")
window.resizable(True, True)

# --------------------------------------------------
# Output Area Function
# --------------------------------------------------
def show_output(message):
    output_label.config(text=message)
    print(message)

# --------------------------------------------------
# Title Section
# --------------------------------------------------
title_font = tfont.Font(
    family="Times New Roman",
    size=18,
    slant="italic"
)

title = tk.Label(
    window,
    text="Tkinter Interactive Widgets Playground",
    font=title_font
)
title.pack(pady=10)

# ==================================================
# 7. Checkbutton
# ==================================================
check_frame = ttk.LabelFrame(window, text="7. Checkbutton", padding=10)
check_frame.pack(fill="x", padx=10, pady=5)

# StringVar stores text values
check_var = tk.StringVar(value="no")

def check_task():
    show_output(f"Terms Accepted: {check_var.get()}")

ttk.Checkbutton(
    check_frame,
    text="Agree with Terms and Conditions",
    variable=check_var,
    onvalue="yes",
    offvalue="no",
    command=check_task
).pack()

# ==================================================
# 8. Radiobutton
# ==================================================
radio_frame = ttk.LabelFrame(window, text="8. Radiobutton", padding=10)
radio_frame.pack(fill="x", padx=10, pady=5)

gender_var = tk.StringVar()

def radio_task():
    show_output(f"Selected Gender: {gender_var.get()}")

ttk.Radiobutton(
    radio_frame,
    text="Male",
    variable=gender_var,
    value="Male",
    command=radio_task
).pack(anchor="w")

ttk.Radiobutton(
    radio_frame,
    text="Female",
    variable=gender_var,
    value="Female",
    command=radio_task
).pack(anchor="w")

# ==================================================
# 9. Combobox
# ==================================================
combo_frame = ttk.LabelFrame(window, text="9. Combobox", padding=10)
combo_frame.pack(fill="x", padx=10, pady=5)

country_var = tk.StringVar()

country_combo = ttk.Combobox(
    combo_frame,
    textvariable=country_var,
    values=("Australia", "India", "Switzerland", "USA", "Russia"),
    state="readonly"
)
country_combo.pack()

# bind connects an event with a function
def country_selected(event):
    show_output(f"Selected Country: {country_var.get()}")

country_combo.bind("<<ComboboxSelected>>", country_selected)

# ==================================================
# 10. Listbox
# ==================================================
listbox_frame = ttk.LabelFrame(window, text="10. Listbox", padding=10)
listbox_frame.pack(fill="x", padx=10, pady=5)

food_items = (
    "Pizza",
    "Burger",
    "Nachos",
    "Salad",
    "Garlic Bread"
)

food_listbox = tk.Listbox(
    listbox_frame,
    height=5,
    selectmode="extended"
)

for item in food_items:
    food_listbox.insert(tk.END, item)

food_listbox.pack()

# curselection() returns selected indexes
def get_food(event):
    selected = [
        food_listbox.get(i)
        for i in food_listbox.curselection()
    ]
    show_output(f"Foods: {selected}")

food_listbox.bind("<<ListboxSelect>>", get_food)

# ==================================================
# 11. Spinbox
# ==================================================
spinbox_frame = ttk.LabelFrame(window, text="11. Spinbox", padding=10)
spinbox_frame.pack(fill="x", padx=10, pady=5)

spin_var = tk.IntVar(value=10)

def get_spinbox():
    show_output(f"Spinbox Value: {spinbox.get()}")

spinbox = ttk.Spinbox(
    spinbox_frame,
    from_=0,
    to=100,
    textvariable=spin_var,
    wrap=True,
    command=get_spinbox
)
spinbox.pack()

# ==================================================
# 12. Variables, Events & Quit Button
# ==================================================
ttk.Button(
    window,
    text="Quit Application",
    command=window.destroy
).pack(pady=10)

# ==================================================
# Separator
# ==================================================
ttk.Separator(
    window,
    orient="horizontal"
).pack(
    fill="x",
    padx=10,
    pady=10
)

# ==================================================
# Output Area
# ==================================================
output_label = ttk.Label(
    window,
    text="Output will appear here",
    padding=10
)
output_label.pack(fill="x", padx=10, pady=10)

window.mainloop()