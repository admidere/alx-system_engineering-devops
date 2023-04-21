# Kills a process named "killmenow"
exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => '/usr/bin/pkill -f killmenow',
  onlyif      => 'pgrep killmenow',
}
