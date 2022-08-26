# Django Bug Tracker Website

A project that allows users and developers to track bugs in various projects. 

**Demo Link - [Here](https://django-bug-tracker-99.herokuapp.com/)**
![bug_tracker_showcase](https://i.imgur.com/vXvhhcg.png)

## Technologies Used 

* [Django](https://www.djangoproject.com/) - The Python framework used to create the backend.
* [PostgreSQL](https://www.postgresql.org/) - Database used to save all of the website's data. 
* [Bootstrap 5](https://getbootstrap.com/) - CSS framework used to style the frontend. 
* [Python](https://www.python.org/) - Backend language 
* HTML
* CSS

## Features
* Login system - Users must log in with a username and password to create projects, tickets, and comments. 
* Roles - Users can be assigned the developer role which grants access to extra features and permissions. 
* Projects - Users can create projects with a title and description. Project creator and developers can edit and delete projects. 
* Tickets - In each project, tickets can be created with tags that show their level of importance. Tickets may be assigned to any number of developers, who can edit, delete, or mark the ticket as resolved. 
* Resolved Tickets - Tickets that are marked as resolved by a developer will be displayed in their own group separate from unresolved tickets. 
* Comments - Users and developers can leave comments on tickets. Comment owners and developers can edit and delete comments. 
* Profile Page - Every user and developer has a profile page that displays all tickets created and comments posted by that user. 
* Ticket Overview - Displays all tickets created, grouped based on if they have been assigned to a developer. 
* Ticket Search - Search for tickets in projects by author name, ticket title, ticket description, or tags.


## Installation 

    # Clone the repository
    $ git clone https://github.com/wbrandon25/Django-Bug-Tracker
    
    # Navigate to directory
    $ cd .\Django-Bug-Tracker  
   
    # Create a virtual environment and activate it 
    $ virtualenv env
    $ .\env\Scripts\activate
    
    # Install requirements 
    $ pip install -r requirements.txt
    
    # Create migrations and migrate into database
    $ python manage.py makemigrations
    $ python manage.py migrate
  
    # Create a superuser 
    $ python manage.py createsuperuser
    
    # Start development server (localhost:8000)
    $ python manage.py runserver
   
 * To create tags, login at localhost:8000/admin as superuser, select the Tags model, and click add Tag. 
 * The default database is sqlite3. To use PostgreSQL, change the database settings in bugTrackerWebsite/settings.py and add your environment variables 

```
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}
```
