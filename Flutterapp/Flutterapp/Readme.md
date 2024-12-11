## Django Framework
**Commands**
1. python --version
2. python -m venv [project-name]
3. [project-name]\Scripts\activate
4. python -m pip install Django==5.1.3
5. Djnago-admin --version
6. Django-admin startproject [project-name/app-name]
7. python manage.py runserver.
## What is a View in Django?
1. A function that takes a request and sents a response. 
2. A request handler.
3. In some frameworks itds called action but in django its called a view.
## How to map the URLs from appplication to the Project.
- Create a module named as urls.py in your application folder.
  ```python
  from django.urls import path
  from . import views
  # URL Configuration
  urlpatterns = [
    path('hello/', views.say_hello)
   ]
   # So far we have created a url  for  our applications in this view module.
  ```
- After creating a url we have to map this in our project folder
```Python
 from django.contrib import admin
 from django.urls import path, include
 urlpatterns = [
    path('admin/', admin.site.urls),
    path('Flutterapplication/',include('Flutterapplication.urls'))
    ] 
```
- third

