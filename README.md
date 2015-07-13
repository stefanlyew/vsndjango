# vsndjango

### Requirements

python 2.7.10
```
Django==1.8.3
MySQL-python==1.2.5
wheel==0.24.0
```

## Installation

### 1. virtualenv
Create a virtualenv for your own project, where `vsndjango` is the name of your project:

`$ mkvirtualenv --clear vsndjango`

### 2. Download
Now, you need the vsndjango project files in your workspace:

    $ cd /path/to/your/workspace
    $ git clone git://github.com/stefanlyew/vsndjango.git && cd vsndjango

### 3. Requirements

`$ pip install -r requirements.txt`

#### Initialize the database
Make sure you have created a database in MySQL's interactive prompt:
$ mysql.server start
$ mysql -u root -p
Enter password:

mysql> CREATE DATABASE vsndjango_development
Query OK, 1 row affected (0.01 sec)
mysql> quit

Make sure that these steps match with the configuration in /vsndjango/settings.py

python manage.py syncdb
python manage.py runserver

### Ready? Go!
`./manage.py import`
`./manage.py runserver`
