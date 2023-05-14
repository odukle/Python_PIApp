import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import json

LABEL_WIDTH = 24
RECORDS_JSON = "records.json"

def create_window():
    root = tk.Tk()
    root_pane = tk.PanedWindow(root,orient=tk.HORIZONTAL,width=1500,height=400)

    ##################### Create Frames for widget groups #############################
    frame_recordFields = tk.Frame(root_pane)
    frame_recordFields.pack(side=tk.LEFT,anchor="w",pady=2,padx=2,fill=tk.BOTH,expand=True)

    frame_tree = tk.Frame(root_pane)
    frame_tree.pack(side=tk.LEFT,pady=2,fill=tk.BOTH,expand=True)

    root_pane.add(frame_recordFields)
    root_pane.add(frame_tree)
    root_pane.config(sashwidth=5)
    root_pane.pack(fill=tk.BOTH, expand=True)

    ##################### Create widgets for Record Fields ###############################

    #AddDate
    frame_dateAdded = tk.Frame(frame_recordFields)
    label_dateAdded = tk.Label(frame_dateAdded, text="Date when release got added",width=LABEL_WIDTH,anchor="w")
    addDatePicker = DateEntry(frame_dateAdded)
    label_dateAdded.pack(side=tk.LEFT)
    addDatePicker.pack(side=tk.LEFT)
    frame_dateAdded.pack(anchor="w",pady=2,padx=2)

    #ModelYear
    frame_MY = tk.Frame(frame_recordFields)
    label_MY = tk.Label(frame_MY,text="Pick Model Year",width=LABEL_WIDTH,anchor="w")
    myOptions = ["MY21","MY22","MY23","MY24","MY25","MY26"]
    combo_modelYear = ttk.Combobox(frame_MY,values=myOptions)
    combo_modelYear.set(myOptions[0])
    label_MY.pack(side=tk.LEFT)
    combo_modelYear.pack(side=tk.LEFT)
    frame_MY.pack(anchor="w",pady=2,padx=2)

    #Path
    frame_path = tk.Frame(frame_recordFields)
    label_path = tk.Label(frame_path,text="Pick path",width=LABEL_WIDTH,anchor="w")
    pathOptions = ["GEN1","GEN2","GEN3","GEN4"]
    combo_path = ttk.Combobox(frame_path,values=pathOptions)
    combo_path.set(pathOptions[0])
    label_path.pack(side=tk.LEFT)
    combo_path.pack(side=tk.LEFT)
    frame_path.pack(anchor="w",pady=2,padx=2)

    #ProgramName
    frame_progName = tk.Frame(frame_recordFields)
    label_progName = tk.Label(frame_progName,text="Enter Program Name",width=LABEL_WIDTH,anchor="w")
    entry_progName = tk.Entry(frame_progName)
    label_progName.pack(side=tk.LEFT)
    entry_progName.pack(side=tk.LEFT)
    frame_progName.pack(anchor="w",pady=2,padx=2)

    #Milestone
    frame_milestone = tk.Frame(frame_recordFields)
    label_milestone = tk.Label(frame_milestone,text="Enter Milestone",width=LABEL_WIDTH,anchor="w")
    entry_milestone = tk.Entry(frame_milestone)
    label_milestone.pack(side=tk.LEFT)
    entry_milestone.pack(side=tk.LEFT)
    frame_milestone.pack(anchor="w",pady=2,padx=2)

    #ReleaseType
    frame_releaseType = tk.Frame(frame_recordFields)
    label_releaseType = tk.Label(frame_releaseType,text="Pick Release Type",width=LABEL_WIDTH,anchor="w")
    releaseTypeOptions = ["Full","Delta","Experimental"]
    combo_releaseType = ttk.Combobox(frame_releaseType,values=releaseTypeOptions)
    combo_releaseType.set(releaseTypeOptions[0])
    label_releaseType.pack(side=tk.LEFT)
    combo_releaseType.pack(side=tk.LEFT)
    frame_releaseType.pack(anchor="w",pady=2,padx=2)

    #ReleaseDate
    frame_releaseDate = tk.Frame(frame_recordFields)
    label_releaseDate = tk.Label(frame_releaseDate, text="Release date",width=LABEL_WIDTH,anchor="w")
    releaseDatePicker = DateEntry(frame_releaseDate)
    label_releaseDate.pack(side=tk.LEFT)
    releaseDatePicker.pack(side=tk.LEFT)
    frame_releaseDate.pack(anchor="w",pady=2,padx=2)

    #Status
    frame_status = tk.Frame(frame_recordFields)
    label_status = tk.Label(frame_status,text="Pick status",width=LABEL_WIDTH,anchor="w")
    statusOptions = ["Delivered","Cancelled","CCB Approved"]
    combo_status = ttk.Combobox(frame_status,values=statusOptions)
    combo_status.set(statusOptions[0])
    label_status.pack(side=tk.LEFT)
    combo_status.pack(side=tk.LEFT)
    frame_status.pack(anchor="w",pady=2,padx=2)

    # Summary of changes
    frame_summaryOfChanges = tk.Frame(frame_recordFields)
    label_summaryOfChanges = tk.Label(frame_summaryOfChanges,text="Enter summary of changes",width=LABEL_WIDTH,anchor="w")
    entry_summaryOfChanges = tk.Entry(frame_summaryOfChanges)
    label_summaryOfChanges.pack(side=tk.LEFT)
    entry_summaryOfChanges.pack(side=tk.LEFT)
    frame_summaryOfChanges.pack(anchor="w",pady=2,padx=2)

    # Frame for Add/Edit record Buttons
    frame_btnAddEditRecord = tk.Frame(frame_recordFields)
    frame_btnAddEditRecord.pack(anchor="w",pady=2,padx=2)

    ##################### Create Tree Widget ########################################

    # Records' Tree
    tree = ttk.Treeview(frame_tree,show="headings")
    tree.pack(fill=tk.BOTH,expand=True)
    fetch_records(tree)

    ####################### Create Button Widgets ######################

    # Button add new record
    btnAddRecord = tk.Button(frame_btnAddEditRecord,text="Add new record",
                             command=lambda: save_record(addDatePicker.get_date(),combo_modelYear.get(),combo_path.get(),
                                                         entry_progName.get(),entry_milestone.get(),combo_releaseType.get(),
                                                         releaseDatePicker.get_date(),combo_status.get(),entry_summaryOfChanges.get(),tree))
    # btnAddRecord.pack(anchor="w",side=tk.LEFT,padx=2,pady=2)
    btnAddRecord.grid(row=1,column=1)

    # Button edit existing record
    btnEditRecord = tk.Button(frame_btnAddEditRecord,text="Edit existing record")
    # btnEditRecord.pack(anchor="w",side=tk.LEFT,padx=2,pady=2)
    btnEditRecord.grid(row=1,column=2)

    # Button fetch records
    btnFetchRecord = tk.Button(frame_btnAddEditRecord,text="Fetch records",command=lambda: fetch_records(tree))
    # btnFetchRecord.pack(anchor="w",side=tk.LEFT,padx=2,pady=2)
    btnFetchRecord.grid(row=1,column=3)

    # Button delete records
    btnDeleteRecords = tk.Button(frame_btnAddEditRecord,text="Delete selected records",command=lambda: delete_records(tree),
                                 state="disabled")
    # btnDeleteRecords.pack(anchor="w",side=tk.BOTTOM,padx=2,pady=2)
    btnDeleteRecords.grid(row=2,column=2,pady=8)
    tree.bind('<<TreeviewSelect>>',lambda event: on_tree_select(event,tree,btnDeleteRecords))

    root.mainloop()

