# install build tools 
sudo yum install make automake gcc gcc-c++ kernel-devel git-core -y 

# install virtualenv
curl -o /tmp/ez_setup.py https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
/usr/bin/python27 /tmp/ez_setup.py 
/usr/bin/easy_install-2.7 pip 
pip install virtualenv

# setup virtual env
sudo virtualenv feelsjournal
source feelsjournal/bin/activate

# install postgres
yum -y install postgresql-devel
pip install -r /root/feelsjournal/requirements.txt

# install gunicorn
pip install gunicorn
pip install setproctitle

# install nginx 
sudo yum install -y nginx
sudo /etc/init.d/nginx start

sudo mv /root/feelsjournal/scripts/ec2/feelsjournal_nginx.conf /etc/nginx/conf.d/
sudo /etc/init.d/nginx restart

# Setup Supervisor
chmod +x /root/feelsjournal/scripts/ec2/setup_supervisor.sh
/root/feelsjournal/scripts/ec2/setup_supervisor.sh

sudo pkill gunicorn
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start feelsjournal

