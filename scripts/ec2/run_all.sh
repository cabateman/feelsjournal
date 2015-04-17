# Setup Python
chmod +x /root/metricboard-server/scripts/ec2/setup_python.sh
/root/metricboard-server/scripts/ec2/setup_python.sh

# Setup Environment Settings
chmod +x /root/metricboard-server/scripts/ec2/setup_env.sh
/root/metricboard-server/scripts/ec2/setup_env.sh

# Setup Gunicorn
chmod +x /root/metricboard-server/scripts/ec2/setup_gunicorn.sh
/root/metricboard-server/scripts/ec2/setup_gunicorn.sh

# Setup Supervisor
chmod +x /root/metricboard-server/scripts/ec2/setup_supervisor.sh
/root/metricboard-server/scripts/ec2/setup_supervisor.sh
