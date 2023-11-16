# default limit
file { '/etc/default/nginx':
  ensure  => file,
  content => '# /etc/default/nginx
# Note: You may want to look at the following page before setting the ULIMIT.
#  http://wiki.nginx.org/CoreModule#worker_rlimit_nofile
# Set the ulimit variable if you need defaults to change.
#  Example: ULIMIT="-n 4096"
ULIMIT="-n 4096"
',
  notify  => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  command     => '/usr/sbin/service nginx restart',  # Adjust the commands as per your system's init system
  refreshonly => true,
  subscribe   => File['/etc/default/nginx'],
}
