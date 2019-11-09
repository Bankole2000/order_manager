import sqlite3

class Database: 
  def __init__(self, db): 
    self.conn = sqlite3.connect(db)
    self.cur = self.conn.cursor()
    self.cur.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, product text, customer text, retailer text, price text)")
    self.conn.commit()
  
  def fetch(self): 
    self.cur.execute("SELECT * FROM orders")
    rows = self.cur.fetchall()
    return rows

  def insert(self, product, customer, retailer, price): 
    self.cur.execute("INSERT INTO orders VALUES (NULL, ?, ?, ?, ?)", (product, customer, retailer, price))
    self.conn.commit()

  def remove(self, id): 
    self.cur.execute("DELETE FROM orders WHERE id=?", (id,))
    self.conn.commit()

  def update(self, id, product, customer, retailer, price):
    self.cur.execute("UPDATE orders SET product = ?, customer = ?, retailer = ?, price = ? WHERE id = ?", (product, customer, retailer, price, id))
    self.conn.commit()

  def __del__(self):
    self.conn.close()

# db = Database('store.db')
# db.insert("HP Envy 2019 Bang and Olufsen","Chibundu Abokhai","HP Computers Banex Abuja","360000")
# db.insert("iPhone 11 Pro","Teniola Esan","Apple Store Lekki","500000")
# db.insert("Samsung A70","Bankole Esan","Samsung Office Banex Abuja","130000")
# db.insert("Microsoft Surface Pro 2","OluwaToni Esan","Microsoft UK","400000")
# db.insert("Benz M-Class 300 Series","Kunle Fakoya","Benz Official Dealer Texas UK","2500000")



