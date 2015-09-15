import sys
import time
import threading
import tkinter as tk
import unitplot as up

userModule = __import__(sys.argv[1])
functions = up.registry
names = [x for x in functions.keys()]
names.sort()

class Gui(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        run_all_button = tk.Button(self, text = 'Run All', command = self.run_all)
        run_all_button.grid(column = 0, row = 0)


        run_selected_button = tk.Button(self, text = 'Run Selected', command = self.run_selected)
        run_selected_button.grid(column = 1, row = 0)

        list_box = tk.Listbox(self, selectmode=tk.EXTENDED)
        list_box.grid(column = 0, row = 1, columnspan = 2, sticky = 'EW')

        for name in names:
            list_box.insert(tk.END, name)

        self.list_box = list_box

        self.resizable(False, False)

    def run_all(self):
        for i in range(0, len(names)):
            name = names[i]
            funct = functions[name]
            self.run_funct(funct, i)

    def run_selected(self):
        for i in self.list_box.curselection():
            name = names[i]
            funct = functions[name]
            self.run_funct(funct, i)

    def append_running_symbol(self, index):
        newname = '* ' + names[index]
        self.list_box.delete(index)
        self.list_box.insert(index, newname)

    def append_time(self, time, index):
        newname = names[index] + (' (%.2f s)' % time)
        self.list_box.delete(index)
        self.list_box.insert(index, newname)

    def run_funct(self, funct, index):
        def run():
            start = time.clock()
            funct()
            timeTaken = time.clock() - start
            self.append_time(timeTaken, index)

        t = threading.Thread(target=run)
        t.start()


if __name__ == '__main__':
    gui = Gui(None)
    gui.title('Graphing Util')
    gui.mainloop()
