###################################################
# NTUPhone screen for the game                    #
###################################################
from game_manager import *

class NTUPhoneScreen(Screen):#TODO: set a restart phone button
	phonescreen_state = ListProperty([False,False])
	def __init__(self, player_id=0,chapter_id=0, **kwargs):
		super(NTUPhoneScreen, self).__init__(**kwargs)
		self.player_id = player_id
		self.chapter_id = chapter_id
		self.size = (self.screen_x,self.screen_y) = get_screen_size()
		print('NTUPhoneScreen.size:',self.size)

		self.phone_pos_hint = {'x':.35,'y':.025}#(.35*self.screen_x,.025*self.screen_y)
		self.phone_size_hint = (.3,.95)#(.3*self.screen_x,.95*self.screen_y) 
		self.canvas.add(Color(.718, .831, .941, 1))
		self.canvas.add(Rectangle(pos=self.pos, size=self.size))

		self.phone = NTUPhone(screen= self,source='res/images/phone/phone_messege.png',pos_hint=self.phone_pos_hint , size_hint=self.phone_size_hint,allow_stretch=True,keep_ratio=False )
		self.add_widget(self.phone)

		btn_len = min(.1*global_w, .2*global_h)
		self.canvas.add(Color(0, 0, 0, .9))
		self.canvas.add(Ellipse(pos=(.2*global_w, .2*global_h), size=(btn_len,btn_len)))
		self.canvas.add(Color(1, 1, 1, .8))
		self.canvas.add(Ellipse(pos=(.2*global_w+btn_len/10, .2*global_h+btn_len/10), size=(.8*btn_len,.8*btn_len)))
		self.add_widget(Label(text='Back!',font_size=100,pos=(.2*global_w+btn_len/10, .2*global_h+btn_len/10), size=(.8*btn_len,.8*btn_len)))
		self.add_widget(Button(on_press=self.back_to_story,background_color=(1,1,1,0),pos_hint={'x':.2,'y':.2},\
			size_hint=(btn_len/global_w,btn_len/global_h)))


	def back_to_story(self,btn):
		self.manager.current = 'story'

class NTUPhone(Image):
	executing_function = StringProperty('messege')
	def __init__(self,screen, **kwargs):
		super(NTUPhone, self).__init__(**kwargs)
		self.messege = 'res/images/phone/phone_messege.png'
		self.screen = screen
	def execute(self,instance, function):
		if function == 'messege':
			self.executing_function = 'messege'
			self.source = self.messege
		elif function == 'story':
			self.executing_function = 'story'
			self.source = 'res/images/phone/phone_story.png'
		elif function == 'NTU':
			self.executing_function = 'NTU'
			self.source = 'res/images/phone/phone_NTU.png' 
		else:
			pass

	def to_direct_messege(self,person,*args):
		if self.messege == 'res/images/phone/phone_messege.png':
			self.source = self.messege = 'res/images/phone/direct_messege.png'
		elif self.messege == 'res/images/phone/direct_messege.png':
			self.source = self.messege = 'res/images/phone/phone_messege.png'



	def on_touch_down(self,touch):
		if self.collide_point(*touch.pos):
			print('touch phone:',touch.pos,touch.spos)





