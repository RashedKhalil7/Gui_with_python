import tkinter as tk 

win = tk.Tk()
'''
label = tk.Label(
	text="Python label!",
	fg = 'green',
	bg = 'yellow',
	width = 10,
	height = 5
	)

button = tk.Button(
	text = 'click me',
	fg = 'black',
	bg = 'blue',
	)
'''
# get data info from username
L = tk.Label(text='username ')
username = tk.Entry()

L.pack()
username.pack()
win.mainloop()