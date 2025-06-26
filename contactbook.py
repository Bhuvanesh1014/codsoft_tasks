import tkinter as tk
from tkinter import messagebox
import json
import os

CONTACTS_FILE = "contacts.json"

# Load existing contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return []

# Save contacts to file
def save_contacts():
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# Add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone Number are required!")
        return

    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts()
    messagebox.showinfo("Success", "Contact added successfully!")
    clear_entries()
    display_contacts()

# Display all contacts in the listbox
def display_contacts():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Clear form fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Search contacts
def search_contact():
    query = search_entry.get().lower()
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Delete selected contact
def delete_contact():
    selected = contact_listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")
        return
    index = selected[0]
    contact = contacts[index]
    confirm = messagebox.askyesno("Delete Contact", f"Are you sure you want to delete {contact['name']}?")
    if confirm:
        contacts.pop(index)
        save_contacts()
        display_contacts()

# Update selected contact
def update_contact():
    selected = contact_listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a contact to update.")
        return
    index = selected[0]

    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone Number are required!")
        return

    contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
    save_contacts()
    messagebox.showinfo("Updated", "Contact updated successfully!")
    display_contacts()

# Load selected contact into form
def load_selected_contact(event):
    selected = contact_listbox.curselection()
    if not selected:
        return
    index = selected[0]
    contact = contacts[index]
    name_entry.delete(0, tk.END)
    name_entry.insert(0, contact["name"])
    phone_entry.delete(0, tk.END)
    phone_entry.insert(0, contact["phone"])
    email_entry.delete(0, tk.END)
    email_entry.insert(0, contact["email"])
    address_entry.delete(0, tk.END)
    address_entry.insert(0, contact["address"])

# Initialize contacts
contacts = load_contacts()

# --- GUI Setup ---
root = tk.Tk()
root.title("📒 Contact Book")
root.geometry("500x600")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

tk.Label(root, text="Contact Book", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)

# Form Frame
form_frame = tk.Frame(root, bg="#f0f0f0")
form_frame.pack(pady=10)

tk.Label(form_frame, text="Name:", bg="#f0f0f0").grid(row=0, column=0, sticky='w')
tk.Label(form_frame, text="Phone:", bg="#f0f0f0").grid(row=1, column=0, sticky='w')
tk.Label(form_frame, text="Email:", bg="#f0f0f0").grid(row=2, column=0, sticky='w')
tk.Label(form_frame, text="Address:", bg="#f0f0f0").grid(row=3, column=0, sticky='w')

name_entry = tk.Entry(form_frame, width=40)
phone_entry = tk.Entry(form_frame, width=40)
email_entry = tk.Entry(form_frame, width=40)
address_entry = tk.Entry(form_frame, width=40)

name_entry.grid(row=0, column=1, pady=2)
phone_entry.grid(row=1, column=1, pady=2)
email_entry.grid(row=2, column=1, pady=2)
address_entry.grid(row=3, column=1, pady=2)

# Buttons
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Contact", width=15, command=add_contact).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update Contact", width=15, command=update_contact).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete Contact", width=15, command=delete_contact).grid(row=0, column=2, padx=5)

# Search Field
search_frame = tk.Frame(root, bg="#f0f0f0")
search_frame.pack(pady=10)
tk.Label(search_frame, text="Search:", bg="#f0f0f0").pack(side=tk.LEFT)
search_entry = tk.Entry(search_frame, width=30)
search_entry.pack(side=tk.LEFT, padx=5)
tk.Button(search_frame, text="Search", command=search_contact).pack(side=tk.LEFT)

# Contact List
contact_listbox = tk.Listbox(root, width=60, height=10)
contact_listbox.pack(pady=10)
contact_listbox.bind("<<ListboxSelect>>", load_selected_contact)

# Initial Display
display_contacts()

root.mainloop()
