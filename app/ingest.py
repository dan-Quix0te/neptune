#!venv/bin/python3


import ffmpeg

#stream = ffmpeg.input('input.mp4')
#stream = ffmpeg.hflip(stream)
#stream = ffmpeg.output(stream, 'output.mp4')
#ffmpeg.run(stream)
#
## Fluent
#
#import ffmpeg
#(
#    ffmpeg
#    .input('input.mp4')
#    .hflip()
#    .output('output.mp4')
#    .run()
#)
#
#
## Probe for ingest
#
#probe = ffmpeg.probe(args.in_filename)
#video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
#width = int(video_stream['width'])
#height = int(video_stream['height'])
#
#
## RTSP to pipe
#
#packet_size = 4096
#
#process = (
#    ffmpeg
#    .input('rtsp://%s:8554/default')
#    .output('-', format='h264')
#    .run_async(pipe_stdout=True)
#)
#
#while process.poll() is None:
#    packet = process.stdout.read(packet_size)
#    try:
#        tcp_socket.send(packet)
#    except socket.error:
#        process.stdout.close()
#        process.wait()
#        break
#
## To server
#
#video_format = "flv"
#server_url = "http://127.0.0.1:8080"
#
#process = (
#    ffmpeg
#    .input("input.mp4")
#    .output(
#        server_url, 
#        codec = "copy", # use same codecs of the original video
#        listen=1, # enables HTTP server
#        f=video_format)
#    .global_args("-re") # argument to act as a live stream
#    .run()
#)
#
#
#
#
