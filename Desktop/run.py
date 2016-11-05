# import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# s.bind(('0.0.0.0',11719))
# while 1:
# 	message = s.recv(128)
# 	print (message)


import socket
from Tkinter import *

tk=Tk()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('0.0.0.0',11719))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)

text=StringVar()
name=StringVar()
name.set('User')
text.set('')
tk.title('MegaChat')
tk.geometry('400x300')

log = Text(tk)
nick = Entry(tk, textvariable=name)
msg = Entry(tk, textvariable=text)
msg.pack(side='bottom', fill='x', expand='true')
nick.pack(side='bottom', fill='x', expand='true')
log.pack(side='top', fill='both',expand='true')

def loopproc():
	s.setblocking(False)
	try:
		message = s.recv(128)
		log.insert(END,message+'\n')
	except:
		tk.after(1,loopproc)
		return
	tk.after(1,loopproc)
	return

def sendproc(event):
	sock.sendto (name.get()+':'+text.get(),('255.255.255.255',11719))
	text.set('')

msg.bind('<Return>',sendproc)
tk.after(1,loopproc)
tk.mainloop()
