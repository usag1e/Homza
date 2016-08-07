#Homza

## Dependencies

#### Python packages

* `couchdbkit`
* `restkit`
* `Resource`
* `python-dateutil`
* `couchdb`
* `pydash`
* `python-nmap`
* `xmltodict`

#### Apt-get

* `mplayer`
* `nmap`
* `couchdb`
* `python-dev`
* `libyaml-dev`

##Important

Check line 24 in **network_scanner** and change the *X* in *192.168.X.0/24* by 0 or 1 depending of your network.

### The view is needed to have people displayed !

`python views.py`

if that command doesn't work, check if you have an admin set up on Couchdb and if yes, that `COUCHDB_USERNAME` and `COUCHDB_PASSWORD` are set in environment
