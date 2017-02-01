#!/bin/bash
#!written by Samuel Churlaud (github.com/quendil) for github.com/learningthruresearch/Biosensors2017/tree/master/poworm_rangers

mkdir clean_bio_sensor
for i in $(ls bio_sensor/ | xargs); do cut -d"," -f1,3 bio_sensor/$i > clean_bio_sensor/$i; sed -i 1d clean_bio_sensor/$i; done