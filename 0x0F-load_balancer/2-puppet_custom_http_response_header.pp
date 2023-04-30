# Ensure the 'apt' module is installed
exec { 'install_apt_module':
  command => 'puppet module install puppetlabs-apt',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
  unless  => 'puppet module list | grep -q puppetlabs-apt',
}

# Update package lists
class { 'apt':
  update => {
    frequency => 'daily',
  },
  require => Exec['install_apt_module'],
}

# Install Nginx
class { 'nginx':
  manage_repo    => true,
  package_source => 'nginx-mainline',
  require        => Class['apt::update'],
}

# Configure Nginx with custom header
nginx::resource::server { 'default':
  listen_options => 'default_server',
  www_root       => '/var/www/html',
  index_files    => ['index.html'],
  use_default_location => false,
  locations      => {
    '/' => {
      location => '/',
      index_files => ['index.html'],
      custom_cfg => {
        'add_header' => 'X-Served-By $hostname',
      },
    },
  },
  require        => Class['nginx'],
}
