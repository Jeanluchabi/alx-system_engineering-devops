file { '/home/luc/.ssh/config':
  ensure  => present,
  content => "
    Host remote_server
      HostName 443297-web-01
      User luc
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
  owner   => 'luc',
  group   => 'luc',
  mode    => '0600',
}

