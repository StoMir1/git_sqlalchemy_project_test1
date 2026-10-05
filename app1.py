from sqlalchemy import create_engine, Column, INTEGER, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///digishop.db")
engine.connect()

Base = declarative_base()

class User(Base):
    __tablename__ = 'userInfo'

    id = Column(INTEGER, primary_key=True)
    name = Column(String)
    address = Column(String)
    score = Column(Float)

class Product(Base):
    __tablename__ = 'ProductInfo'

    id = Column(INTEGER, primary_key=True)
    name_product = Column(String)
    price = Column(Float)
    quantity = Column(INTEGER)
    

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
sessionLocal = Session()
#####################################################

# user1 = User(name='Ali', address= 'Ahwaz', score=4.9)
# user2 = User(name='Morteza', address= 'Tehran', score=4.95)

# sessionLocal.add(user1)
# sessionLocal.add(user2)
# sessionLocal.commit()

#####################################################

#user3 = User(name='AliReza', address= 'Ahwaz', score=4.7)
#user4 = User(name='Nima', address= 'Shiraz', score=4.90)

#sessionLocal.add_all([user3,user4])
#sessionLocal.commit()

#####################################################

# users = sessionLocal.query(User).all() # --> select all records
# #print(users)
# for item in users:
#     print('name: ', item.name)
#     print('add: ', item.address)
#     print('score: ', item.score)
#     print('-' * 30)

# Product1 = Product(name_product='laptop',price=2000,quantity=5)
# Product2 = Product(name_product='mouse',price=50,quantity=400)

# sessionLocal.add_all([Product1,Product2])
# sessionLocal.commit()

# product = sessionLocal.query(Product).all()
# for item in product:
#     print('name: ', item.name_product)
#     print('price: ', item.price)
#     print('quantity: ', item.quantity)
#     print('-' * 30)

#####################################################

# temp_user = sessionLocal.query(User).filter_by(address='Ahwaz').all()
# print(temp_user[-1].name)
# print(temp_user[-1].address)

#####################################################

# temp_user = sessionLocal.query(User).filter(User.score > 4.8).all()
# print(temp_user)
# for item in temp_user:
#     print(item.name)
#     print(item.score)
#     print('-'*30)

# temp_user = sessionLocal.query(User).filter(User.name.like('%Ali%')).all()
# for item in temp_user:
#     print(item.name)
#     print(item.address)
#     print(item.score)
#     print('-'*30)

# temp_user = sessionLocal.query(Product).filter(Product.price > 200).all()
# for item in temp_user:
#     print(item.name_product)
#     print(item.price)
#     print(item.quantity)

# temp_user = sessionLocal.query(Product).filter(Product.name_product.like('%lap%')).all()
# for item in temp_user:
#     print(item.name_product)
#     print(item.price)
#     print(item.quantity)

####################################################

user = sessionLocal.query(User).filter_by(id=1).first()
product = sessionLocal.query(Product).filter(Product.price > 1000).first()

# user.name = 'Saeed'
# user.address = 'Tabriz'
# sessionLocal.commit()

####################################################

# if user !=None:
#     sessionLocal.delete(user)
#     sessionLocal.commit()

if product !=None:
    sessionLocal.delete(product)
    sessionLocal.commit()