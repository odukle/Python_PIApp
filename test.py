import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

LABEL_WIDTH = 18

def create_window():
    root = tk.Tk()

    ## create widgets

    #label
    lbl = tk.Label(root, text="Test!")
    
    #Date
    frame_date = tk.Frame(root)
    label_date = tk.Label(frame_date, text="Pick date",width=LABEL_WIDTH,anchor="w")
    datePicker = DateEntry(frame_date)
    label_date.pack(side=tk.LEFT)
    datePicker.pack(side=tk.LEFT)

    #ModelYear
    frame_MY = tk.Frame(root)
    label_MY = tk.Label(frame_MY,text="Pick Model Year",width=LABEL_WIDTH,anchor="w")
    myOptions = ["MY21","MY22","MY23","MY24","MY25","MY26"]
    combo_modelYear = ttk.Combobox(frame_MY,values=myOptions)
    combo_modelYear.set(myOptions[0])
    label_MY.pack(side=tk.LEFT)
    combo_modelYear.pack(side=tk.LEFT)

    #Path
    frame_path = tk.Frame(root)
    label_path = tk.Label(frame_path,text="Pick path",width=LABEL_WIDTH,anchor="w")
    pathOptions = ["GEN1","GEN2","GEN3","GEN4"]
    combo_path = ttk.Combobox(frame_path,values=pathOptions)
    combo_path.set(pathOptions[0])
    label_path.pack(side=tk.LEFT)
    combo_path.pack(side=tk.LEFT)

    #ProgramName
    frame_progName = tk.Frame(root)
    label_progName = tk.Label(frame_progName,text="Enter Program Name",width=LABEL_WIDTH,anchor="w")
    entry_progName = tk.Entry(frame_progName)
    label_progName.pack(side=tk.LEFT)
    entry_progName.pack(side=tk.LEFT)

    #Milestone
    frame_milestone = tk.Frame(root)
    label_milestone = tk.Label(frame_milestone,text="Enter Milestone",width=LABEL_WIDTH,anchor="w")
    entry_milestone = tk.Entry(frame_milestone)
    label_milestone.pack(side=tk.LEFT)
    entry_milestone.pack(side=tk.LEFT)

    #ReleaseType
    frame_releaseType = tk.Frame(root)
    label_releaseType = tk.Label(frame_releaseType,text="Pick Release Type",width=LABEL_WIDTH,anchor="w")
    releaseTypeOptions = ["Full","Delta","Experimental"]
    combo_releaseType = ttk.Combobox(frame_releaseType,values=releaseTypeOptions)
    combo_modelYear.set(releaseTypeOptions[0])
    label_releaseType.pack(side=tk.LEFT)
    combo_modelYear.pack(side=tk.LEFT)
    
    # place widgets
    lbl.pack(side=tk.TOP)
    frame_date.pack(anchor="w",pady=2,padx=2)
    frame_MY.pack(anchor="w",pady=2,padx=2)
    frame_path.pack(anchor="w",pady=2,padx=2)
    frame_progName.pack(anchor="w",pady=2,padx=2)
    frame_milestone.pack(anchor="w",pady=2,padx=2)
    frame_releaseType.pack(anchor="w",pady=2,padx=2)
    
    root.mainloop()

if __name__ == "__main__":
    create_window()

