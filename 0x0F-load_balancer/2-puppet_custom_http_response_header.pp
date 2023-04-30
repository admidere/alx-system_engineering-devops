# Ensure the 'apt' module is installed
exec {'Custom HTTP header':
  command  => 'sudo apt-get update;
    sudo apt-get -y install nginx;
    sudo sed -i "/Default server configuration/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
    sudo service nginx restart',
  provider => shell,
}
