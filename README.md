# A simple library API
This is a simple library API where you can do CRUD operations for book categories and books.

# How to start
## Install reqirments and virtual env
First create a virtual env for the project.
```python
python -m venv DIR
```

Later activate the virtual env and install the requirments for the project.
```python
pip install -r requirments.txt
```

## Create a SECRET_KEY for the project
You should either create a dotenv or edit ```library_project/settings.py``` and change the ```SECRET_KEY```

To create a new ```SECRET_KEY``` you can use python shell:
```python
from django.core.management.utils import  get_random_secret_key
get_random_secret_key()
```
You can copy the output value and apply it in dotenv file or into ```settings.py```

## Using runserver(Debug/Local)
Make sure you are in the same DIR as ```manage.py``` and have activeted virtual env.
Since there isn't a database yet you should makemigrations and migrate first.
```cmd
python manage.py makemigrations
python manage.py migrate
```

From there you can use:
```cmd
python manage.py runserver
```
You can pres ```CONTROL+C``` to interrupt the runserver

For creating a superuser:
```cmd
python manage.py createsuperuser
```
Also you can see available commands in:
```
python manage.py
```

## Usage and URLs
```localhost:8000``` is the default adress

```/books/``` for Book list. The GET result has pagination with 50 items per page. the results are in the ```result``` key of the json. 
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "Example",
            "pub_date": "YYYY-MM-DD",
            "author": "Example",
            "description": "Example",
            "category": [
                1
            ]
        }
    ]
}
```
POST will create a new book.(You have to be logged as superuser)
```json
{
"title":"Example",
"pub_date":"YYYY-MM-DD",
"author":"Example",
"description":"Example",
"category":[CATEGORY_ID]
}
````

```/books/id/``` for the CRUD of the ```id item```

```/categories/``` for Categories CRUD. Same as ```/books/``` 

```/search/``` search for books from ```/search/?category=NUMBER``` , ```/search/?title=TEXT```  and ```/search/?author=TEXT``` . You can chain them with ```&```
Example:

```/search/?category=1&title=example```

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "Example",
            "pub_date": "YYYY-MM-DD",
            "author": "Example",
            "description": "Example",
            "category": [
                1
            ]
        }
    ]
}
```


```/api_auth/login/``` is for login to API. 

You will need to first make a ```GET``` request  and get the ```csrftoken``` added into Headers as ```X-CSRFToken``` . 

## Used in project
Django RESTFramework -> https://www.django-rest-framework.org/

Django -> https://www.djangoproject.com/

Python-dotenv

Versions
```
asgiref==3.6.0
Django==4.1.7
djangorestframework==3.14.0
python-dotenv==1.0.0
pytz==2023.2
sqlparse==0.4.3
```

# .
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
