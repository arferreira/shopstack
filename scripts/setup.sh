#!/bin/bash

echo "Provisioning virtual machine..."


sudo apt-get update

sudo apt-get -y upgrade

# Install Python.
sudo apt-get install -y python3-dev python3-pip

# Install PostgreSQL.
sudo apt-get install -y postgresql postgresql-contrib libpq-dev




