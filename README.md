[![Tools](http://img.shields.io/:python-v3-green.svg)](https://github.com/msfernandes/busine.me/wiki/Ferramentas)
[![Tools](http://img.shields.io/:django-v1.8.4-green.svg)](https://github.com/msfernandes/busine.me/wiki/Ferramentas)
[![Build Status](https://drone.io/github.com/msfernandes/busine.me/status.png)](https://drone.io/github.com/msfernandes/busine.me/latest)
[![Coverage Status](https://coveralls.io/repos/msfernandes/busine.me/badge.svg?branch=master&service=github)](https://coveralls.io/github/msfernandes/busine.me?branch=master)
[![Code Climate](https://codeclimate.com/github/msfernandes/busine.me/badges/gpa.svg)](https://codeclimate.com/github/msfernandes/busine.me)
[![License](http://img.shields.io/:license-gpl3-blue.svg)](https://github.com/msfernandes/busine.me/wiki/Licen%C3%A7a)

# Busine.me
---

For more information, see [Busine.me Wiki](https://github.com/msfernandes/busine.me/wiki)

### Setting up development environment

```
$ sudo apt-get install python3 python3-pip
$ sudo pip3 install -r requirements.txt
```

```
$ cp settings/databases settings/databases.py
$ cp settings/security settings/security.py
```

```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py makemigrations
$ python manage.py runserver
```
