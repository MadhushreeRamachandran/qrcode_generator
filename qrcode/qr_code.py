import qrcode
from tkinter import *
from tkinter import colorchooser, filedialog, messagebox
from PIL import Image, ImageTk

# Function to generate QR code
def generate_qr():
    try:
        # Get user input values
        link = entry_link.get()
        box_size = int(entry_box_size.get())
        border_size = int(entry_border_size.get())
        fill_color = fill_color_var.get()
        back_color = back_color_var.get()

        # Create QR code object with custom options
        qr = qrcode.QRCode(version=1, box_size=box_size, border=border_size)
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)

        # Display the QR code in the preview area
        img.thumbnail((200, 200))  # Resize for preview
        img = ImageTk.PhotoImage(img)
        qr_output_label.configure(image=img)
        qr_output_label.image = img  # Keep a reference to avoid garbage collection
        qr_output_label.grid(row=0, column=0, padx=10, pady=10)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to save QR code image
def save_qr():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        link = entry_link.get()
        box_size = int(entry_box_size.get())
        border_size = int(entry_border_size.get())
        fill_color = fill_color_var.get()
        back_color = back_color_var.get()
        
        qr = qrcode.QRCode(version=1, box_size=box_size, border=border_size)
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img.save(file_path)
        messagebox.showinfo("Success", f"QR code saved at {file_path}")

# Function to select color for fill
def select_fill_color():
    color = colorchooser.askcolor()[1]
    if color:
        fill_color_var.set(color)

# Function to select color for background
def select_back_color():
    color = colorchooser.askcolor()[1]
    if color:
        back_color_var.set(color)

# Initialize Tkinter window
app = Tk()
app.title("Enhanced QR Code Generator")
app.geometry("600x500")
app.configure(bg="#f0f0f0")

# Fonts
title_font = ("Helvetica", 14, "bold")
label_font = ("Helvetica", 10)
button_font = ("Helvetica", 10, "bold")

# Title
title_label = Label(app, text="QR Code Generator", font=title_font, bg="#f0f0f0")
title_label.pack(pady=10)

# Main Frame for QR Code details and preview side by side
main_frame = Frame(app, bg="#ffffff", padx=20, pady=20, relief="groove", bd=2)
main_frame.pack(pady=10, fill=BOTH, expand=True)

# Input Frame for QR Code details on the left
input_frame = Frame(main_frame, bg="#ffffff")
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

# Link input
Label(input_frame, text="Enter URL or Text for QR Code:", font=label_font, bg="#ffffff").grid(row=0, column=0, sticky="w", pady=(0, 5))
entry_link = Entry(input_frame, width=40, font=label_font)
entry_link.grid(row=1, column=0, pady=(0, 10))

# Box size input
Label(input_frame, text="Box Size:", font=label_font, bg="#ffffff").grid(row=2, column=0, sticky="w", pady=(10, 5))
entry_box_size = Entry(input_frame, width=10, font=label_font)
entry_box_size.insert(0, "5")
entry_box_size.grid(row=3, column=0, pady=(0, 10))

# Border size input
Label(input_frame, text="Border Size:", font=label_font, bg="#ffffff").grid(row=4, column=0, sticky="w", pady=(10, 5))
entry_border_size = Entry(input_frame, width=10, font=label_font)
entry_border_size.insert(0, "5")
entry_border_size.grid(row=5, column=0, pady=(0, 10))

# Color selection
fill_color_var = StringVar(value="black")
back_color_var = StringVar(value="white")
Label(input_frame, text="Fill Color:", font=label_font, bg="#ffffff").grid(row=6, column=0, sticky="w", pady=(10, 5))
Button(input_frame, text="Select Fill Color", command=select_fill_color, font=button_font, bg="#cccccc", fg="#333333").grid(row=7, column=0, pady=(0, 10))
Label(input_frame, text="Background Color:", font=label_font, bg="#ffffff").grid(row=8, column=0, sticky="w", pady=(10, 5))
Button(input_frame, text="Select Background Color", command=select_back_color, font=button_font, bg="#cccccc", fg="#333333").grid(row=9, column=0, pady=(0, 10))

# QR code generation button
Button(input_frame, text="Generate QR Code", command=generate_qr, font=button_font, bg="#007acc", fg="white", relief="raised").grid(row=10, column=0, pady=(20, 10))

# Output Frame on the right for QR Code preview
output_frame = Frame(main_frame, bg="#ffffff", relief="groove", bd=2)
output_frame.grid(row=0, column=1, padx=10, pady=10)

# Label in output frame to display generated QR code
output_label = Label(output_frame, text="QR Code Preview", font=label_font, bg="#ffffff")
output_label.grid(row=0, column=0, pady=(0, 10))
qr_output_label = Label(output_frame, bg="#ffffff")
qr_output_label.grid(row=1, column=0)

# Save QR code button at the bottom
Button(app, text="Save QR Code", command=save_qr, font=button_font, bg="#4CAF50", fg="white", relief="raised").pack(pady=(10, 20))

app.mainloop()
