# st.title("Ankur Mishra")
# st.write("Hello streamlit I am in the write method")
# st.text("Writing this text in text")
# st.markdown("Hello I am markdown")

# name = st.text_input("Enter your name:")
# age = st.number_input("Enter your age:", min_value=0, max_value=120)
# st.write(f"Hello {name}, you are {age} years old!")
'''
import streamlit as st
from sqlalchemy import create_engine, text
import urllib.parse

#database configuration
DB_HOST = "127.0.0.1" # Replce your m
DB_PORT = "3306"
DB_NAME = "STUDENT_DATABASE"
DB_USER = 'ROOT'
DB_PASSWORD = urllib.parse.quote("#Pandat9810")

#CREATE A CONNECTION TO DATABASE 
db_url = f"mysql=pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(db_url)





def insert_data(firstname, lastname, title, age, nationality, registration_status, num_course, num_semester):
    query = text(
        """
        INSERT INTO STUDENT_DATA(firstname, lastname, title, age, nationality, registration_status, num_course, num_semester)
        VALUES (firstname, lastname, title, age, nationality, registration_status, num_course, num_semester)
        """
    )
    try:
        print(f"Inserting data:({firstname}, {lastname}, {title}, {age}, {nationality}, {registration_status}, {num_course}, {num_semester}")
        with engine.connect() as conn:
            conn.execute(query, {
                "firstname": firstname,
                "lastname":lastname,
                "title":title,
                "age":age,
                "nationality":nationality,
                "registration_status":registration_status,
                "num_course":num_course,
                "num_semester":num_semester
            })
            conn.commit()
    except Exception as e:
        print(f"Error occurred{e}")
        raise RuntimeError(f"Database operation failed: {e}")










with st.form("Student Data Entry Form"):
    st.title("User Information")
    firstName = st.text_input("Enter First name")
    lastName = st.text_input("Enter Last name")
    title = st.selectbox("Title", ["","Mr. ", "Ms. ", "Dr. "])
    age = st.number_input("Age", min_value=18, max_value=80, step = 1)
    nationlity = st.selectbox("nationlity", ["", "India", "Aisa", "Europe", "South America"])

     # Course info
    st.header("Course Information")
    registration_status = st.radio(
        "Registration Status", ["Registered", "Not Registered"], index=1
    )
    num_courses = st.number_input("# Completed Courses", min_value=0, step=1)
    num_semesters = st.number_input("# Semesters", min_value=0, step=1)

    # Terms and conditions
    st.header("Terms & Conditions")
    accepted = st.checkbox("I accept the terms and conditions.")

    # Submit button
    submitted = st.form_submit_button("Submit")


    submitted = st.form_submit_button("Submit")

    if submitted:
        if accepted:
            if firstName.strip() and lastName.strip():  # Ensure fields are not empty
                try:
                    insert_data(firstName, lastName, title, age, nationlity, registration_status, num_courses, num_semesters)
                    st.success("Data successfully submitted!")
                except RuntimeError as e:
                    st.error(f"An error occurred: {e}")
            else:
                st.warning("First name and last name are required.")
        else:
            st.warning("You must accept the terms and conditions to proceed.")


'''



import streamlit as st
from sqlalchemy import create_engine, text
import urllib.parse

# Database configuration
DB_HOST = "127.0.0.1"  # Replace with your MySQL server host (e.g., IP address or domain)
DB_PORT = "3306"  # MySQL default port
DB_NAME = "student_data"  # Replace with your database name
DB_USER = "root"  # Replace with your MySQL username
DB_PASSWORD = urllib.parse.quote("#Pandat9810")  # URL-encode your password if it contains special characters

# Create a connection to the database
db_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(db_url)


def clear_form():
    st.session_state['firstname'] = ''
    st.session_state['lastemail'] = ''
    st.session_state['title'] = ''
    st.session_state['age'] = ''
    st.session_state['nationality'] = ''
    st.session_state['registration_status'] = ''
    st.session_state['num_course'] = ''
    st.session_state['num_semester'] = ''



# Function to insert data into the database
def insert_data(firstname, lastname, title, age, nationality, registration_status, num_course, num_semester):
    query = text(
        """
        INSERT INTO Student_Data (firstname, lastname, title, age, nationality, registration_status, num_course, num_semester)
        VALUES (:firstname, :lastname, :title, :age, :nationality, :registration_status, :num_course, :num_semester)
        """
    )
    try:
        # Debugging: Print the data being inserted
        print(f"Inserting data: {firstname}, {lastname}, {title}, {age}, {nationality}, {registration_status}, {num_course}, {num_semester}")
        with engine.connect() as conn:
            conn.execute(query, {
                "firstname": firstname,
                "lastname": lastname,
                "title": title,
                "age": age,
                "nationality": nationality,
                "registration_status": registration_status,
                "num_course": num_course,
                "num_semester": num_semester
            })
            # Commit the transaction explicitly
            conn.commit()
    except Exception as e:
        print(f"Error occurred: {e}")
        raise RuntimeError(f"Database operation failed: {e}")

# Streamlit UI
st.title("Student Data Entry Form")

with st.form("data_entry_form"):
    # User info
    st.header("User Information")
    firstname = st.text_input("First Name", value=st.session_state['firstname'], key='firstname')
    lastname = st.text_input("Last Name", value=st.session_state['lastname'], key='lastname')
    title = st.selectbox("Title", ["", "Mr.", "Ms.", "Dr."], value=st.session_state['Title'], key='Title')
    age = st.number_input("Age", min_value=18, max_value=110, step=1, value=st.session_state['Age'], key='Age')
    nationality = st.selectbox(
        "Nationality", ["", "Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"],value=st.session_state['Nationality'], key='Nationality'
    )

    # Course info
    st.header("Course Information")
    registration_status = st.radio(
        "Registration Status", ["Registered", "Not Registered"], index=1,value=st.session_state['registration_status'], key='registration_status'
    )
    num_courses = st.number_input("# Completed Courses", min_value=0, step=1, value=st.session_state['num_courses'], key='num_courses' )
    num_semesters = st.number_input("# Semesters", min_value=0, step=1, value=st.session_state['num_semesters'], key='num_semesters')

    # Terms and conditions
    st.header("Terms & Conditions")
    accepted = st.checkbox("I accept the terms and conditions.")

    # Submit button
    submitted = st.form_submit_button("Submit")

    if submitted:
        if accepted:
            if firstname.strip() and lastname.strip():  # Ensure fields are not empty
                try:
                    insert_data(firstname, lastname, title, age, nationality, registration_status, num_courses, num_semesters)
                    st.success("Data successfully submitted!")
                except RuntimeError as e:
                    st.error(f"An error occurred: {e}")
            else:
                st.warning("First name and last name are required.")
        else:
            st.warning("You must accept the terms and conditions to proceed.")
    clear_form()

