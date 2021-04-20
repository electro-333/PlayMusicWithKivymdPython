
__author__ = """ Badr """
__date__ = """18/4/2021"""
__version__ = """0.0.1"""

from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.app import MDApp
from pygame import mixer
##########################################################
KV = '''
ScreenManager:
	FirstScreen:
<FirstScreen>:
	name:"FirstScreen"
	MDFloatLayout:
		md_bg_color:[0/255,0/255,0/255,1]
		MDRaisedButton:
			text:"play"
			pos_hint:{"center_y":.5,"center_x":.8}
			on_press:app.play()
		MDRaisedButton:
			text:"pause"
			pos_hint:{"center_y":.5,"center_x":.5}
			on_press:app.pause()
			
		MDRaisedButton:
			text:"continue"
			pos_hint:{"center_y":.5,"center_x":.2}
			on_press:app.unpause()
'''
##########################################################
class FirstScreen(Screen):
    pass
#########################################################
sm = ScreenManager()
sm.add_widget(FirstScreen(name = 'FirstScreen'))
#########################################################
class Main(MDApp):
	def build(self):
		self.app1=Builder.load_string(KV)
		return self.app1
	def play(self):
		mixer.init()
		mixer.music.load("/sdcard/kivy/gtts.mp3")
		mixer.music.set_volume(0.7)
		mixer.music.play() # start music from 00:00
		
	def pause(self):
		mixer.music.pause() #pause music
	
	def unpause(self):
		mixer.music.unpause() #continue music
		
		
		
		
#########################################################
Main().run()



