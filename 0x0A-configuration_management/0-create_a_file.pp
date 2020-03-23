# create a file in /tmp

file {'holberton':
  ensure  => 'present',
  mode    => '0744',
  content => 'I love Puppet',
  owner   => 'www-data',
  group  => 'www-data',
  path    => '/tmp/holberton',
}
