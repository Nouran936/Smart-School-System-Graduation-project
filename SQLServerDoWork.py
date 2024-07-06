import pyodbc
import Display_Video
import datetime
DRIVER_NAME = 'SQL SERVER'
SERVER=f"localhost\\sqlexpress"
DATABASE_NAME="Gp"
SERVER_NAME= "DESKTOP-2KON84S\SQLEXPRESS"
connection_string = f"""
DRIVER={{{DRIVER_NAME}}};
SERVER={SERVER_NAME};
DATABASE={DATABASE_NAME};
Trust Connection=yes;
"""
def Add_Violence_Incidences(current_datetime,path):
    conn = pyodbc.connect(connection_string)
    SQL_QUERY = """
    INSERT INTO Violence_Incidences 
    VALUES (?, ?)
    """

    cursor = conn.cursor()
    cursor.execute(SQL_QUERY,(current_datetime,path))
    conn.commit()
    cursor.close()

def Diplay_Violence_Incidences():
    conn = pyodbc.connect(connection_string)
    SQL_QUERY="select * from Violence_Incidences "
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)
    records = cursor.fetchall()
    x=[]
    for r in records:
        #print("ds")
        x.append((r.Id, r.Date, r.path))
        #print(f"{r.Id} {r.Date} {r.path}")
        #Display_Video.Display_Video(r.path)
    cursor.close()
    conn.close()
    return x
# r=Diplay_Violence_Incidences()
# for x in r:
#     print(x[1])

def showStudeentStatus(date):
    conn = pyodbc.connect(connection_string)
    SQL_QUERY = """
        SELECT s.id,s.name, sa.date,s.StClass
        FROM Students AS s
        LEFT JOIN Student_Attendance AS sa ON sa.id = s.id AND CAST(sa.date AS DATE) = ? 
        ORDER BY s.id;
        """
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY, (date,))
    records = cursor.fetchall()
    x = []
    for r in records:
        x.append((r.id,r.name, r.date,r.StClass))
    cursor.close()
    conn.close()
    return x




# z=showStudeentStatus("2024-04-14")
# for var in z:
#     print(var[0],var[1],var[2],var[3])

def showStudeentStatusWithoutDate():
    conn = pyodbc.connect(connection_string)
    SQL_QUERY = """
        SELECT s.id,s.name, sa.date,s.StClass
        FROM Students AS s
        inner JOIN Student_Attendance AS sa ON sa.id = s.id 
        ORDER BY s.id;
        """
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)
    records = cursor.fetchall()
    x = []
    for r in records:
        x.append((r.id,r.name, r.date,r.StClass))
    cursor.close()
    conn.close()
    return x


def diplayAllStudents():
    conn = pyodbc.connect(connection_string)
    SQL_QUERY = "select * from Students "
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)
    records = cursor.fetchall()
    x = []
    for r in records:
        # print("ds")
        x.append((r.id, r.name, r.Gender,r.StClass,r.Birthdate,r.Age,r.Address,r.phone,r.email,r.AdmissionDate))
        # print(f"{r.Id} {r.Date} {r.path}")
        # Display_Video.Display_Video(r.path)
    cursor.close()
    conn.close()
    return x


# z=diplayAllStudents()
# for var in z:
#     print(var[0],var[1],var[2],var[3],var[4])


def AddStudent(id,name,gender,stClass,DOB,Age,Addr,Phone,email):
    conn = pyodbc.connect(connection_string)
    SQL_QUERY = """
       INSERT INTO Students 
       VALUES (?,?,? ,?,?,? ,?,?,?,?)
       """

    cursor = conn.cursor()
    current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #print(id)
    cursor.execute(SQL_QUERY, (int(id), name,gender,stClass,DOB,int(Age),Addr,Phone,email,current_datetime))
    conn.commit()
    cursor.close()

def AddStudentAttendance(ids,times):
    conn = pyodbc.connect(connection_string)
    SQL_QUERY = """
       INSERT INTO Student_Attendance 
       VALUES (?, ?)
       """

    cursor = conn.cursor()

    for id,time in zip(ids,times):
        cursor.execute(SQL_QUERY, (int(id), time))
        #print(f"id {int(id)} Time{time}")
    conn.commit()
    cursor.close()

def findStudentsById(ids):
    conn = pyodbc.connect(connection_string)
    # Build the parameter placeholders for the IN clause
    #ids = [str(id).rstrip('.') for id in ids]

    placeholders = ','.join('?' for _ in ids)

    SQL_QUERY = f"""
           SELECT s.id, s.name
           FROM Students AS s
           WHERE s.id IN ({placeholders})
       """

    with pyodbc.connect(connection_string) as conn:
        with conn.cursor() as cursor:
            cursor.execute(SQL_QUERY, ids)
            records = cursor.fetchall()
            result = [(r.id, r.name) for r in records]

    #print(result)
    return result

#findStudentsById(['449','901'])
#AddStudent(223,"name","gender","stClass","4/18/2024",5,"Addr","Phone","email")
#diplayAllStudents()
#findStudentsById([449,312])