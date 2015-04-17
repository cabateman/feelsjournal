# now install pip for 2.7 
curl -o /tmp/ez_setup.py https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
/usr/bin/python27 /tmp/ez_setup.py 
/usr/bin/easy_install-2.7 pip 
pip install virtualenv
#pip install --upgrade virtualenvwrapper
#echo "source /usr/bin/virtualenvwrapper_lazy.sh" >> /root/.bashrc
#source /root/.bashrc

mkvirtualenv feelsjournal
source /root/.virtualenvs/feelsjournal/bin/activate
yum -y install postgresql-devel
pip install -r /root/feelsjournal/requirements.txt
