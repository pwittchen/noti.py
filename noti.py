#!/usr/bin/python -u
import sys, getopt
from gi.repository import Gtk, Notify

def main(argv):
    title = ''
    message = ''
    try:
        opts, args = getopt.getopt(argv,"t:m:",["title=","message="])
    except getopt.GetoptError:
        print 'noti.py -t <title> -m <message>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'noti.py -t <title> -m <message>'
            sys.exit()
        elif opt in ("-t", "--title"):
            title = arg
        elif opt in ("-m", "--message"):
            message = arg
            show_notification(title, message)

def show_notification(title, message):
    Notify.init ('Application')
    notification = Notify.Notification.new (title, message, '')
    notification.show ()

if __name__ == "__main__":
    main(sys.argv[1:])
