
cd /var/www/html

git clone 

sudo apt update

sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools

sudo apt install python3-venv

python3 -m venv venv

source venv/bin/activate

venv/bin/pip install -r requirements.txt

sudo apt install nginx

ln -s neptune-admin/setup/gunicorn/neptune.serivce /etc/systemd/system/

sudo systemctl enable neptune.service

sudo systemctl start neptune.service

ln -s neptune-admin/setup/nginx/neptune.conf /etc/nginx/sites-enabled/

sudo systemctl restart nginx

ref - https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04
