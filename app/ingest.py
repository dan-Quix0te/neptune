#!venv/bin/python3


import ffmpeg

def ingestMedia(in_filename):
    probe = ffmpeg.probe(in_filename)
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    width = int(video_stream['width'])
    height = int(video_stream['height'])
    return width, height

if __name__ == "__main__":
    ingest('media/test.mp4')

