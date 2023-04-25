# Install and configure Nginx web server using puppet

exec { 'install_nginx':
  command => 'apt-get update && apt-get install -y nginx',
  unless  => 'which nginx',
}

exec { 'create_index_file':
  command => 'echo "Hello World!" > /var/www/html/index.html',
  require => Exec['install_nginx'],
}

exec { 'create_redirect':
  command => 'echo "server { listen 80 default_server; listen [::]:80 default_server; server_name _; return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4$request_uri; }" > /etc/nginx/sites-available/default',
  require => Exec['install_nginx'],
}

exec { 'enable_redirect':
  command => 'ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/',
  require => Exec['create_redirect'],
}

service { 'nginx':
  ensure => running,
  enable => true,
  require => [Exec['create_index_file'], Exec['enable_redirect']],
}
