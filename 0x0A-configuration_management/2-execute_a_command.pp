# kills a process named killmenow
exec {'pkill_killmenow':
    command => '/usr/bin/pkill killmenow'
}
