source /root/.virtualenvs/feelsjournal/bin/activate

pip install gunicorn
pip install setproctitle

chmod u+x /root/feelsjournal/bin/gunicorn_start.sh
