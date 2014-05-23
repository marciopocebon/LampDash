from gi.repository import Gtk

glade_file = "NanoDash.glade"

class Handler:
    """
    Callback handler functions for the Gtk signals
    """
    def __init__(self, GtkBuilder):
        self.builder = GtkBuilder

    def openAboutWin(self, *args):
        self.aboutWin = self.builder.get_object("aboutdialog1")
        self.aboutWin.show_all()
        
    def deleteMainWindow(self, *args):
        Gtk.main_quit()

class MainWindow:
    """
    Gtk Builder and main top level window
    Sets up event handling and shows windows
    """
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(glade_file)
        self.builder.connect_signals(Handler(self.builder))
        self.win = self.builder.get_object("MainWindow")
        self.win.show_all()

if __name__ == "__main__":
    mainWin = MainWindow()
    Gtk.main()
