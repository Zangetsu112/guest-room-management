from bottle import run, route, template, error
from bottle import get, post, put, delete
from bottle import request, response, redirect

import json
import psycopg2

# Login
from authorised_user import *
@post('/api/login')
def login():
    '''
        Expected Input JSON:
            {
                'username': ...,
                'password': ...
            }
        Output JSON:
            {
                'Token': ...,
                'Message': ...
            }
    '''
    username = request.json.get('username')
    password = request.json.get('password')
    return authenticate(username, password)

@post('/api/logout')
def logout():
    '''
        Expected Input JSON:
            {
                'Token': ...,
            }
        Output JSON:
            {
                'Status': ...,
                'Message': ...
            }
    '''

# Admin
from student import *
from faculty import *
from employee import
@post('/api/add_student')
def add_student():
    '''
        Expected Input JSON:
            {
                'Name': STRING
                'Dept': STRING(3)
            }
        Output JSON:
            {
                'Status': STRING
            }
    '''

@delete('/api/delete_student')
def delete_student():
    '''
        Expected Input JSON:
            {
                'ID': STRING
            }
        Output JSON:
            {
                'Status': STRING
            }
    '''

@post('/api/add_faculty')
def add_faculty():
    '''
        Expected Input JSON:
            {
                'Name': STRING
                'Dept': STRING(3)
            }
        Output JSON:
            {
                'Status': STRING
            }
    '''

@delete('/api/delete_faculty')
def delete_faculty():
    '''
        Expected Input JSON:
            {
                'ID': STRING
            }
        Output JSON:
            {
                'Status': STRING
            }
    '''
@post('/api/add_employee')
def add_employee():
    '''
        Expected Input JSON:
            {
                'Name': STRING
                'Dept': STRING(3)
            }
        Output JSON:
            {
                'Status': STRING
            }
    '''

@delete('/api/delete_employee')
def delete_employee():
    '''
        Expected Input JSON:
            {
                'ID': STRING
            }
        Output JSON:
            {
                'Status': STRING
            }
    '''

# Manager Functionalities
@post('/api/room_price_change')
def room_price_change():
    '''
        Expected Input JSON:
        {
            'Beds': INT,
            'AC': BOOL,
            'New_Price': INT,
        }

        Output JSON:
        {
            'Status' : STRING
        }
    '''

@add('/api/add_staff_room')
def add_staff_room():
    '''
        Expected Input JSON:
        {
            'StaffId' : STRING,
            'RoomID': STRING
        }
        Output JSON:
        {
            'Status' : STRING
        }
    '''

@delete('/api/delete_staff_room')
def delete_staff_room():
    '''
        Expected Input JSON:
        {
            'StaffId' : STRING,
            'RoomID': STRING
        }
        Output JSON:
        {
            'Status' : STRING
        }
    '''

@get('/api/all_staff_room')
def all_staff_room():
    '''
        # Expected Input JSON:
        #     No input JSON

        Output JSON:
        {
            'Attributes': LIST OF ATTRIBUTES,
            'Records': LIST OF TUPLES WITH EACH TUPLE A RECORD
        }
    '''

@get('/api/view_by_name')
def view_by_name():
    '''
        Expected Input JSON:
        {
            'Name': STRING
        }
        Output JSON:
        {
            'Records': LIST OF TUPLES
        }
    '''

@get('/api/view_by_arrival')
def view_by_arrival():
    '''
        Expected Input JSON:
        {
            'Arrival' : STRING, FORMAT ('YYYY-MM-DD')
        }
        Output JSON:
        {
            'Attributes': LIST OF ATTRIBUTES,
            'Records': LIST OF TUPLES WITH EACH TUPLE A RECORD
        }
    '''

@get('/api/view_active')
def view_active():
    '''
        # Expected Input JSON:
        #     No input JSON

        Output JSON:
        {
            'Attributes': LIST OF ATTRIBUTES,
            'Records': LIST OF TUPLES WITH EACH TUPLE A RECORD
        }
    '''


# Reception Functionalities
@get('/api/check_room')
def check_room():
    '''
        Expected Input JSON:
        {
            'Beds': INT
            'AC': BOOL
        }
        Output JSON:
        {
            'Room_num' : STRING(4)
        }
    '''

@get('/api/check_price')
def check_price():
    '''
        Expected Input JSON:
        {
            'Room_num' : STRING(4)
            'Service_list' : LIST of BOOL
            'Occupant_Count' : INT
        }
        Output JSON:
        {
            'Room_Charge': INT
            'Serice_Charge': LIST OF INT
        }
    '''

@get('/api/check_relation')
def check_relation():
    '''
        Expected Input JSON:
        {
            'Nature' : [EITHER OF 'Student', 'Faculty', 'College']
            'ID' : STRING
        }
        Output JSON:
        {
            'BOOLEAN' : BOOL
        }
    '''
    pass

@put('/api/check_in')
def check_in():
    '''
        Expected Input JSON:
        {
            'GCode': STRING
            'GName': STRING
            'Phone': INT
    		'Address': STRING
    		'Nature': STRING
    		'RelationID': STRING
    		'PersonsCount': INT
    		'RID': STRING
    		'Arrival': STRING
    		'Departure': STRING
    		'Paid': INT
    		'Due': INT
    		'Total': INT
        }
        Output JSON:
        {
            'Status' : STRING (Sucessful)
        }
    '''
    rel_code = request.json.get('nature')
    rel_id = request.json.get('relation')

@delete('/api/check_out')
def check_out():
    '''
        Expected Input JSON:
        {
            'GCode': STRING
        }
        Output JSON:
        {
            'Status': STRING
        }
    '''
    pass

run(host='localhost', port=8080, debug=True)
