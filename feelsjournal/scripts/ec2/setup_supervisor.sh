###############################################
echo "*****************************************"
echo " 1. Prerequisites: Install easy install"
echo "*****************************************"
yum -y update
yum -y install python-setuptools
echo "*****************************************"
echo " 2. Install supervisor"
echo "*****************************************"
easy_install supervisor
echo "*****************************************"
echo " 3. Check version"
echo "*****************************************"
supervisord --version
echo "*****************************************"
echo " 4. Configure Supervisord.Conf"
echo "*****************************************"
echo " Edit supervisor.conf as follows:"
echo " 1: ... add feelsjournal.conf"
echo " 3: ... make directories for logfile for feelsjournal"
echo "*****************************************"
#echo_supervisord_conf > /etc/supervisord.conf
mv /root/feelsjournal/scripts/ec2/supervisor/supervisord.conf /etc/
mkdir /etc/supervisor.d/
mkdir -p /var/log/feelsjournal/
touch /var/log/feelsjournal/access.log
echo "*****************************************"
echo " 5. Install Init Script"
echo "*****************************************"
mv /root/feelsjournal/scripts/ec2/supervisor/supervisord /etc/rc.d/init.d/
mv /root/feelsjournal/scripts/ec2/supervisor/feelsjournal.conf /etc/supervisor.d/
chmod +x /etc/rc.d/init.d/supervisord
echo "*****************************************"
echo " 6. Auto-Enable Supervisor"
echo "*****************************************"
chkconfig --add supervisord
chkconfig --level 345 supervisord on
echo "*****************************************"
echo " 7. Start Supervisor"
echo "*****************************************"
touch /var/run/supervisord.pid
service supervisord start
echo "*****************************************"
echo " Complete!"
echo "*****************************************"
