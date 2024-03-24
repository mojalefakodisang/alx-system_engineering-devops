# Configures SSH for no password and specifying IdentityFile

$line_string = "Host 34.239.250.176\n\
    IndentityFile ~/.ssh/school\n\
    PasswordAuthentication no\n\"

file {"/etc/ssh/ssh_config":
    ensure => file,
    content => $line_string
}
