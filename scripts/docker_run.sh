#!/bin/bash
docker run -d -it --mount type=bind,source=/home/fingerpose/Videos,target=/open$
mv ../video.avi ../Videos/
sudo mkdir ../Videos/output
