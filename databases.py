from model import *


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session 


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = scoped_session(sessionmaker(bind=engine,autoflush=False))

def add_product(name,price,Description,picture):
	product_object = Product(
	        name=name,
	        price=price,
	        Description=Description,
	        picture=picture)
	session.add(product_object)
	session.commit() 

# add_product("old record", 20 , "an old unknown record, buy it and try it", "heres a pic" )


def edit_product(ID, Dsescription):
	product_object = session.query(Product).filter_by(ID=ID).first()
	product_object.description = description
	session.commit()

def delete_product(ID):
	product_object = session.query(Product).filter_by(ID=ID).delete()	
	session.commit()

def query_products():
	products = session.query(Product).all()
	return products


def query_by_name(ID):
	products = session.query(Product).filter_by(ID=ID).first()
	return products

def add_to_cart(productID):
	product_object = Cart( 
		productID = productID)
	session.add(product_object)
	session.commit()
	
