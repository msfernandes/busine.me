<a href="https://zenhub.io"><img src="https://raw.githubusercontent.com/ZenHubIO/support/master/zenhub-badge.png"></a>

[ ![Codeship Status for msfernandes/busine.me](https://codeship.com/projects/287d5980-27f7-0133-10e3-3ef19dc5f2fb/status?branch=master)](https://codeship.com/projects/97544)

[![Tools](http://img.shields.io/:python-v3-green.svg)](https://github.com/msfernandes/busine.me/wiki/Ferramentas)
[![Tools](http://img.shields.io/:django-v1.8.4-green.svg)](https://github.com/msfernandes/busine.me/wiki/Ferramentas)
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
### Population databases

```
$ python3 manage.py shell
$ from importer.parser import Parser
$ p = Parser()
$ p.import_data()
```
