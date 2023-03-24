# excuting my manifest
exec { 'killmenow':
  command   => 'pkill killmenow',
  onlyif    => 'pgrep killmenow',
  provider  => 'shell',
  logoutput => true,
}
