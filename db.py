import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()
cnx = mysql.connector.connect(
  host=os.environ.get('RDS_DB_ENDPOINT'),
  user=os.environ.get('RDS_DB_USERNAME'),
  password=os.environ.get('RDS_DB_PASSWORD'),
  # database=os.environ.get('RDS_DB_NAME'),
)
cursor = cnx.cursor()