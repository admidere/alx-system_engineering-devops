#!/usr/bin/env bash
# configure previous file using puppet

file { '/etc/ssh/ssh_config':
  ensure => file,
  mode   => '0644',
  content => "Host web-01\n
              HostName 18.207.2.134\n
              User ubuntu\n
              IdentityFile ~/.ssh/school\n
              PasswordAuthentication no\n",
}
