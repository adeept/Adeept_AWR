#!/usr/bin/env python3
# File name   : servo.py
# Description : Control Motor
# Product     : RaspRover
# Website     : www.adeept.com
# E-mail      : support@adeept.com
# Author      : William
# Date        : 2019/02/23
from __future__ import division
import time
import RPi.GPIO as GPIO
import sys
import Adafruit_PCA9685

'''
change this form 1 to 0 to reverse servos
'''
look_direction = 1


pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

look_max = 500
look_min = 100

org_pos = 300

def ctrl_range(raw, max_genout, min_genout):
	if raw > max_genout:
		raw_output = max_genout
	elif raw < min_genout:
		raw_output = min_genout
	else:
		raw_output = raw
	return int(raw_output)


def camera_ang(direction, ang):
	global org_pos
	if ang == 'no':
		ang = 50
	if look_direction:
		if direction == 'lookdown':
			if org_pos < 300:
				org_pos+=ang
				org_pos = ctrl_range(org_pos, look_max, look_min)		
		elif direction == 'lookup':
			org_pos-=ang
			org_pos = ctrl_range(org_pos, look_max, look_min)
		elif direction == 'home':
			org_pos = 300
	else:
		if direction == 'lookdown':
			org_pos-=ang
			org_pos = ctrl_range(org_pos, look_max, look_min)
		elif direction == 'lookup':
			org_pos+=ang
			org_pos = ctrl_range(org_pos, look_max, look_min)
		elif direction == 'home':
			org_pos = 300	

	pwm.set_all_pwm(0,org_pos)


def clean_all():
	pwm.set_all_pwm(0, 0)


if __name__ == '__main__':
	camera_ang('lookup')
	time.sleep(1)
	camera_ang('lookup')
	time.sleep(1)
	camera_ang('lookup')
	time.sleep(1)
	camera_ang('lookup')
	time.sleep(1)
	camera_ang('lookdown')
	time.sleep(1)
	camera_ang('lookdown')
	time.sleep(1)
	camera_ang('home')
	time.sleep(1)
	'''
	camera_ang('home', 0)
	time.sleep(0.4)
	clean_all()
	while 1:
		a=input('press any key')
		print(camera_ang('lookup', 0))
		pass
	'''