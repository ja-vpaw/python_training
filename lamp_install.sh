#!/bin/sh

#install LAMP och PHPmyAdmin - testat i Mint 18.1 (lamp och mysql kommer att starta automatiskt vid boot)
tput setaf 7 &&
sudo apt-get install apache2 &&
sudo apt-get install libapache2-mod-php &&
sudo a2enmod rewrite &&
sudo apt-get install php-xdebug &&
echo "" &&
tput setaf 190; echo "Now, find <Directory /var/www/> and set AllowOverride to All \
  (otherwise, changing permalinks will break the site). Also, if your web files are \
  on a data partition the corresponding <Directory> block needs to be created for that location." &&
sudo xed /etc/apache2/apache2.conf &&
tput setaf 7; sudo /etc/init.d/apache2 restart &&

#verify apache2 and php installation
sudo sh -c 'echo "<?php phpinfo() ?>" > /var/www/html/phpinfo.php' &&
xdg-open http://localhost/phpinfo.php &&

#mysql and phpmyadmin
sudo apt-get install mysql-server &&
sudo apt-get install mysql-client &&
sudo apt-get install php7.0-mysql php7.0-curl php7.0-json &&
sudo apt-get install phpmyadmin &&

#increase php upload size (for Wordpress)
tput setaf 190; echo "Now set 32M for upload_max_filesize och post_max_size" &&
sudo xed /etc/php/7.0/apache2/php.ini &&
tput setaf 7; sudo service apache2 restart &&

#just testing...
echo "" &&
tput setaf 190; echo "Print PHP version and MySQL status..." &&
tput setaf 7; php -v &&
sudo systemctl status mysql &&

#verify that phpmyadmin works
xdg-open http://localhost/phpmyadmin &&

#SET PROPER PERMISSIONS - only works if '$USER' is current username
#sets the group owndership of all files in /var/www to "www-data" recursively
sudo chown -R www-data: /var/www &&
#allows everyone (including apache) to read all files in /var/www
sudo chmod -R o+r /var/www &&
#allows group members to write to all files in /var/www
sudo chmod -R g+w /var/www &&
#sets new files to retain the group of the directory they are created in
sudo find /var/www -type d -exec chmod g+s {} \; &&
#add user '$USER' to www-data
sudo usermod -a -G www-data $USER &&
tput setaf 190; echo "Setting proper permissions for /var/www/" &&
echo "User $USER has now joined group www-data. Log out and in again for permissions \
  to take effect. N.B. if the user to join www-data was someone else, do it manually \
  or adapt script. Furthermore, if using a symlinked data partition for web files,\
  the permissions commands from the script need to be issued manually for the data partition as well."
