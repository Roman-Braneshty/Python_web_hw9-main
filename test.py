from db import session
from models import Contact, Notate
from faker import Faker

fake = Faker()
a = ['d', 'g', 'd', 'd']
contact = Contact(
            user_name='Roman Boss',
            phone='+380673933154',
            birthday='2002/07/26',
            email='email@gmail.com',
            address='address'
        )

notate = Notate(
            notate='boss cake'
)
session.add(contact)
session.add(notate)
session.commit()
