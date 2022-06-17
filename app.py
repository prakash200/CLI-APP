# while signup check exist email and email correctection
#In read.md developer options like check database,table and user options

import hashlib
import typer
import sqlite3
import requests

app = typer.Typer()

@app.command()
def createdatabase():
    conn = sqlite3.connect("Users_Details.db")
    print ("Created Users_Details Database successfully!");
    conn.close();


@app.command()
def createtable():
    conn = sqlite3.connect('Users_Details.db')
    try:
        conn.execute('''CREATE TABLE Login_Details
                (NAME           TEXT    NOT NULL,
                EMAIL_ID            char(50),
                PASSWORD        CHAR(50),
                LOGIN_STATUS         INT NOT NULL);''')
        print ("created Login_Details Table successfully!");
    except :
        print("Table Login_Details Already Created!")

    conn.close();

@app.command()
def signup(name: str , email: str , password: str , confirm_password: str):
    conn = sqlite3.connect('Users_Details.db')
    data = conn.execute("SELECT name, EMAIL_ID, PASSWORD , LOGIN_STATUS from Login_Details where EMAIL_ID = ?",(email,))
    if data.fetchone():
        print("Email-id Already Exists!")
    elif password == confirm_password:
        enc = confirm_password.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        conn.execute("INSERT INTO Login_Details (NAME ,EMAIL_ID ,PASSWORD, LOGIN_STATUS) \
        VALUES (?, ?, ?, 0)",(name,email,hash1));
        conn.commit();
        print("You have registered successfully!")
    else:
        print("Both Passwords doesn't match!")
    conn.close();


@app.command()
def login(email: str , password: str):
    conn = sqlite3.connect('Users_Details.db')
    data = conn.execute("SELECT EMAIL_ID, PASSWORD , LOGIN_STATUS from Login_Details where EMAIL_ID = ?",(email,))
    if (data.fetchone()) is None:
        print("Invalid Credentials!")
    else:
        data_1 = conn.execute("SELECT  name , Email_id , PASSWORD ,LOGIN_STATUS from Login_Details where EMAIL_ID = ?",(email,))
        auth = password.encode()
        auth_hash = hashlib.md5(auth).hexdigest()
        for i in data_1:
            hashpassword = i[2]
            name = i[0]
            log_status = i[3]
        if auth_hash == hashpassword:
            if log_status==1:
                print("Hi "+str(name)+"!")
                print("Already Logged in")
            else:
                conn.execute("UPDATE Login_Details set LOGIN_STATUS = 1 where EMAIL_ID = ?",(email,))
                conn.commit();
                print("Logged in Successfully!")
                print("Hi "+str(name)+"!")
                print("-----  Weleocome to our App  -----")
        else:
            print("Invalid Credentials!")
    conn.close()

@app.command()
def logout(email: str):
    conn = sqlite3.connect('Users_Details.db')
    data_1 = conn.execute("SELECT  LOGIN_STATUS from Login_Details where EMAIL_ID = ?",(email,))
    for i in data_1:
        if i[0]==0:
            print("Signup/Login First")
        else:
            conn.execute("UPDATE Login_Details set LOGIN_STATUS = 0 where EMAIL_ID = ?",(email,))
            conn.commit();
            print("Loggedout Successfully!")
            print("-----  Thankyou for using our App -----")
        conn.close()
        return()
    print("Account linked with Email-id --- {} --- doesn't exist !".format(email))
    conn.close()
        

@app.command()
def checkloginstatus(email: str):
    conn = sqlite3.connect('Users_Details.db')
    data = conn.execute("SELECT name , EMAIL_ID, PASSWORD , LOGIN_STATUS from Login_Details where EMAIL_ID = ?",(email,))
    for i in data:
        conn.close()
        print("Login status "+str(i[3]))
        return(i[3])
    print("Account linked with Email-id --- {} ---- doesn't exist !".format(email))
    return(0)

@app.command()
def viewusers(email: str):
    # To check whether user is logged in we are collecting his email-id and verifying
    if checkloginstatus(email)==0:
        print("Signup/Login First!")
    else:
        conn = sqlite3.connect('Users_Details.db')
        cursor = conn.execute("SELECT name, EMAIL_ID, PASSWORD , LOGIN_STATUS from Login_Details")
        print("Name       Email-id              Password                        Login_Status")
        for row in cursor:
            print(row[0], end="     ")
            print(row[1], end="     ")
            print(row[2],end="      ")
            print(row[3])
        conn.close()

