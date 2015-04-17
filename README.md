#Metricboard Server


### Setup Local Environment

##### Setup virtualenv

```
# install virtualenv if you don't have it.
$ sudo easy_install virtualenv virtualenvwrapper
$ echo "source /usr/local/bin/virtualenvwrapper_lazy.sh" >> ~/.bash_profile
$ source ~/.bash_profile

# setup
$ mkvirtualenv mtc
$ workon mtc
$ pip install -r requirements.txt

# you can disable current virtualenv by run
$ deactivate
```

##### Setup database

Edit `db/reset_db.sh` then run it.

##### Custom config

```
$ touch config/config.py
```
then you can overwrite any variables you want.

### Run Web Server

```
$ python server.py -h
$ python server.py
```
