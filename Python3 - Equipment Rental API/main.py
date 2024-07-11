'''
Project: Sample Equipment Rental Application API
Creator: Jorge Pabón (pianistapr@hotmail.com)
Done:    July/10/2024
'''


#################### Initialization ####################


# to handle requests
import datetime
from flask import Flask, json, jsonify, request
# to connect to the database using flask
from flask_mysqldb import MySQL
# to simplify the use of the database
from flask_sqlalchemy import SQLAlchemy
# to convert complex data type objects to python objects
from flask_marshmallow import Marshmallow


# initialize the app in flask
app = Flask( __name__ )
# create our database connection
db = SQLAlchemy()
ma = Marshmallow()
# pass our flask app to MySQL
mysql = MySQL( app )



#################### Object Definitions ####################


'''
database models (will create tables for each class)
'''


# model for equipment in the db
class Equipment( db.Model ):
  id          = db.Column( db.Integer, primary_key = True )
  name        = db.Column( db.String( 255 ), nullable = False )
  price       = db.Column( db.Float, nullable = False )
  category    = db.Column ( db.String( 255 ), nullable = False )
  description = db.Column( db.String( 255 ), nullable = False )

  # define the constructor for this class
  def __init__( self, name, price, category, description ) -> None:
    self.name         = name
    self.price        = price
    self.category     = category
    self.description  = description

# model for customer in the db
class Customer( db.Model ):
  id          = db.Column( db.Integer, primary_key = True )
  f_name      = db.Column( db.String( 255 ), nullable = False )
  l_name      = db.Column( db.String( 255 ), nullable = False )
  address     = db.Column( db.String( 255 ), nullable = False )
  city        = db.Column( db.String( 255 ), nullable = False )
  state       = db.Column( db.String( 5 ), nullable = False )
  phone       = db.Column( db.String( 12 ), nullable = False )

  # define the constructor for this class
  def __init__( self, f_name, l_name, address, city, state, phone ) -> None:
    self.f_name   = f_name
    self.l_name   = l_name
    self.address  = address
    self.city     = city
    self.state    = state
    self.phone    = phone

# model for the equipment inventory in the db
class Inventory( db.Model ):
  equipment_id  = db.Column( db.Integer, primary_key = True )
  total         = db.Column( db.Integer, nullable = False )
  rented        = db.Column( db.Integer, nullable = False )

  # define the constructor for this class
  def __init__(self, equipment_id, total, rented) -> None:
    self.equipment_id = equipment_id
    self.total        = total
    self.rented       = rented

# model for the equipment leases in the db
class Rental( db.Model ):
  id            = db.Column( db.Integer, primary_key = True )
  customer_id   = db.Column( db.Integer, nullable = False )
  equipment_id  = db.Column( db.Integer, nullable = False )
  quantity      = db.Column( db.Integer, nullable = False )
  start         = db.Column( db.Date, nullable = False )
  end           = db.Column( db.Date, nullable = False )

  #define the constructor for this class
  def __init__(self, customer_id, equipment_id, quantity, start, end) -> None:
    self.customer_id  = customer_id
    self.equipment_id = equipment_id
    self.quantity     = quantity
    self.start        = start
    self.end          = end


'''
response objects for each class
'''

# To return equipment
class EquipmentSchema( ma.Schema ):
  class Meta:
    fields = ( 'id', 'name', 'price', 'category', 'description' )

# To return customer
class CustomerSchema( ma.Schema ):
  class Meta:
    fields = ( 'id', 'f_name', 'l_name', 'address', 'city', 'state', 'phone' )

# To return Inventory
class InventorySchema( ma.Schema ):
  class Meta:
    fields = ( 'equipment_id', 'total', 'rented' )

# To return Rentals
class RentalSchema( ma.Schema ):
  class Meta:
    fields = ( 'id', 'customer_id', 'equipment_id', 'quantity', 'start', 'end' )



#################### Database Setup ####################


'''
connect application to database, have it create the tables that we've defined in the model classes
'''


# if using MySQL
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:password@localhost/equipmentrental"
# if using SQLite
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://Database.db"
db.init_app( app )
with app.app_context():
  db.create_all()



#################### API Implementation ####################


'''
application documentation route
'''


