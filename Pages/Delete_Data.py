import streamlit as st
from sqlalchemy import create_engine, text
import urllib.parse


# Database connection setup
DB_HOST = "127.0.0.1"
DB_PORT = "3306"
DB_NAME = "student_data"
DB_USER = "root"
DB_PASSWORD = urllib.parse.quote("#Pandat9810")
db_url = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(db_url)

def delete_data(student_id):
    query = text("DELETE FROM student_data WHERE ID = :student_id ")
    with engine.connect() as con:
        con.execute(query, {"student_id": student_id})
        con.commit()

st.title("Delete Student Data")
student_id = st.number_input("Enter Student ID to Delete",min_value = 1, step=1)
if st.button("Delete"):
    try:
        delete_data(student_id)
        st.success(f"Data with Student ID {student_id} successfully delete!")
    except Exception as e:
        st.error(f"Error deleting data : {e}")

