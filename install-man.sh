#!/usr/bin/bash

if [ ! -f "/usr/local/man/man1" ]; then
    [ ! -f "/usr/local/man" ] && mkdir /usr/local/man
    mkdir /usr/local/man/man1
fi

cd man && rtfm
cd ..
