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
        Gtk.main_quit(*args)

    def setHostsText(self, *args):
        print(args)

class NanoDash:
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

        # Fill the hosts TextView with /etc/hosts file
        self.hostsTextView = self.builder.get_object("textview1")
        self.hostsBuff = self.hostsTextView.get_buffer()
        with open("/etc/hosts", "r") as hostsFile:
            self.hostsBuff.set_text(hostsFile.read())

        # Fill the vhosts TreeView with a list of sites-available
        # List of files, on/off toggle, edit button, delete, clone
        
        # Set the httpd status text
        # Running/Off

    # def save etchosts

    # def restart httpd

    def run(self):
        Gtk.main()


if __name__ == "__main__":
    dash = NanoDash()
    dash.run()
