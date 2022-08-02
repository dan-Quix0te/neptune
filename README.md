# Neptune Admin Page 

Admin page to control the backend of Neptune 


## Ingest

Select file

ffprobe readout of file

transcode to channel codec

accepts: files, external streams, and live video out

signal generator 

preview file uploaded 

split audio / video


## Schedule

select source for time slots

drag and drop source into different slots

export schedule ( ffmpeg concat .txt file) 

cron to switch mixer between sources if not concat 


## Mixer

live mixer view with preview / program on top and 8 sources on the bottom

buttons to send commands to mixer

text read out for response from server

text send to give manual commands to mixer

audio mixer

## Record 

Record stream output / iso / mix 


## Archive 

previous recordings 

send to ingest page


## Delivery 

outputs - m3u8 / rtmp / 

to OSP




## Install

<code>

python3 -m venv venv

venv/bin/pip install -r requirements.txt

cp config-example.py config.py (Change secret!)

./run.py 

<ip-address>:5000

</code>


## Tests

ffmpeg -f lavfi -i smptebars -t 30 smpte.mp4


## Install

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


## Docker

docker build --build-arg VERSION=0.0.1 -t neptune .

docker run --name neptune -d -p 5000:5000 neptune/latest