# route to get the API information
@app.route( '/', methods = ['GET'] )
def api_doc():
  docs = '''
  <style>
    table, th, td {
      border: 1px solid black;
      border-collapse: collapse;
    }
    th, td {
      padding: 10px;
    }
    th {
      text-align: left;
    }
  </style>

  <h1>Equipment Rental API</h1>
  <hr>

  <h2>Endpoints:</h2>

  <table>
    <tr>
      <th>Endpoint</th>
      <th>Purpose</th>
    </tr>
    <tr>
      <td>/</td>
      <td>Endpoint for API Docs</td>
    </tr>
    <tr>
      <td>/Customer</td>
      <td>Endpoint for customer data</td>
    </tr>
    <tr>
      <td>/Equipment</td>
      <td>Endpoint for equipment data</td>
    </tr>
    <tr>
      <td>/Leases</td>
      <td>Endpoint for lease data</td>
    </tr>
  </table>

  <h2>Available Requests:</h2>

  <table>
    <tr>
      <th>Endpoint</th>
      <th>Request Type</th>
      <th>Body of Request</th>
      <th>Response</th>
    </tr>

    <tr>
      <td>/</td>
      <td>GET</td>
      <td>N/A</td>
      <td>The API documentation (this)</td>
    </tr>

    <tr>
      <td>/Customer</td>
      <td>GET</td>
      <td>N/A</td>
      <td>A list of the customers in 'data' and a 'message'.</td>
    </tr>
    <tr>
      <td>/Customer/{id}</td>
      <td>GET</td>
      <td>N/A</td>
      <td>The details of the specified customer in 'data' and 'message'.</td>
    </tr>
    <tr>
      <td>/Customer</td>
      <td>POST</td>
      <td>
          {<br>
            "f_name": "John",<br>
            "l_name": "Dewey",<br>
            "address": "123 South St.",<br>
            "city": "Somewhere",<br>
            "state": "MI",<br>
            "phone": "123-456-7890"<br>
          }
      </td>
      <td>A 'message'.</td>
    </tr>
    <tr>
      <td>/Customer/{id}</td>
      <td>PUT</td>
      <td>
          {<br>
            "f_name": "John",<br>
            "l_name": "Dewey",<br>
            "address": "444 North St.",<br>
            "city": "Somewhere",<br>
            "state": "MI",<br>
            "phone": "321-456-7890"<br>
          }
      </td>
      <td>A 'message'.</td>
    </tr>
    <tr>
      <td>/Customer/{id}</td>
      <td>DELETE</td>
      <td>N/A</td>
      <td>A 'message'.</td>
    </tr>

    <tr>
      <td>/Equipment</td>
      <td>GET</td>
      <td>N/A</td>
      <td>A list of the equipment in 'data' and a 'message'.</td>
    </tr>
    <tr>
      <td>/Equipment/{id}</td>
      <td>GET</td>
      <td>N/A</td>
      <td>The details of the specified equipment in 'data' and 'message'.</td>
    </tr>
    <tr>
      <td>/Equipment</td>
      <td>POST</td>
      <td>
        {<br>
          "name": "Phillips Screwdriver",<br>
          "price": 1.00,<br>
          "category": "Hand Tools",<br>
          "description": "A 6-inch, red, Phillips screw driver."<br>
        }
      </td>
      <td>A 'message'.</td>
    </tr>
    <tr>
      <td>/Equipment/{id}</td>
      <td>PUT</td>
      <td>
        {<br>
          "name": "Phillips Screwdriver",<br>
          "price": 1.50,<br>
          "category": "Hand Tools",<br>
          "description": "A 6-inch, orange, Phillips screw driver."<br>
        }
      </td>
      <td>A 'message'.</td>
    </tr>
    <tr>
      <td>/Equipment/{id}</td>
      <td>DELETE</td>
      <td>N/A</td>
      <td>A 'message'.</td>
    </tr>

    <tr>
      <td>/Inventory</td>
      <td>GET</td>
      <td>N/A</td>
      <td>A list of the items in the inventory in 'data' and a 'message'.</td>
    </tr>
    <tr>
      <td>/Inventory/{equipment_id}</td>
      <td>GET</td>
      <td>N/A</td>
      <td>The details of the specified item in the inventory.</td>
    </tr>
    <tr>
      <td>/Inventory</td>
      <td>POST</td>
      <td>
        {<br>
          "equipment_id": 1,<br>
          "total": 50,<br>
          "rented": 0<br>
        }
      </td>
      <td>A 'message'.</td>
    </tr>
    <tr>
      <td>/Inventory/{equipment_id}</td>
      <td>PUT</td>
      <td>
        {<br>
          "equipment_id": 1,<br>
          "total": 100,<br>
          "rented": 0<br>
        }
      </td>
      <td>A 'message'.</td>
    </tr>
    <tr>
      <td>/Inventory/{equipment_id}</td>
      <td>DELETE</td>
      <td>N/A</td>
      <td>A 'message'.</td>
    </tr>

    <tr>
      <td>/Rental</td>
      <td>GET</td>
      <td>N/A</td>
      <td>A list of the rentals in the system in 'data' and a 'message'.</td>
    </tr>
    <tr>
      <td>/Rental/{id}</td>
      <td>GET</td>
      <td>N/A</td>
      <td>The details of the specified rental in the inventory.</td>
    </tr>
    <tr>
      <td>/Rental</td>
      <td>POST</td>
      <td>
        {<br>
          "customer_id": 1,<br>
          "equipment_id": 2,<br>
          "quantity": 1,<br>
          "start": "2024-07-01",<br>
          "end": "2024-07-03"<br>
        }
      </td>
      <td>A 'message'.</td>
    </tr>
    <tr>
      <td>/Rental/{id}</td>
      <td>PUT</td>
      <td>
        {<br>
          "customer_id": 1,<br>
          "equipment_id": 2,<br>
          "quantity": 1,<br>
          "start": "2024-07-01",<br>
          "end": "2024-07-02"<br>
        }</td>
      <td>A 'message'.</td>
    </tr>
    <tr>
      <td>/Rental/{id}</td>
      <td>DELETE</td>
      <td></td>
      <td>A 'message'.</td>
    </tr>
  </table>

  '''
  return docs


