# Install Nginx
class { 'nginx': }

# Add custom header X-Served-By with the server's hostname
nginx::config::vhost { 'default':
  ensure => present,
  content => template('nginx/default.conf.erb'),
}

file { '/etc/nginx/default.conf':
  ensure => present,
  content => template('nginx/default.conf.erb'),
  notify => Service['nginx'],
}

# Define custom fact for the server's hostname
Facter.add('server_hostname') do
  setcode do
    Facter::Core::Execution.execute('hostname')
  end
end

# Add custom header to Nginx configuration
nginx::resource::server_header { 'X-Served-By':
  value => $::server_hostname,
}
