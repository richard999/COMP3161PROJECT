import pandas as pd
from faker import Faker
from collections import defaultdict
from sqlalchemy import create_engine

fake = Faker()
fake_data = defaultdict(list)

for _ in range(200000):
    fake_data["Fname"].append( fake.first_name() )
    fake_data["Lname"].append( fake.last_name() )
    fake_data["Password"].append( fake.password(length=15) )
    fake_data["Email"].append( fake.email() )
    fake_data["Address"].append( fake.address() )


df_fake_data = pd.DataFrame(fake_data)

engine = create_engine('mysql://root:@localhost/mealdb', echo=False)

df_fake_data.to_sql('User', con=engine,index=False)



rfake = Faker()
fake_rec = defaultdict(list)

for i in range(600000):
    fake_rec["Date_Created"].append(fake.date_this_year())
    fake_rec["Total_Calories"].append(fake.random_int(min=100, max=3000))
    fake_rec["RecipeName"].append(fake.license_plate())
    fake_rec["Description"].append(fake.street_name())



df_fake_rec = pd.DataFrame(fake_rec)

engine = create_engine('mysql://root:@localhost/mealdb', echo=False)

df_fake_rec.to_sql('Recipe', con=engine,index=False)