#!/usr/bin/env python

import gtk, webkit

def goback(button):
	view.go_back()

def navrequest(thisview, frame, networkRequest):
	address = networkRequest.get_uri()
	if not "debian.org" in address:
		md = gtk.MessageDialog(win, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, gtk.BUTTONS_CLOSE, "Not allowed to leave the site!")
		md.run()
		md.destroy()
		view.open("http://www.debian.org")

view = webkit.WebView()
view.connect("navigation-requested", navrequest)

sw = gtk.ScrolledWindow()
sw.add(view)

button = gtk.Button("Back")
button.connect("clicked", goback)

vbox = gtk.VBox()
vbox.pack_start(button, False, False, 0)
vbox.add(sw)

win = gtk.Window(gtk.WINDOW_TOPLEVEL)
win.set_size_request(800, 600)
win.connect("destroy", gtk.main_quit)
win.set_title("Victoria's micro-browser")
win.add(vbox)
win.show_all()

view.open("http://www.debian.org") 
gtk.main()
