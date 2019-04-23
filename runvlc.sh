raspivid -o - -t 99999 -w 800 -h 600 -fps 24|cvlc stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:3000}' :demux=h264