def save_record(dateAdded,modelYear,path,progName,milestone
                ,releaseType,releaseDate,status,summaryOfChanges,tree):
    data = {
        "dateAdded": dateAdded.strftime("%Y-%m-%d"),
        "modelYear": modelYear,
        "path": path,
        "progName": progName,
        "milestone": milestone,
        "releaseType": releaseType,
        "releaseDate": releaseDate.strftime("%Y-%m-%d"),
        "status": status,
        "summaryOfChanges": summaryOfChanges
    }

    with open(RECORDS_JSON, 'r') as f:
        json_data = f.read()
    
    records = json.loads(json_data)
    records.append(data)
    tree.insert("",tk.END, values=list(data.values()))
    tree.update()

    with open(RECORDS_JSON, "w") as f:
        json.dump(records, f)

def fetch_records(tree):

    with open(RECORDS_JSON, 'r') as f:
        json_data = f.read()
    
    records = json.loads(json_data)
    tree["columns"] = list(records[0].keys())
    
    for column in tree["columns"]:
        if column == "summaryOfChanges":
            width = 200
        else:
            width = 75
        tree.column(column,width=width)
        tree.heading(column, text=column)

    tree.delete(*tree.get_children())
    for row in records:
        tree.insert("",tk.END,values=list(row.values()))

    tree.update()

def on_tree_select(event,tree,button):
    cur_item = tree.focus()
    if cur_item:
        button.configure(state='normal')
        button.update()
    else:
        button.configure(state='disabled')
        button.update()

def delete_records(tree):
    selected_items = tree.selection()
    with open(RECORDS_JSON) as f:
        data = json.load(f)
    
    for item in reversed(selected_items):
        del data[tree.index(item)]

    with open(RECORDS_JSON, 'w') as f:
        json.dump(data, f)
    
    fetch_records(tree)

if __name__ == "__main__":
    create_window()