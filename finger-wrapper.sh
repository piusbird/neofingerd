#!/usr/bin/env bash
set -e
source .env
cd $NF_BASEDIR
source .venv/bin/activate
exec ./neofinger.py
