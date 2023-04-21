# Kills a process named "killmenow"
exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => ['/usr/bin', '/bin', '/usr/local/bin'],
  onlyif      => 'pgrep killmenow',
}
