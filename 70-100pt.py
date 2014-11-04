##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Canvas Widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# This is the outline of the house: Just roof and base house shape
square = drawpad.create_rectangle(260,320,530,600, fill='white')
line = drawpad.create_line(260, 320, 380, 180)
line = drawpad.create_line(530, 320, 380, 180)
#Square windows
square = drawpad.create_rectangle(300,360,340,400, fill='red')
square = drawpad.create_rectangle(460,360,500,400, fill='red')
#door
square = drawpad.create_rectangle(370,510,430,600, fill='white')
#Door Handle
square = drawpad.create_rectangle(410,550,430,560, fill='white')
#Chimney
line = drawpad.create_line(300, 272, 300, 180)
line = drawpad.create_line(300, 180, 340, 180)
line = drawpad.create_line(340, 180, 340, 227)





root.mainloop()
