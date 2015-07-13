# Homza

# testing_nmap.py
You will need to first do:

````
sudo apt-get install nmap
sudo pip install python-nmap
````

You can then:
````
sudo python testing_nmap.py
````
Or run the current script:
````
sudo python whos_up.py
````
The code is fully commented.

# Installing couchdb
````
sudo apt-get install couchdb
sudo pip install couchdb
````
# Try the website
````
sudo apt-get update
sudo apt-get upgrade
sudo apt-get -y install apache2 
sudo apt-get -y install php5 libapache2-mod-php5 php5-mcrypt
````
Then go to the folder /php_homza and:
````
./deploy
````
Open your favorite browser, go to 127.0.0.1

# How to run a program in background
If you wish to run a program in background, you have to end the command with "&".
````
script.py &
````
If you want to continue this job after you log out from your terminal, you can prefix with nohup
````
nohup script.py &
````
# How to allow your Apache server work on raspberry (to process php files)

You'll need to install PHP5 and the PHP5 module for Apache. Type the following command to install these:
````
sudo apt-get install php5 libapache2-mod-php5 -y
````
Now remove the index.html file:
````
sudo rm index.html
````
and create the file index.php:
````
sudo nano index.php
````
# How to screen

SSH connect the RPi, then:
````
screen
````
You are now inscide a screen, even if the SSh connection to the RPi is broken, you can reconnect to the RPi, and type:
````
screen -r
````
You will be able to check the running screens, and if several are running you will need to type:
````
screen -r  [screen name displayed after screen -r]
````
Example:
````
screen -r  31844.pts-0.office
````

#Dependencies
```
sudo pip install xmltodict
```


