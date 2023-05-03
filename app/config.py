import os
import socket

postgres_host = "db"
ip_address = socket.gethostbyname(postgres_host)

username= 'hime' #os.environ.get('POSTGRES_USER')
pwd = 'hime' #os.environ.get('POSTGRES_PASSWORD')
database = 'note' #os.environ.get('POSTGRES_DB')
port_id = 5432

url= f'postgresql://{username}:{pwd}@{ip_address}:{port_id}/{database}'
