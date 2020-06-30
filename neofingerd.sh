#!/bin/bash
. .env
$NF_PREPEND tcpserver -v -u $NF_RUNAS -g $NF_GROUP  0 $NF_PORT $NF_BASEDIR/finger-wrapper.sh
