# Puppet manifest for installing and configuring nginx

exec {'update_kernel':
    command => '/usr/bin/apt-get update'
}

exec {'install nginx':
    command => '/usr/bin/apt-get install -y nginx'
}

exec {'mkdir_root_html':
    command => '/usr/bin/mkdir -p /var/www/html/'
}

file {'/var/www/html/index.html':
    content => 'Hello World!'
}

file {'/var/www/html/404.html':
    content => "Ceci n'est pas une page"
}

$config ="server {
    listen 80;
    listen [::]:80;

    server_name bravemaster.tech www.bravemaster.tech;
    root /var/www/html;
    index index.html index.htm;

    location /redirect_me {
        return 301 https://github.com/bravemaster3;
    }
}"

file {'/etc/nginx/sites-available/default':
    content => $config
}

exec {'restart_nginx_service':
    command => '/usr/sbin/service nginx restart'
}
