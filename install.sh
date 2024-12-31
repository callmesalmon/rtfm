#!/usr/bin/bash

# Source vars
SRC_DIR=./src
SRC_BIN=$SRC_DIR/main.py

# Installation vars
INSTALL_DIR=/usr/local/bin
INSTALL_BIN=$INSTALL_DIR/rtfm

# Libraries
for src in $SRC_DIR/*; do
    if [ -f $src ] && [ src != "main.py" ]; then
        sudo cp $src $INSTALL_DIR/$(basename $src)
    fi
done

# Binary
sudo cp $SRC_BIN $INSTALL_BIN
