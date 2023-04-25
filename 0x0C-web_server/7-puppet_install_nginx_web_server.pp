# Install and configure Nginx web server using puppet

class nginx_server {
  package { 'nginx':
    ensure => 'installed',
  }

  service { 'nginx':
    ensure => 'running',
    enable => true,
    require => Package['nginx'],
  }

  file { '/var/www/html/index.html':
    content => 'Hello World!',
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-available/default':
    content => "server {
      listen 80 default_server;
      listen [::]:80 default_server;
      server_name _;
      return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4$request_uri;
    }",
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-enabled/redirect':
    ensure => 'link',
    target => '/etc/nginx/sites-available/default',
    require => File['/etc/nginx/sites-available/default'],
  }
}

include nginx_server
