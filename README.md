# Weather Forecasting  Command - Line Interface App

![Weather](https://pictures.brafton.com/x_0_0_0_14119699_800.jpg)

### Weather Forecasting Command-Line interface Application which helps users to Register , Login , Update account , Logout and  Check weather report of an given city .
## User Privilages

1. Signup
2. Login
3. Logout
4. Update Account
    * Change Username
    * Change Email-id
    * Change Password
5. Delete Account
6. Checking Weather report for a particular city
    * Humidity
    * Pressure
    * Average Temperature 
    * Wind speed
    * Wind Degrees
    * UV (Ultraviolet radiation) index




## API Reference

- API KEY is present in **API_KEY.txt** file.

**API-1**

```bash
  https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `City name` | `string` | **Required**. city name|
| `API key` | `string` | **Required**. API key |

**API-2**

```bash
  https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `lat, lon`      | `string` | **Required**. Geographical coordinates (latitude, longitude) |
| `Part` | `string` | **Optional**. By using this parameter you can exclude some parts of the weather data from the API response. It should be a comma-delimited list (without spaces). Available values:  current,minutely,hourly,dailyalerts.
| `API key` | `string` | **Required**.  API key | 


## Installation

- Windows   --> Git Bash
- Linux/Mac --> Terminal

**Clone the project** 

```bash
  git clone https://github.com/prakash200/CLI-APP.git
```

**Go to the project directory** 

```bash
  cd CLI-APP
```

**Activate Virtual Environment**

```bash
  source Cli-env/bin/activate
```
- Make sure you Install python, which automatically installs pip.

**Install dependencies**

```bash
  pip install -r requirements.txt
```

- Project installation Done.

## Project Demo



The below help command list out all the available app commands, which are functions in the App.

```bash
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py --help
Usage: app.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  changeemailid
  changepassword
  changeusername
  checkloginstatus
  createdatabase
  createtable
  deleteuser
  login
  logout
  signup
  viewusers
  weatherreport
```
- **I have already created database , Table and 3 sample users. If you want to skip then start with Step_2  else delete the Users_Details.db file and start from Step_1.**

## Step_1

- Create Database and Table by running following commands

- The below command creates database with the name **Users_Details.db**

```bash
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py createdatabase
Created Users_Details Database successfully!
```
- The below command creates table with the name **Login_Details**

```bash
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py createtable
created Login_Details Table successfully!
```
- Table consists of **username** , **Email-id** , **Password(hashed)** , **Login_status**

- Now the table is empty, so signup and create 3 users for our Demo.
- While signup user must enter password twice to confirm password.
- We are using Email-id of the user to track the login/signup status.  

```bash
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py signup user0 user0@gmail.com user0password user0password
You have registered successfully!
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py signup user1 user1@gmail.com user1password user1password
You have registered successfully!
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py signup user2 user2@gmail.com user2password user2password
You have registered successfully!
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ 
```
- Things taken care While User signup are:
   - User signing up with already existed Email-id **user2@gmail.com**.
   - password and confirm passwors are not same **(user3password,user2password)**.
- Below are the Examples

```bash
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py signup user3 user2@gmail.com user3password user3password
Email-id Already Exists!
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py signup user3 user3@gmail.com user3password user2password
Both Passwords doesnt match!
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py signup user3 user3@gmail.com user3password user3password
You have registered successfully!
```
- Below help command displays the Documentation of the command .

```bash
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py login --help
Usage: app.py login [OPTIONS] EMAIL PASSWORD

Arguments:
  EMAIL     [required]
  PASSWORD  [required]

Options:
  --help  Show this message and exit.
```

## Step_2

### Let's Login into the app as user0.
<br>

```bash
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py login user0@gmail.com user0password
Logged in Successfully!
Hi user0!
-----  Weleocome to Weather Forecasting App  -----
```
> ### Hurray! we have successfully logged into the App.
<br>

- Let's Read All the Users
- Login_status "1" implies user has logged in.

```bash
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py viewusers user0@gmail.com
Login status 1
Name       Email-id              Password                        Login_Status
user0     user0@gmail.com     11bf18b346fc29f1c47af18064a992ab      1
user1     user1@gmail.com     5ccafb277fa23cd0e71d99bc20715d9a      0
user2     user2@gmail.com     55b873945f78672333f33000075e7cde      0
user3     user3@gmail.com     cc17149e22e73f910c1f8d59a52228b7      0
```

- If user didn't login , he/she cannot use any privilages in the app.
- User1 didn't login and tries to Read all the users.

```bash
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py viewusers user1@gmail.com
Login status 0
Signup/Login First!
```
- User can check his login status

```bash
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py checkloginstatus user0@gmail.com
Login status 1
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py checkloginstatus user1@gmail.com
Login status 0
```

## Step_3

### Let's modify username , Email-id , password
<br>

```bash
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py changeusername user0@gmail.com USER0
Login status 1
Successfully Updated username!
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py changeemailid  user0@gmail.com USER0@GMAIL.COM 
Login status 1
Successfully Updated Email-id
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py changepassword  USER0@GMAIL.COM  USER0PASSWORD
Login status 1
Successfully Updated Password!
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py viewusers  USER0@GMAIL.COM  
Login status 1
Name       Email-id              Password                        Login_Status
USER0     USER0@GMAIL.COM     1d367d80b05887be3e14b8232a2ae87d      1
user1     user1@gmail.com     5ccafb277fa23cd0e71d99bc20715d9a      0
user2     user2@gmail.com     55b873945f78672333f33000075e7cde      0
user3     user3@gmail.com     cc17149e22e73f910c1f8d59a52228b7      0
```
- Updates : 
   - **user0 --> USER0** 
   - **user0@gmail.com --> USER0@GMAIL.COM**
   - **user0password -->USER0PASSWORD .**

- Old and new credentials cannot be same while updation. Below is the scenario .

```bash
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py changeusername USER0@GMAIL.COM USER0
Login status 1
Old and New user names are same!
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py changeemailid USER0@GMAIL.COM USER0@GMAIL.COM
Login status 1
Old and New Emails are same!
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py changepassword USER0@GMAIL.COM USER0PASSWORD
Login status 1
Old and New passwords are same!
```
- Lets Delete **USER0**

```bash
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py deleteuser  USER0@GMAIL.COM USER0PASSWORD
Successfully Deleted!
```
- Let's login in app with **user1** and check users.

```bash
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py login user1@gmail.com user1password
Logged in Successfully!
Hi user1!
-----  Weleocome to Weather Forecasting  -----
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py viewusers user1@gmail.com 
Login status 1
Name       Email-id              Password                        Login_Status
user1     user1@gmail.com     5ccafb277fa23cd0e71d99bc20715d9a      1
user2     user2@gmail.com     55b873945f78672333f33000075e7cde      0
user3     user3@gmail.com     cc17149e22e73f910c1f8d59a52228b7      0
```
- **USER0** successfully deleted his account .

## Step_4

### Checking Weather reportof the cities
- Check the city name before entering .
- Below Weather report generated on **Jun 18 5:20 PM**

```bash
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py weatherreport user1@gmail.com hyderabad
Login status 1
----- Weather Report -----
Humidity: 55 %
Pressure: 1006 hpa
Avg.Temperature: 34.0 degrees
Wind_speed: 5.66 m/s
Wind_degree: 170 degrees
UV index: 0.19
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py weatherreport user1@gmail.com Bengaluru
Login status 1
----- Weather Report -----
Humidity: 68 %
Pressure: 928 hpa
Avg.Temperature: 28.0 degrees
Wind_speed: 1.54 m/s
Wind_degree: 170 degrees
UV index: 0.62
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py weatherreport user1@gmail.com Delhi
Login status 1
----- Weather Report -----
Humidity: 62 %
Pressure: 1001 hpa
Avg.Temperature: 32.0 degrees
Wind_speed: 2.57 m/s
Wind_degree: 350 degrees
UV index: 0.84
```

## Step_5

### Logout account

```bash
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py logout user1@gmail.com
Logged out Successfully!
-----  Thankyou for using our App -----
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python app.py checkloginstatus user1@gmail.com
Login status 0
```

**Note** : If user don't logout from the app , it will not be logged out automatically. But when he/she is trying to login next time it tells that **Already Logged in** .

## Author 
###  Prakash Kalari

# ------------------------  **Thank you**  -----------------------
