from tkinter import *
import tkintermapview

root = Tk()
root.title('Map View')
root.geometry("900x700")

my_label = LabelFrame(root)
my_label.pack(pady=20)

map_widget = tkintermapview.TkinterMapView(my_label, width=800, height=600, corner_radius=0)
# Set Coordinates
map_widget.set_position(5.6037, -0.1870)    # Accra
# Set Zoom Level
map_widget.set_zoom(9)
# Set address position
# map_widget.set_address("accra, ghana")

map_widget.pack()



root.mainloop()