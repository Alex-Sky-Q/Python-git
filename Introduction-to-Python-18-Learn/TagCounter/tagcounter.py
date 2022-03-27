import func

# func.run_gui_cl()
# url = 'https://' + 'skyfitness.ru'
# func.db_reader(url)

# Temporary write to file - logs in the future
# func.dict_writer(tags)



from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
