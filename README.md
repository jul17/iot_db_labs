﻿# iot_db_labs

To run REST service:
```
$ .\app.py
```
> Test if app is running in normal way
> ```
> in postman : Get http://127.0.0.1:8000/test
> ```
> You should get "ok" in response


In file app.config:

- change your credentials to Azure Event Hub, Redis Cashe
- in mode section choose the mode where data would be viewed (cli or event_hub)

> - Go to http://127.0.0.1:8000 in PostMen
> - Create method get with url: http://127.0.0.1:8000/<your url to file>
> - in my case I use : http://127.0.0.1:8000/files/https://data.kyivcity.gov.ua/system/files/expenses.csv


Tips:
- reading logic from file in  manager/implementation/file_manager.py
- a record in the Event Hub in view_data_interfaces/implementation/view_data_event_hub.py
- a record in cli(command line interface) in view_data_interfaces/implementation/view_data_cli.py



