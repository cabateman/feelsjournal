#!/bin/bash
yum -y install git
git clone https://chrisbates:aassddff90-@github.com/chrisbates/feelsjournal.git /root/feelsjournal

chmod +x /root/feelsjournal/scripts/ec2/run_all.sh
/root/feelsjournal/scripts/ec2/run_all.sh

