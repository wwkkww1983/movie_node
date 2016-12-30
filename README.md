# movie_node

cvlc -vvv ~/1.rmvb --sout "#transcode{vcodec=h264,acodec=mpga,ab=128,channels=2,samplerate=44100}:udp{dst=255.255.255.255:1234}" --sout-all --sout-keep



¬¬http://shumeipai.nxez.com/2014/11/23/raspberry-pi-using-vlc-show-nude-webcam-stream-h264.html¬¬



raspivid -t 0 -w 1280 -h 720 -fps 25 -b 500000 -o - | ffmpeg -i - -vcodec copy -an -r 25 -f flv rtmp://send1.douyu.com/live/1249638rhQH4LZPT?wsSecret=8c152df367127c3010765348971b1345\&wsTime=5816ee6f


ffmpeg -i /dev/video0 -vcodec copy -an -r 25 -f flv rtmp://send1.douyu.com/live/1249638rhQH4LZPT?wsSecret=8c152df367127c3010765348971b1345\&wsTime=5816ee6f

ffmpeg -i /dev/video0 -vcodec copy -an -r 25 -f libx264 rtmp://send1.douyu.com/live/1249638rhQH4LZPT?wsSecret=8c152df367127c3010765348971b1345\&wsTime=5816ee6f




ffmpeg -f x11grab -video_size 640x480 -framerate 30 -i :0.0 \
-f v4l2 -video_size 320x240 -framerate 30 -i /dev/video0  -maxrate 3000k -bufsize 4000k -acodec libmp3lame -ar 44100 -b:a 128k \
-f flv rtmp://send1.douyu.com/live/1249638rhQH4LZPT?wsSecret=8c152df367127c3010765348971b1345\&wsTime=5816ee6f


ffmpeg -f v4l2 -video_size 1680x1050 -framerate 30 -i /dev/video0  -maxrate 3000k -bufsize 4000k -acodec libmp3lame -ar 44100 -b:a 128k \
-f flv rtmp://send1.douyu.com/live/1249638rhQH4LZPT?wsSecret=8c152df367127c3010765348971b1345\&wsTime=5816ee6f



ffmpeg -f x11grab -video_size 1680x1050 -framerate 30 -i :0.0 -maxrate 3000k -bufsize 4000k -acodec libmp3lame -ar 44100 -b:a 128k \
-f flv rtmp://send1.douyu.com/live/1249638rhQH4LZPT?wsSecret=8c152df367127c3010765348971b1345\&wsTime=5816ee6f
