#!venv/bin/python3


import ffmpeg

def ingestMedia(in_filename):
    probe = ffmpeg.probe(in_filename)
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    return video_stream

if __name__ == "__main__":
    ingestMedia('media/test.mp4')

