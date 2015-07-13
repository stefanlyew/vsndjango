# vsndjango

### Requirements

`python 2.7.10`
`Django==1.8.3`
`MySQL-python==1.2.5`
`wheel==0.24.0`

## Installation

### 1. virtualenv
Create a virtualenv for your own project with virtualenvwrapper, where `vsndjango` is the name of your project:

`$ mkvirtualenv --clear vsndjango`

### 2. Download
Now, you need the vsndjango project files in your workspace:

    $ cd /path/to/your/workspace
    $ git clone git://github.com/stefanlyew/vsndjango.git && cd vsndjango

### 3. Requirements

`$ pip install -r requirements.txt`

#### 4. Create the database
Make sure you have created a database in MySQL's interactive prompt:

`$ mysql.server start`
`$ mysql -u root -p`
`Enter password:`

`mysql> CREATE DATABASE vsndjango_development`
`Query OK, 1 row affected (0.01 sec)``
`mysql> quit`

Make sure that these steps match for your configuration in /vsndjango/settings.py!

#### 5. Setup the database
`./manage.py syncdb`

The Import Command Parses the CSV file vsn_data.csv and seeds the database with
Vehicle Records from it
`./manage.py import`

### 6. Ready? Go!
`./manage.py runserver`

### Known Issues
If you are receiving and error on "./manage.py import":
this is probably because of carriage return differences between unix and mac
please make sure to convert CRLF to LF for the file vsn_data.csv

### Areas for improvement, ideas for version 2, etc.

Would like to have test coverage for this project, but am new to python
ecosystem and have much to learn.

The VSN number applied to each vehicle by each manufacturer will be in a variety
of different formats.  We will need to extend the VSNDataParser into classes
that can handle each manufacturer separately.  Different VSN's mean different
things to each manufacturer.


