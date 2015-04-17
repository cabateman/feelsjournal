#!/bin/bash
yum -y install git
git clone https://chrisbates:aassddff90-@github.com/chrisbates/metricboard-server.git /root/feelsjournal

chmod +x /root/metricboard-server/scripts/ec2/run_all.sh
/root/metricboard-server/scripts/ec2/run_all.sh

