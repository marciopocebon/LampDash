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

class NanoDash:
    """
    Gtk Builder and main top level window
    Sets up event handling and shows windows
    """
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(glade_file)
        self.builder.connect_signals(Handler(self.builder))
        self.mainWin = self.builder.get_object("MainWindow")
        self.mainWin.show_all()

        # Fill the hosts TextView with /etc/hosts file
        self.ehostsTextView = self.builder.get_object("ehostsText")
        self.ehostsBuff = self.ehostsTextView.get_buffer()
        with open("/etc/hosts", "r") as hostsFile:
            self.ehostsBuff.set_text(hostsFile.read())

        # Fill the vhosts
        self.vhostsTextView = self.builder.get_object("vhostsText")
        self.vhostsBuff = self.vhostsTextView.get_buffer()
        with open("/etc/httpd/conf/httpd.conf", "r") as hostsFile:
            self.vhostsBuff.set_text(hostsFile.read())
        
        # Set the httpd status text
        # Running/Off

    # def save etchosts

    # def restart httpd

    def run(self):
        Gtk.main()


if __name__ == "__main__":
    dash = NanoDash()
    dash.run()
