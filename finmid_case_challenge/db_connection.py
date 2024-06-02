
import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection settings
db_username = 'postgres'
db_password = 'finmid'
db_host = 'localhost'
db_port = '5432'
db_name = 'postgres'  # Assuming you are connecting to the default 'postgres' database

# Create SQLAlchemy engine
engine = create_engine(f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')