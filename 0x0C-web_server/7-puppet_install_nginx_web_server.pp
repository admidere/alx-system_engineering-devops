# Install and configure Nginx web server using puppet

# update apt packages
exec { 'update packages':
  command => '/usr/bin/apt-get update',
}

# Install Nginx package
package { 'install nginx':
  ensure => installed,
}

# Create configuration file
file { '/var/www/index.html':
  content => 'Hello World!'
}

# redirect
exec {'redirect_me':
  command  => 'sed -i "24i\	rewrite ^/redirect_me  https://www.youtube.com/watch?v=QH2-TGUlwu4/;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

# create symbolic link to enable the virtual host
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
}

#Restart the Nginx service
service { 'nginx':
  ensure  => running
}