@app.command()
def changeusername(email: str,newname: str):
    if checkloginstatus(email)==0:
        print("Signup/Login First!")
    else:
        conn = sqlite3.connect('Users_Details.db')
        data = conn.execute("SELECT Name  from Login_Details where EMAIL_ID = ?",(email,))
        for i in data:
            oldname = i[0]
        if oldname == newname:
            print("Old and New user names are same!")
        else:
            conn.execute("UPDATE Login_Details set name = ? where EMAIL_ID = ?",(newname,email))
            print("Successfully Updated username!")
            conn.commit()
        conn.close()

@app.command()
def changeemailid(email: str,newemail: str):
    if checkloginstatus(email)==0:
        print("Signup/Login First!")
    else:
        if email == newemail:
            print("Old and New Emails are same!")
        else:
            conn = sqlite3.connect('Users_Details.db')
            conn.execute("UPDATE Login_Details set EMAIL_ID = ? where EMAIL_ID = ?",(newemail,email))
            print("Successfully Updated Email-id")
            conn.commit()
            conn.close()

@app.command()
def changepassword(email: str,newpassword: str):
    if checkloginstatus(email)==0:
        print("Signup/Login First!")
    else:
        conn = sqlite3.connect('Users_Details.db')
        data = conn.execute("SELECT PASSWORD  from Login_Details where EMAIL_ID = ?",(email,))
        for i in data:
            oldpassword = i[0]
        auth = newpassword.encode()
        auth_hash = hashlib.md5(auth).hexdigest()
        if auth_hash == oldpassword:
            print("Old and New passwords are same!")
            conn.close()
        else:
            conn.execute("UPDATE Login_Details set PASSWORD = ? where EMAIL_ID = ?",(auth_hash,email))
            print("Successfully Updated Password!")
            conn.commit()
            conn.close()

@app.command()
def deleteuser(email: str,password:str ):
    conn = sqlite3.connect('Users_Details.db')
    data = conn.execute("SELECT  PASSWORD , LOGIN_STATUS from Login_Details where EMAIL_ID = ?",(email,))
    for i in data:
        log_status = i[1]
        originalpassword = i[0]
        if log_status == 0:
            print("Signup/Login First!")
            conn.close()
            return()
        else:
            auth = password.encode()
            auth_hash = hashlib.md5(auth).hexdigest()
            if auth_hash == originalpassword:
                conn.execute("DELETE from Login_Details where Email_ID = ?",(email,))
                conn.commit()
                print("Successfully Deleted!")
                return()
            else:
                print("Incoreect password!")
                conn.close()
                return()
    print("Account linked with Email-id --- {}--- doesn't exist!".format(email))
    conn.close()     

# 1. Humidity
# 2. Pressure
# 3. Average temperature
# 4. Wind Speed
# 5. Wind degree
# 6. UV Index 


#Reference_API_Link1 = "https://openweathermap.org/api/one-call-api"
#Peferance_API_Link2 = "https://openweathermap.org/current"

@app.command()
def weatherreport(email: str,city: str): 
    if checkloginstatus(email)==0:
        print("Signup/Login First!")
    else:
        File = open("API_KEY.txt", "r")
        API_KEY = File.read().strip()

        cityname = city

        Api_link = "https://api.openweathermap.org/data/2.5/weather?q="+cityname+"&appid="+API_KEY

        Request_Api = requests.get(Api_link)
        Api_data = Request_Api.json()

        if Api_data['cod'] == '404':
            print("Invalild city {}, Please check your city name".format(cityname))
        else:
            coordinates = Api_data['coord']
            main = Api_data['main']
            wind = Api_data['wind']
        
            lat = coordinates['lat']
            long = coordinates['lon']
            humidity = main['humidity']
            pressure = main['pressure']
            min_temp = main['temp_min']
            max_temp = main['temp_max']
            average_temperature = (min_temp+max_temp)/2
            wind_speed = wind['speed']
            wind_degree = wind['deg']


            Api_link1 = "https://api.openweathermap.org/data/2.5/onecall?lat="+str(lat)+"&lon="+str(long)+"&exclude=hourly,daily&appid="+API_KEY

            Request_Api = requests.get(Api_link1)
            Api_data = Request_Api.json()
            uvi_index = Api_data['current']['uvi'] 

            print("----- Weather Report -----")
            print("Humidity: {} %".format(humidity))
            print("Pressure: {} hpa".format(pressure))
            # Kelvin to degrees coversion 1C = k=273.15
            print("Avg.Temperature: {:.1f} degrees".format(average_temperature-273.15))
            print("Wind_speed: {} m/s".format(wind_speed))
            print("Wind_degree: {} degrees".format(wind_degree))
            print("UV index: {}".format(uvi_index))                            


if __name__ == "__main__":
    app()