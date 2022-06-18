# Weather Forecasting  Command - Line Interface App

![Weather](https://pictures.brafton.com/x_0_0_0_14119699_800.jpg)

Weather Forecasting Command-Line interface Application which helps users to 
check the weather report for a given city .

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

- API KEY is present in API_KEY.txt file.

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

**Install dependencies**

```bash
  pip install requirements.txt
```

- Project installation Done.

## Project Demo



The below help command list out all the available app commands, which are functions in the App.

```bash
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python3 app.py --help
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

- Create Database and Table by running following commands

- The below command creates database with the name **Users_Details.db**

```bash
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python3 app.py createdatabase
Created Users_Details Database successfully!
```
- The below command creates table with the name **Login_Details**

```bash
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python3 app.py createtable
created Login_Details Table successfully!
```
- Now the table is empty, so signup and create 3 users
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

```bash
(Cli-env) prakash@PKC:~/Documents/CLI_app/CLI-APP$ python3 app.py login user0@gmail.com user0password
Logged in Successfully!
Hi user0!
-----  Weleocome to our App  -----
```



