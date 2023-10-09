# Install Nginx web server (w/ Puppet)
package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => present,
  content => "Hello World!\n",
  require => Package['nginx'],
}

file { '/var/www/html/custom_404.html':
  ensure  => present,
  content => "Ceci n'est pas une page\n",
  require => Package['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => '
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html;

        location /redirect_me {
            return 301 https://www.linkedin.com/in/abodawoud/;
        }
    }
  ',
  require => Package['nginx'],
}

service { 'nginx':
  notify => File['/etc/nginx/sites-available/default'],
}
