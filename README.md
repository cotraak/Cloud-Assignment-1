CLOUD ASSIGNMENT-1 (Feb 2019)

Deployed an application that generates the sum of first n natural numbers. Given a number the application that returns the sum of 1 to n given numbers. This application accepts inputs up to 1000000.

Launched Ubuntu-18.04-amd64-server-20180912 (ami-0f65671a86f061fcd) instance

Started the instance with existing .ppk key.

Installed apache webserver and mod_wsgi using the following steps:

$ sudo apt-get update $ sudo apt-get install apache2 $ sudo apt-get install libapache2-mod-wsgi

Installed Flask using the pip tool (which also needs to be installed). $ sudo apt-get install python-pip $ sudo pip install flask

Created a directory for Flask app. A directory is created in home directory, and linked it to the site-root defined in apache's configuration ( /etc/apache2/sites-enabled/000-default.conf).

$ mkdir ~/flaskapp $ sudo ln -sT ~/flaskapp /var/www/html/flaskapp

In flaskapp directory, put the files flaskapp.py, templates folder. In the templates folder, put sum.html file.

Created a .wsgi file to load the app.

Enabled mod_wsgi by modifying the apache configuration file located at /etc/apache2/sites-enabled/000-default.conf, the following block is added just after the DocumentRoot /var/www/html line:

WSGIDaemonProcess flaskapp threads=5
WSGIScriptAlias / /var/www/html/flaskapp/flaskapp.wsgi

<Directory flaskapp>
    WSGIProcessGroup flaskapp
    WSGIApplicationGroup %{GLOBAL}
    Order deny,allow
    Allow from all
</Directory>

The webserver is restarted using the following commands. $ sudo apachectl restart

The application is up and running at http://52.14.107.197

The public DNS is http://ec2-52-14-107-197.us-east-2.compute.amazonaws.com

REFERENCES: https://www.datasciencebytes.com/bytes/2015/02/24/running-a-flask-app-on-aws-ec2/
