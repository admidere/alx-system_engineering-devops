#!/usr/bin/env bash
# set up your client SSH configuration file

exec { 'ssh_config':
  path    => '/bin/',
  command => 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config'
}