'''
equipment application routes
'''


# route to create a new equipment entry
@app.route( '/Equipment', methods = ['POST'] )
def add_equipment():
  # grab the submitted data
  request_data = request.json
  name        = request_data['name']
  price       = request_data['price']
  category    = request_data['category']
  description = request_data['description']
  # prepare the object to store in the db
  new_equipment = Equipment( name=name, price=price, category=category, description=description )
  # store in db
  db.session.add( new_equipment )
  db.session.commit()
  return jsonify( {"message": "Equipment added to the system"} )


# route to get all equipment
@app.route( '/Equipment', methods = ['GET'] )
def get_all_equipment():
  # use the multiple equipment items schema
  all_equipment_schema = EquipmentSchema( many = True )
  all_equipment = []
  data = Equipment.query.all()
  all_equipment = all_equipment_schema.dump( data )
  return jsonify( {"message": "All equipment provided", "data": all_equipment} )


# route to get a specific equipment
@app.route( '/Equipment/<id>', methods = ['GET'] )
def get_equipment( id ):
  equipment_schema = EquipmentSchema()
  data = []
  equipment = Equipment.query.get( id )
  data = equipment_schema.dump( equipment )
  # if the equipment exists
  if data:
    return jsonify( {"message": "Equipment provided", "data": data} )
  # if id given is not valid
  else:
    response = jsonify( {"message": f"Equipment with id ({id}) was not found in the system"} )
    response.status_code = 404
    return response


# route to delete a specific equipment
@app.route( '/Equipment/<id>', methods = ['DELETE'] )
def delete_equipment( id ):
  equipment = Equipment.query.get( id )
  # if equipment exists, delete it
  if equipment:
    db.session.delete( equipment )
    db.session.commit()
    return jsonify( {"message": f"Equipment with id ({id}) was deleted from the system"} )
  else:
    response = jsonify( {"message": f"Equipment with id ({id}) was not found in the system"} )
    response.status_code = 404
    return response

# route to update a specific equipment
@app.route( '/Equipment/<id>', methods = ['PUT'] )
def update_equipment( id ):
  equipment = Equipment.query.get( id )
  # if equipment exists, update it
  if equipment:
    # grab the submitted data
    request_data = request.json
    # update the object to store in the db
    equipment.name = request_data['name']
    equipment.price = request_data['price']
    equipment.category = request_data['category']
    equipment.description = request_data['description']
    # store in db
    db.session.commit()
    return jsonify( {"message": f"Equipment with id ({id}) updated in the system"} )
  else:
    response = jsonify( {"message": f"Equipment with id ({id}) was not found in the system"} )
    response.status_code = 404
    return response


'''
customer application routes
'''


