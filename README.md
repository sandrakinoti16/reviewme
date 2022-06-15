# reviewme
## Description
This application will allow a user to post a project he/she has created and get it reviewed by his/her peers.

## Screenshots 
###### Home page
![Screenshot from 2022-06-15 13-07-37](https://user-images.githubusercontent.com/99794154/173820273-256e53c7-4140-46fe-a10a-d83efbbf9680.png)
###### Rating of a post
![Screenshot from 2022-06-14 12-52-12](https://user-images.githubusercontent.com/99794154/173820470-48ad45a2-350a-49fa-bff7-460960052b03.png)

 
## User Story  
  
* A user can view posted projects and their details.  
* A user can post a project to be rated/reviewed. 
* A user can rate/ review other users' projects.  
* Search for projects.  
* View projects overall score.
* A user can view their profile page.  
  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/sandrakinoti16/reviewme 
```
##### Navigate into the folder and install requirements  
 ```bash 
cd reviewme pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations reviewdeck
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
 
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 4.0](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but if you notice any kindly contact me with the email below 
  
## Contact Information   
If you have any question or contributions, please email me at [sandrakinya6@gmail.com]  
  
## License 
* *MIT License:*
* Copyright (c) 2022 **Sandra Kinoti**
