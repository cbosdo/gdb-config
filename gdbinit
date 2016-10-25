# Copy this file to ~/.gdbinit and fix it

set debug auto-load on

set auto-load python-scripts
add-auto-load-safe-path ~
# Replace <user> by the proper username
add-auto-load-scripts-directory /home/<user>/.gdb/python/auto-load

set print pretty on
set print object on
