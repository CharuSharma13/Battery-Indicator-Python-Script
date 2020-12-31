import psutil 							  # psutil ( Python system and process utility)  contain info about processes and system utilization
										   # that will be the CPU, memory , disk , network, censors and battery

import time                               #add some delay in our operation

import pyttsx3      						#text to speech library (work offline) providing voice elert to user whether battery is getting 
										   #low or completed

from win10toast import ToastNotifier 		#providing desktop notification to user

import threading							#run different process at the same time (used for voice alert as well as desktop notification simultaneously)


# initialize objects
toaster=ToastNotifier()
x=pyttsx3.init()
x.setProperty("rate",130)
x.setProperty("volume",10)


def show_notification(show_text):
	toaster.show_toast("BATTERY WARN",show_text,duration=10)
	while(toaster.notification_active()):
		time.sleep(0.1)

def monitor():
	count=0
	while(count<2):
		time.sleep(15)
		battery=psutil.sensors_battery()
		plugged=battery.power_plugged
		percent=int(battery.percent)

		if(percent<20):
			if(plugged==False):
				processthread=threading.Thread(target=show_notification,args=("Your battery at "+str(percent)+"% Please plug the cable",))
				processthread.start()
				x.say("Your battery is getting low so charge it now")
				x.runAndWait()
				count=count+1
				

		elif(percent>90):
			if(plugged==True):
				processthread=threading.Thread(target=show_notification,args=("Charging is getting complete",))
				processthread.start()
				x.say("Charging is getting complete")
				x.runAndWait()
				count=count+1

		else:
			count=2
				

if __name__ == '__main__':
	monitor()