# route to create a new customer entry
@app.route( '/Customer', methods = ['POST'] )
def add_customer():
  # grab the submitted data
  request_data = request.json
  f_name  = request_data['f_name']
  l_name  = request_data['l_name']
  address = request_data['address']
  city    = request_data['city']
  state   = request_data['state']
  phone   = request_data['phone']
  # prepare the object to store in the db
  new_customer = Customer( f_name=f_name, l_name=l_name, address=address, city=city, state=state, phone=phone )
  # store in db
  db.session.add( new_customer )
  db.session.commit()
  return jsonify( {"message": "Customer added to the system"} )


# route to get all customer
@app.route( '/Customer', methods = ['GET'] )
def get_all_customers():
  # use the multiple customer items schema
  all_customer_schema = CustomerSchema( many = True )
  all_customer = []
  data = Customer.query.all()
  all_customer = all_customer_schema.dump( data )
  return jsonify( {"message": "All customers provided", "data": all_customer} )


# route to get a specific customer
@app.route( '/Customer/<id>', methods = ['GET'] )
def get_customer( id ):
  customer_schema = CustomerSchema()
  data = []
  customer = Customer.query.get( id )
  data = customer_schema.dump( customer )
  # if the customer exists
  if data:
    return jsonify( {"message": "Customer provided", "data": data} )
  # if id given is not valid
  else:
    response = jsonify( {"message": f"Customer with id ({id}) was not found in the system"} )
    response.status_code = 404
    return response


# route to delete a specific customer
@app.route( '/Customer/<id>', methods = ['DELETE'] )
def delete_customer( id ):
  customer = Customer.query.get( id )
  # if customer exists, delete it
  if customer:
    db.session.delete( customer )
    db.session.commit()
    return jsonify( {"message": f"Customer with id ({id}) was deleted from the system"} )
  else:
    response = jsonify( {"message": f"Customer with id ({id}) was not found in the system"} )
    response.status_code = 404
    return response

# route to update a specific customer
@app.route( '/Customer/<id>', methods = ['PUT'] )
def update_customer( id ):
  customer = Customer.query.get( id )
  # if customer exists, update it
  if customer:
    # grab the submitted data
    request_data = request.json
    # update the object to store in the db
    customer.f_name  = request_data['f_name']
    customer.l_name  = request_data['l_name']
    customer.address = request_data['address']
    customer.city    = request_data['city']
    customer.state   = request_data['state']
    customer.phone   = request_data['phone']
    # store in db
    db.session.commit()
    return jsonify( {"message": f"Customer with id ({id}) updated in the system"} )
  else:
    response = jsonify( {"message": f"Customer with id ({id}) was not found in the system"} )
    response.status_code = 404
    return response


'''
inventory application routes
'''


# route to create a new inventory entry
@app.route( '/Inventory', methods = ['POST'] )
def add_inventory():
  # grab the submitted data
  request_data = request.json
  equipment_id  = request_data['equipment_id']
  total         = request_data['total']
  rented        = request_data['rented']
  # prepare the object to store in the db
  new_inventory = Inventory( equipment_id=equipment_id, total=total, rented=rented )
  # store in db
  db.session.add( new_inventory )
  db.session.commit()
  return jsonify( {"message": "Item added to the system inventory"} )


# route to get all inventory
@app.route( '/Inventory', methods = ['GET'] )
def get_all_inventorys():
  # use the multiple inventory items schema
  all_inventory_schema = InventorySchema( many = True )
  all_inventory = []
  data = Inventory.query.all()
  all_inventory = all_inventory_schema.dump( data )
  return jsonify( {"message": "All inventory provided", "data": all_inventory} )


# route to get a specific inventory
@app.route( '/Inventory/<id>', methods = ['GET'] )
def get_inventory( id ):
  inventory_schema = InventorySchema()
  data = []
  inventory = Inventory.query.get( id )
  data = inventory_schema.dump( inventory )
  # if the inventory exists
  if data:
    return jsonify( {"message": "Inventory provided", "data": data} )
  # if id given is not valid
  else:
    response = jsonify( {"message": f"Inventory item with id ({id}) was not found in the system"} )
    response.status_code = 404
    return response


# route to delete a specific inventory
@app.route( '/Inventory/<id>', methods = ['DELETE'] )
def delete_inventory( id ):
  inventory = Inventory.query.get( id )
  # if inventory exists, delete it
  if inventory:
    db.session.delete( inventory )
    db.session.commit()
    return jsonify( {"message": f"Inventory item with id ({id}) was deleted from the system"} )
  else:
    response = jsonify( {"message": f"Inventory item with id ({id}) was not found in the system"} )
    response.status_code = 404
    return response

