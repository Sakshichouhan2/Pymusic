from pygame import mixer
mixer.init()

mixer.music.load("Malang (Title Track)(bossmobi).mp3")
mixer.music.set_volume(0.7)
mixer.music.play()


while True:
	print("Press 'P' to pause 'R' to resume ")
	print("Press 'E' to exit the program" ) 
	query = input(" >>> ")

	if query == 'P' or 'p':
		mixer.music.pause()
	elif query == 'R' or 'r':
		mixer.music.unpause()
	elif query == 'E' or 'e':
		mixer.music.stop()
		break