### Run in order

`git clone https://github.com/DocTheDJ/homework.git`

`cd homework`

`python3 -m venv env`

Linux: `source env/bin/activate`

Windows: `.\env\Scripts\activate`

`pip install -r requirements.txt`

`python3 manage.py migrate`

`python3 manage.py runserver`

at this point the server should be accessible through your browser on the address and port which it says in your console

when you click on it it should open your default browser and it will send you to a "Page not found", do not worry, it is to be expected, there is no root path view defined

you should see possible paths on the page

- admin/
    > path to the default admin pages in django
- import/
    > path where you can paste your JSON input

    > pass the JSON into the content field in the page, files are NOT supported, yet
- models/
    > path which will give you possible names of tables to be used as parameters
- detail/<str:name>/
    > path which will return all rows from the named table

    > if the name is not known it will show possible names
- detail/<str:name>/<int:id>
    > path to return one row from table which is named and its id is passed

for both details only the surface value in the table is returned no joins have been implemented in the serializers, rather easy to make so i did not bother at this time

to kill the server just use CTRL + C in the terminal where it was started

to exit env type: `deactivate`
