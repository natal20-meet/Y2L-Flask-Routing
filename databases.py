from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name,price,description,picture):
	product_object = Product(
	        name=name,
	        price=price,
	        description=description,
	        picture=picture)
	    session.add(product_object)
	    session.commit() 

def edit_product(ID, description):
	product_object = session.query(Product).filter_by(id=ID).first()
	product_object.description = description
	session.commit()

def delete_product(ID):
	product_object = session.query(Product).filter_by(id=ID).delete()	
	session.commit()

def query_products():
	products = session.query(Product).all()
	return products


def query_by_name(ID):
	products = session.query(Product).filter_by(id=ID).first()
	return products

def add_to_cart(productID):
	product_object = Cart( 
		productID = productID)
	session.add(product_object)
	session.commit()
	
