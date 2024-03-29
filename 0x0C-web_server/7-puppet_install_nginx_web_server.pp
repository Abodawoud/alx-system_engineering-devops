# Install Nginx web server (w/ Puppet)
package { 'nginx':
  ensure => installed,
}

exec { 'become_root':
  command     => 'sudo -i',
  path        => ['/usr/bin', '/bin'],
  refreshonly => true,
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => [Package['nginx'], Exec['become_root']],
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

            index index.html index.htm index.nginx-debian.html;

            server_name abodawoud.tech;

            error_page 404 /custom_404.html;

            location /redirect_me {
                    return 301 https://www.linkedin.com/in/abodawoud/;
            }

            location / {
                    root /var/www/html;
                    index index.nginx-debian.html;
                    try_files $uri $uri/ =404;
            }
}
  ',
  require => Package['nginx'],
  replace => 'true',
}

service { 'nginx':
  notify => File['/etc/nginx/sites-available/default'],
}
