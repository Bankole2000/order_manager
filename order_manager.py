from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')


# functions
def populate_list():
  orders_list.delete(0, END)
  for row in db.fetch(): 
    orders_list.insert(END, row)
  print('Populate list')

def add_order():
  if order_text.get() == '' or customer_text.get() == '' or retailer_text.get() == '' or price_text.get() == '': 
    messagebox.showerror('Required Fields', 'Please fill all the fields')
    return
  db.insert(order_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
  orders_list.delete(0, END)
  orders_list.insert(END, (order_text.get(), customer_text.get(), retailer_text.get(), price_text.get()))
  clear_order()
  populate_list()
  print('Added Order')

def select_item(event): 
  global selected_item
  index = orders_list.curselection()[0]
  selected_item = orders_list.get(index)
  print(selected_item)
  # 
  order_entry.delete(0, END)
  order_entry.insert(END, selected_item[1])
  customer_entry.delete(0, END)
  customer_entry.insert(END, selected_item[2])
  retailer_entry.delete(0, END)
  retailer_entry.insert(END, selected_item[3])
  price_entry.delete(0, END)
  price_entry.insert(END, selected_item[4])

def update_order():
  db.update(selected_item[0], order_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
  populate_list()
  print('Update Order')

def remove_order():
  db.remove(selected_item[0])
  clear_order()
  populate_list()
  print('Remove Order')

def clear_order():
  print('Clear Order')
  order_entry.delete(0, END)
  customer_entry.delete(0, END)
  retailer_entry.delete(0, END)
  price_entry.delete(0, END)
   

# Create window object
app = Tk()

# Order
order_text = StringVar()
order_label = Label(app, text='Order Name', font=('bold',12), pady=20, padx=20)
order_label.grid(row=0, column=0, sticky=W) 
order_entry = Entry(app, textvariable=order_text)
order_entry.grid(row=0, column=1)

# Customer
customer_text = StringVar()
customer_label = Label(app, text='Customer Name', font=('bold',12), pady=20, padx=20)
customer_label.grid(row=0, column=2) 
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

# Retailer
retailer_text = StringVar()
retailer_label = Label(app, text='Retailer Name', font=('bold',12), pady=20, padx=20)
retailer_label.grid(row=1, column=0) 
retailer_entry = Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1)

# Price
price_text = StringVar()
price_label = Label(app, text='Price in N', font=('bold',12), pady=20, padx=20)
price_label.grid(row=1, column=2) 
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)

# Order List
orders_list = Listbox(app, height=8, width=85)
orders_list.grid(row=3, column=0, columnspan=4, rowspan=6)

# Create Scroll Bar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=4, sticky=W, columnspan=2)

# Set scroll to listbox
orders_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=orders_list.yview)

# Bind Select
orders_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(app, text="Add Order", width=12, command=add_order) #command=add_order
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text="Remove Order", width=12, command=remove_order) #command=remove_order
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text="Update Order", width=12, command=update_order) #command=update_order
update_btn.grid(row=2, column=2)

Clear_btn = Button(app, text="Clear Form", width=12, command=clear_order) #command=clear_order
Clear_btn.grid(row=2, column=3)


app.title('Order Manager')
app.geometry('600x350')

# Populate List
populate_list()

# Start program 
app.mainloop()
