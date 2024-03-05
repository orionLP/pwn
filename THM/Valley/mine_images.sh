#!/bin/bash

for i in {1..18}
do
  wget -O "mine$i.jpg" "http://10.10.19.32/static/$i"
done

for i in {1..18}
do
  echo "Image $i"
  echo " "
  exiftool mine$i.jpg
done