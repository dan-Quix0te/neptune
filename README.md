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
