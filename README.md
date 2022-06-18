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

#### API-1

```http
  https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `City name` | `string` | **Required**. city name|
| `API key` | `string` | **Required**. API key |

#### API-2

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

** Clone the project 

```bash
  git clone https://github.com/prakash200/CLI-APP.git
```

** Go to the project directory 

```bash
  cd CLI-APP
```
** Activate Virtual Environment

```bash
  source Cli-env/bin/activate
```

** Install dependencies

```bash
  pip install requirements.txt
```

- Project installation Done.

## Run Locally

```bash
  python3 app.py --help
```

** The above help command list all the available app commands, which are functions in a App .

