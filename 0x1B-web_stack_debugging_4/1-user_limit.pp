# 1-user_limit.pp

file { '/etc/security/limits.conf':
  content => "holberton hard nofile 97816\nholberton soft nofile 97816\n",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

exec { 'reload_pam':
  command     => '/bin/pkill -HUP -u holberton bash',
  refreshonly => true,
  subscribe   => File['/etc/security/limits.conf'],
}

user { 'holberton':
  ensure => present,
}
