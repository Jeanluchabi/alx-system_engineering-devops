# Puppet Manifest to create a file in /tmp called "school" with specific permissions, owner, and group.

file { '/tmp/school':
  ensure  => file,           
  mode    => '0744',      
  owner   => 'www-data',      
  group   => 'www-data',      
  content => "I love Puppet\n",  
}

