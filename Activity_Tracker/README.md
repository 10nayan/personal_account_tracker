# Personal Account Tracker using Django    

## Introduction
This application is built with Django which is a python framework for web development.
This application has basic features of view,create,edit and delete money spent on personal activities. The money spent on various activities can be categorised with date and type of spent later.
## Files in the project
- **/pat/views.py**: This is the app file that contains the logic of all the view functions in the backend which generate dynamic contents to HTML template.
- **/pat/models.py**: Contains Django models used for storing activity data.
- **/pat/forms.py**: python app file  required for creating form in this appliation.
- **/pat/urls.py**: python app file  required for url mapping to all the view functions.
- **/pat/admin.py**: python app file  required for registering to django-administration of this appliation.
- **/pat/tests.py**: python app file  required for testing of this appliation.
- **/pat/apps.py**: python app file  required for registering the pat app to django main project of this appliation.
- **/personal_account_tracker/**: python main project folder in which pat app is created.
- **pat/templates/**: folder with all HTML files
- **pat/static/**: for all JS scripts and CSS files
## Usage
### Clone/Modify app
1. Modify personal_account_tracker folder or create a new app in the main personal_account_tracker project folder.

    For modifying existance code or creating new app, These lines need to be edited in personal_account_tracker/settings.py are shown below:
```python
SECRET_KEY ='<your secret key>'
ALLOWED_HOSTS = ['<your allowed host>']
DATABASES = {<your database settings>}
```
2. Run makemigrations and migrate command from the terminal to create the table with the link to your database.

3. Run createsuperuser command to register to django admin panel.

4. Create new app in personal_account_tracker project folder using following command,
    
```console
C:\<path to personal_account_tracker>\python manage.py startapp <your app name>
```
## Areas of improvement
1. More functionality can be added to the application such as graph representation of spent type or date, monthly money spent report and linked to google  sheet that a user can download all the data.
2. Style of this website can be improved to another level, I have written very less CSS, most of the time I used bootstrap template.
3. Frontend user experience can be improved by using javascript framework or vanilla javascript.