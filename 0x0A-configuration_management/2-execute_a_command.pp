# This manifest kills a process named "killmenow" using the pkill command
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin:/bin:/usr/sbin:/sbin',
  onlyif  => 'pgrep killmenow',
}