# route to update a specific inventory
@app.route( '/Inventory/<id>', methods = ['PUT'] )
def update_inventory( id ):
  inventory = Inventory.query.get( id )
  # if inventory exists, update it
  if inventory:
    # grab the submitted data
    request_data = request.json
    # update the object to store in the db
    inventory.equipment_id = request_data['equipment_id']
    inventory.total        = request_data['total']
    inventory.rented       = request_data['rented']
    # store in db
    db.session.commit()
    return jsonify( {"message": f"Inventory item with id ({id}) updated in the system"} )
  else:
    response = jsonify( {"message": f"Inventory item with id ({id}) was not found in the system"} )
    response.status_code = 404
    return response


'''
rentals application routes
'''


# route to create a new rental entry
@app.route( '/Rental', methods = ['POST'] )
def add_rental():
  # grab the submitted data
  request_data = request.json
  customer_id  = request_data['customer_id']
  equipment_id = request_data['equipment_id']
  quantity     = request_data['quantity']
  start        = request_data['start']
  end          = request_data['end']
  # prepare the object to store in the db
  new_rental = Rental( customer_id=customer_id, equipment_id=equipment_id, quantity=quantity, start=start, end=end )
  # store in db
  db.session.add( new_rental )
  db.session.commit()

  # Retrieve details to build a message
  customer = CustomerSchema()
  equipment = EquipmentSchema()
  cdata = Customer.query.get( customer_id )
  edata = Equipment.query.get( equipment_id )
  c_fname = cdata.f_name
  e_price = edata.price
  # calculate cost
  days    = ( datetime.datetime.strptime(request_data['end'], "%Y-%m-%d").date() - datetime.datetime.strptime(request_data['start'], "%Y-%m-%d").date() ).days
  total   = ( e_price * days ) * request_data['quantity']
  
  return jsonify( {"message": f"Entry added to the system rentals.  {c_fname} owes ${total} for {days} days of use."} )


# route to get all rental
@app.route( '/Rental', methods = ['GET'] )
def get_all_rentals():
  # use the multiple rental items schema
  all_rental_schema = RentalSchema( many = True )
  all_rental = []
  data = Rental.query.all()
  all_rental = all_rental_schema.dump( data )
  return jsonify( {"message": "All rentals provided", "data": all_rental} )


# route to get a specific rental
@app.route( '/Rental/<id>', methods = ['GET'] )
def get_rental( id ):
  rental_schema = RentalSchema()
  data = []
  rental = Rental.query.get( id )
  data = rental_schema.dump( rental )
  # if the rental exists
  if data:
    return jsonify( {"message": "Rental provided", "data": data} )
  # if id given is not valid
  else:
    response = jsonify( {"message": f"Rental item with id ({id}) was not found in the system"} )
    response.status_code = 404
    return response


# route to delete a specific rental
@app.route( '/Rental/<id>', methods = ['DELETE'] )
def delete_rental( id ):
  rental = Rental.query.get( id )
  # if rental exists, delete it
  if rental:
    db.session.delete( rental )
    db.session.commit()
    return jsonify( {"message": f"Rental item with id ({id}) was deleted from the system"} )
  else:
    response = jsonify( {"message": f"Rental item with id ({id}) was not found in the system"} )
    response.status_code = 404
    return response

# route to update a specific rental
@app.route( '/Rental/<id>', methods = ['PUT'] )
def update_rental( id ):
  rental = Rental.query.get( id )
  # if rental exists, update it
  if rental:
    # grab the submitted data
    request_data = request.json
    # update the object to store in the db
    rental.customer_id  = request_data['customer_id']
    rental.equipment_id = request_data['equipment_id']
    rental.quantity     = request_data['quantity']
    rental.start        = request_data['start']
    rental.end          = request_data['end']
    # store in db
    db.session.commit()
    return jsonify( {"message": f"Rental item with id ({id}) updated in the system"} )
  else:
    response = jsonify( {"message": f"Rental item with id ({id}) was not found in the system"} )
    response.status_code = 404
    return response


#################### Application Execution ####################


# run the app
if __name__ == '__main__':
  # when making changes, set to True so that you don't have to stop and start the app to see changes
  app.run( debug = True )