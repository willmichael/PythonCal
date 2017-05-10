import calendar 
import sys
import time
import fire

class PyCal():
    # Update Calendar
    def u(self, date, name, desc):
        print date
        print name
        print desc

    # Display day
    def d(self, *args):
        count = len(args)
        # Display today
        if count == 0:
            print "today"

        # Display day n
        elif count == 1:
            print args[0]

        # Display day range
        else:
            for a in args:
                print a
        

def main():
    fire.Fire(PyCal)


if __name__ == "__main__":
    main()

