# Library      : PyColor
# Language     : Python  Version 2 & 3
# Version      : 1.0.0
# Auther       : Ayman Mahmoud Alaiwah    
# Facebook     : https://www.fb.com/ProgAymanAlaiwah
# GitHub       : https://github.com/ProgAymanAlaiwah
#---------------------------------------------------#

# Used ctypes to access the C-API of the interpreter
import ctypes as c 

# Edit Api Interpreter
_get_dict = c.pythonapi._PyObject_GetDictPtr
_get_dict.restype = c.POINTER(c.py_object)
_get_dict.argtypes = [c.py_object]
def get_dict(object):return _get_dict(object).contents.value
 
# Function Main 
def set_code_color(self,code_color) :return  "\x1b[1;{0};40m{1}\x1b[0m".format(code_color,self)
def set_code_bg(self,code_color)    :return  "\033[{0}m{1}\033[00m".format(code_color,self)

# Function Edit Fonts Text
def text_bold(self)      :return "\033[1m{0}\033[21m".format(self) 
def text_underline(self) :return "\033[4m{0}\033[24m".format(self)
get_dict(str)['text_bold']      = text_bold
get_dict(str)['text_underline'] = text_underline

# Function Edit Text Colors
def white(self)   :return set_code_color(self,97)
def black(self)   :return set_code_color(self,30) 
def red(self)     :return set_code_color(self,31) 
def green(self)   :return set_code_color(self,32) 
def yellow(self)  :return set_code_color(self,33) 
def blue(self)    :return set_code_color(self,34) 
def magenta(self) :return set_code_color(self,35) 
def cyan(self)    :return set_code_color(self,36) 
def gray(self)    :return set_code_color(self,90) 

# Add Function Text Colors To Class String The Private Python Using 
# Library ctypes API The Edit is On Interpreter Python
get_dict(str)['white']   = white
get_dict(str)['black']   = black
get_dict(str)['red']     = red
get_dict(str)['green']   = green
get_dict(str)['yellow']  = yellow
get_dict(str)['blue']    = blue
get_dict(str)['magenta'] = magenta
get_dict(str)['cyan']    = cyan
get_dict(str)['gray']    = gray


# Function Edit Background Colors
def bg_white(self)   :return set_code_bg(self,107)
def bg_black(self)   :return set_code_bg(self,40) 
def bg_red(self)     :return set_code_bg(self,41) 
def bg_green(self)   :return set_code_bg(self,42) 
def bg_yellow(self)  :return set_code_bg(self,43) 
def bg_blue(self)    :return set_code_bg(self,44) 
def bg_magenta(self) :return set_code_bg(self,45) 
def bg_cyan(self)    :return set_code_bg(self,46) 
def bg_gray(self)    :return set_code_bg(self,100) 

# Add Function Background Colors To Class String The Private Python Using 
# Library ctypes API The Edit is On Interpreter Python
get_dict(str)['bg_white']   = bg_white
get_dict(str)['bg_black']   = bg_black
get_dict(str)['bg_red']     = bg_red
get_dict(str)['bg_green']   = bg_green
get_dict(str)['bg_yellow']  = bg_yellow
get_dict(str)['bg_blue']    = bg_blue
get_dict(str)['bg_magenta'] = bg_magenta
get_dict(str)['bg_cyan']    = bg_cyan
get_dict(str)['bg_gray']    = bg_gray

# Show All Function Text Color And Background Color 
def showColor():

	# Array Content All Function Color And Background Color 
	colors ={
				'Text':[
					'white'.white(),
					'black'.black(),
					'red'.red(),
					'green'.green(),
					'yellow'.yellow(),
					'blue'.blue(),
					'magenta'.magenta(),
					'cyan'.cyan(),
					'gray'.gray()
				],
				'Bg'  :[
					'bg_white'.bg_white(),
					'bg_black'.bg_black(),
					'bg_red'.bg_red(),
					'bg_green'.bg_green(),
					'bg_yellow'.bg_yellow(),
					'bg_blue'.bg_blue(),
					'bg_magenta'.bg_magenta(),
					'bg_cyan'.bg_cyan(),
					'bg_gray'.bg_gray()
				]
			}
	print("------------[ Name Function Color ]-------------")
	for color in colors['Text']:
		print(color)
	print("------------[ Name Function Bg Color ]----------")
	for color in colors['Bg']:
		print(color)