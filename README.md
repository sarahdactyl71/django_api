# Contact API

### Requirements
1. Python Version

### Running the Server
1. clone this repository
2. navigate to the inner `django_api` folder, `cd django_api`
3. run `python manage.py runserver`

### List of Endpoints
1. api_index path: `http://localhost:8000/contact_api/api_index`
2. api_show path: `http://localhost:8000/contact_api/api_show`
3. api_post path: `http://localhost:8000/contact_api/api_post` This endpoint requires a body to be sent in with request.
4. api_edit path: `http://localhost:8000/contact_api/api_edit` This endpoint requires a body to be sent in with request.
5. api_delete path: `http://localhost:8000/contact_api/api_delete` This endpoint requires a body to be sent in with request.
6. api_list path: `http://localhost:8000/contact_api/api_list` This endpoint requires a body to be sent in with request.

To access some of the endpoints you must be a logged in, authenticated user.

### Testing Endpoints
I used Postman to test any endpoints that updated information.
Often there will be a body to the request and it should be formatted like so:

```
{
	"key": "value",
	"key": "value"
}
```

![Alt text](postman_screenshot.png?raw=true "Postman Screenshot")

For authenticating a user for endpoints that modify data, pass key values pairs into the header of the request like you see pictured below.

`username: finnthehuman`

`password: password`
![Alt text](postman_screenshot.png?raw=true "Postman Screenshot")

### Other App Functionality
Navigate to `http://localhost:8000/contact_api/` to check out the site, and `http://localhost:8000/accounts/login` to login and become an authenticated user.

There is also some basic CRUD functionality within this app. Contacts can be created, retrieved, updated, and destroyed from the users end.

Users can also login and logout, but a user must be created in the python shell.

```
from django.contrib.auth.models import User

user = User.objects.create_user('username', 'genericemail@gmail.com', 'mypassword')

user.first_name = 'Finn'
user.last_name = 'Martin'
user.save()
```
