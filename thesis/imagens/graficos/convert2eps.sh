#!/bin/sh

for i in *.png; do convert $i ${i/.png}.eps; done
for i in *.jpg; do convert $i ${i/.jpg}.eps; done
