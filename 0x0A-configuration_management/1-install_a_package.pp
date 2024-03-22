# Installs flask from pip3 with all dependencies

# check that python 3 is installed
package {'python3':
    ensure   => present,
}

# Check that pip3 is installed
package {'python3-pip':
    ensure => present
}

# install flask version 2.1.0
package {'flask':
    ensure   =>'2.1.0',
    name     =>'flask',
    provider =>'pip'
}

# install werkzeug
package {'werkzeug':
    ensure   =>'2.1.1',
    provider =>'pip'
}
