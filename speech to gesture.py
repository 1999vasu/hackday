import speech_recognition as sr
import time
import cv2
import os
r = sr.Recognizer()
with sr.Microphone() as source:
	print("Say something")
	audio = r.listen(source)
	print("end")
try:
	a = r.recognize_google(audio)
	print("Text: "+ a)
except:
	pass


a  = [i.lower() for i in a.strip().split()]
print(a)
b = []
for i in range(len(a)):
	if(a[i]=='how' and a[i+1]=='are'):
		b.append('how_are')
		i+=1
		continue
	if(a[i] == 'peace' and a[i+1] =='out'):
		b.append('peace_out')
		i+=1
		continue
	if(a[i]=='do'):
		continue
	b.append(a[i])
print(b)
for i in b:
	if(i+'.jpeg' in os.listdir('./text to gesture/')):
		x = cv2.imread('./text to gesture/'+i+'.jpeg')
		cv2.imshow('video',x)
		cv2.waitKey(0)
cv2.destroyAllWindows()
