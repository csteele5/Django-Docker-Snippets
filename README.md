# Django on Docker Snippets

## Summary

This is a repository building up a functioning Django/Python simple website, with basic database connectivity and data management.  This will start with a partially populated sql lite database, migrating to PostgreSQL and will include many sample functions. 

## Deployment

This project is initially setup with manual steps that must be run to set up the Django environment and application after the docker containers (web and postgres) are launched.  The plan will be to migrate this to complete automation.  We'll see how that goes.

**Steps from Tutorial (see reference below)**
Create project directory
Create Dockerfile, requirements.txt, docker-compose.yml
Run the following: 
```
sudo docker-compose run web django-admin startproject composeexample .
sudo chown -R $USER:$USER .
```

Update the settings.py per the documentation to connect to the database.  This replaces the sqllite connection with postgres in the adjacent container

Bring the image back up:
`docker-compose up`

To run multiple commands in the web image, replace the command statement in the yml file with this:
	```
    #command: python manage.py runserver 0.0.0.0:8000
    context: .
    command: >
        sh -c "python manage.py wait_for_db &&
               python manage.py migrate &&
               python manage.py runserver 0.0.0.0:8000"
    ```

To manually create superuser:
`sudo docker-compose run web python manage.py createsuperuser`

# Setting up Base Django Project

Delete the django project directory (composeexample or whatever)
Delete the sqllite and manage.py file

Now we start over:
Start a new project where your existing project files will be placed.
This may be set up as a volume as well as a source (let's see).  But first, a simple source.
```
docker-compose up --build   (web will close automatically)
sudo docker-compose run web django-admin startproject djangosnippets .
```

Now run 'docker-compose up' again.  This will create the sqllite file.  
NOTE: we are not running on postgres yet!  This is just to verify the project will run from the original tutorial
`sudo chown -R $USER:$USER .`

At this point, we can copy over the project files and rerun docker-compose, with or without the original sqllite file.  If we do without, we need to make superuser (osboxes).  Either way, we should makemigrations


Now that the app runs on sqllite, try switching over to postgres.  It will be a blank database at first, but should function.
Edit settings.py with new database info: 

``` 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```

**ERROR RUNNING PORTED APP**
The price field in the products model was not accepted by postgres.  I tried to update the model, but it didn't seem to matter.  The problem was the old migrations in the migrations folders.  I did update those, but I could also delete them.


SUCCESS!
Site is up and running with empty database.
Create Super User and see if all pages function (except the raw view pages.  these did not work with sqllite)

**Lingering error with creating classview entry**
```
web_1  | Quit the server with CONTROL-C.
web_1  | [30/Jun/2020 22:48:51] "GET /classview/create/ HTTP/1.1" 200 1503
web_1  | FORM NOT SAVED
web_1  | [30/Jun/2020 22:48:56] "POST /classview/create/ HTTP/1.1" 200 1503
```


## Reference Material

**[Django Tutorial](https://www.youtube.com/watch?v=F5mRW0jo-U4)**

- 1:15 Installing. Virtual environment
- 18:54 Set up code text editor
- 22:27 Django settings
- 29:48 Built-In components
- 46:22 New model fields
- 59:27 Custom homepage
- 1:04:08 URL routing
- 1:16:50 Django templating engine basics
- 1:23:59 Include template tag
- 1:49:09 Render data from the database with a model
- 2:06:50 Django model forms
- 2:35:33 Form widgets
- 2:41:29 Form validation methods
- 2:48:59 Initial values for forms
- 3:00:00 Dynamic linking of URLs
- 3:03:10 In app URLs and Namespacing
- 3:15:42 Class based views – CreateView

**[Docker Setup Steps](https://docs.docker.com/compose/django/)**

**[Dockerize Django App](https://www.youtube.com/watch?v=90LCcim-wHQ)**

