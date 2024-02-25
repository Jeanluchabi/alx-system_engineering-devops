#!/usr/bin/env bash
# The script for my client SSh config to connect
# to a server without typing a password

file_line { 'Turn off passwd auth':
  path   => '/home/luc/.ssh/config',
  line   => 'PasswordAuthentication no',
  match  => '^#?PasswordAuthentication',
}

file_line { 'Declare identity file':
  path   => '/home/luc/.ssh/config',  
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^#?IdentityFile',
}

service { 'ssh':
  ensure     => 'running',
  enable     => true,
  subscribe  => [File_line['Turn off passwd auth'], File_line['Declare identity file']],
}

