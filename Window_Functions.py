from tkinter import *
from Test_Case_Functions import *
import threading
from tkinter import ttk


def Window_One():
    root = Tk()  # Creates the window; root is main window
    # Window size & Window priority
    root.geometry('900x600')
    root.attributes("-topmost", True)

    # TITLE OF FRAME & ICON
    root.title("SHIELD: A Next Generation Network Configuration Tool")
    root.iconbitmap("icon.ico")

    # CENTERING WINDOW
    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 3.7 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 4 - windowHeight / 2)
    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))

    # Text in window ; Welcome message
    Label1 = Label(root, text="\n\n\n WELCOME TO SHIELD", font="Helvetica 25 bold").pack()

    image = PhotoImage(file="icon.png")
    label = Label(image=image)
    label.pack()

    Label2 = Label(root, text=" \n A Network Configuration Testing Tool ", font="Helvetica 14 bold italic").pack()
    Label3 = Label(root, text="\n To start testing your firewall, click start to proceed.\n\n", font="Helvetica 13 italic").pack()


    # Invisible "containers" that goes into root
    topFrame = Frame(root)
    topFrame.pack()  #pack makes it display into the window

    # Buttons
    button2 = Button(root, text="Start", width=16, command=lambda: transition_one(root)).pack()
    button1 = Button(root, text="Exit",width=16, command = root.destroy).pack()


    root.mainloop()

#########################
# CHOOSE TEST CASE WINDOW
#########################
def click_run(root):
    if (URLenable == 1 or FileBlocking_enable == 1 or (anti_virus_enable == 1 and anti_virus_enable_for_input ==1)):
        root.destroy()
        transition_from_selection_to_loading()

def transition_one(root):
    root.destroy()
    global FileBlocking_enable
    FileBlocking_enable = 0

    global URLenable
    URLenable = 0

    global FileBlocking_finished
    FileBlocking_finished = 0

    global URL_Finished
    URL_Finished = 0

    global POP3_no_attachments_enable
    POP3_no_attachments_enable = 0

    global IMAP4_with_A_enable
    IMAP4_with_A_enable = 0

    global IMAP4_without_A_enable
    IMAP4_without_A_enable = 0

    global anti_virus_enable
    anti_virus_enable = 0

    global anti_virus_enable_for_input
    anti_virus_enable_for_input = 0

    Window_Two()

def Window_Two():
    root = Tk()  # Creates the window; root is main window
    # Window size & Window priority
    root.geometry('900x600')
    root.attributes("-topmost", True)

    # TITLE OF FRAME & ICON
    root.title("SHIELD: A Next Generation Network Configuration Tool")
    root.iconbitmap("icon.ico")

    # CENTERING WINDOW
    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 3.7 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 4 - windowHeight / 2)
    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))

    # Text in window
    Label1 = Label(root,text="\n\n\n\n\n LIST OF TEST CASES", font="Helvetica 16 bold").pack()
    Label2 = Label(root,text="\n \n Select one or more of the following options and click on run to view the results.\n",
                   font="Helvetica 13 italic").pack()

    # Invisible "containers" that goes into root
    topFrame = Frame(root)
    topFrame.pack() #pack makes it display into the window


    # CHECKBOXES
    checkedA = Checkbutton(root, text="File Blocking",command = file_blocking_selects).pack()
    checkedB = Checkbutton(root, text="Antivirus Monitoring", command = antivirus_select).pack()
    checkedC = Checkbutton(root, text="URL Filtering ", command = URLFilter_selects).pack()

    Lable13 = Label(root, text = "\n \n").pack()
    # Buttons
    button2 = Button(root, text="Run", width=16, command=lambda: click_run(root)).pack()
    button1 = Button(root, text="Cancel",width=16, command=root.destroy).pack()


    root.mainloop()

#########################
# URL FILTERING WINDOW
#########################
def URLFilter_selects():
    if URLenable == 1:
        global URLenable
        URLenable = 0
    else:
        Window_GetUrlInput()

def click_UpdateURLs():
    file = open('website_list.txt', 'w')
    file.write(e1.get("1.0", "end"))

def Window_GetUrlInput():
    root = Tk() #Creates the window; root is main window
    #Window size & Window priority
    root.geometry('800x500')
    root.attributes("-topmost",True)

    #TITLE OF FRAME & ICON
    root.title("SHIELD: A Next Generation Network Configuration Tool")
    root.iconbitmap("icon.ico")

    # CENTERING WINDOW
    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 3.3 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 3.3 - windowHeight / 2)
    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))

    #Text in window
    Label1 = Label(root, text="\n\n\n You have selected: URL Filtering\n", font="Helvetica 16 bold").pack()
    Label2 = Label(root, text="Step 1: Provide a list of your URLs.",font="Helvetica 13").pack()
    Label3 = Label(root, text="Step 2: Click on Update URLs.", font="Helvetica 13 ").pack()
    Label4 = Label(root, text="Step 3: Click on Return. \n", font="Helvetica 13 ").pack()
    Label5 = Label(root, text="Files :", font="Helvetica 16 bold").pack()
    Label6 = Label(root, text="(Example -> https://www.telus.com)\n", font="Helvetica 13 italic").pack()

    #Invisible "containers" that goes into root
    topFrame=Frame(root)
    topFrame.pack() #pack makes it display into the window
    bottomFrame=Frame(root)
    bottomFrame.pack(side=BOTTOM)

    #TEXTBOX
    global e1
    txt1=open("website_list.txt").read()

    e1 = Text(root)
    e1.pack()

    e1.insert(END,txt1)

    global URLenable
    URLenable = 1

    #Buttons
    button1 = Button(bottomFrame, text="Update URLs", width=16, command=click_UpdateURLs).pack()
    button3 = Button(bottomFrame, text="Return",width=16, command = root.destroy).pack()


    root.mainloop()

#########################
# FILE BLOCKING WINDOW
##########################
def file_blocking_selects():
    if FileBlocking_enable == 1:
        global FileBlocking_enable
        FileBlocking_enable = 0
    else:
        Window_GetFileBlockingInput()

def click_UpdateBlocking():
    file = open('download_list.txt', 'w')
    file.write(e2.get("1.0", "end"))

def Window_GetFileBlockingInput():
    root = Tk()  # Creates the window; root is main window
    # Window size & Window priority
    root.geometry('800x500')
    root.attributes("-topmost", True)

    # TITLE OF FRAME & ICON
    root.title("SHIELD: A Next Generation Network Configuration Tool")
    root.iconbitmap("icon.ico")

    # CENTERING WINDOW
    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 3.3 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 3.3 - windowHeight / 2)
    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))

    # Text in window
    Label1 = Label(root, text="\n\n\n You have selected: File Blocking", font="Helvetica 16 bold").pack()
    Label2 = Label(root, text="Step 1: Provide a list of your files.", font="Helvetica 13").pack()
    Label3 = Label(root, text="Step 2: Click on Update Files.", font="Helvetica 13 ").pack()
    Label4 = Label(root, text="Step 3: Click on Return. \n", font="Helvetica 13 ").pack()
    Label5 = Label(root, text="Files :", font="Helvetica 16 bold").pack()

    # Invisible "containers" that goes into root
    topFrame = Frame(root)
    topFrame.pack()  # pack makes it display into the window
    bottomFrame=Frame(root)
    bottomFrame.pack(side=BOTTOM)


    # TEXTBOX
    global e2
    txt2=open("download_list.txt").read()

    e2 = Text(root)
    e2.pack()

    e2.insert(END,txt2)

    global FileBlocking_enable
    FileBlocking_enable = 1

    # Buttons
    button1 = Button(bottomFrame, text="Update Files", width=16, command=click_UpdateBlocking).pack()
    button3 = Button(bottomFrame, text="Return",width=16, command = root.destroy).pack()


    root.mainloop()

#########################
# ANTIVIRUS WINDOW
#########################
def antivirus_select():
    if anti_virus_enable_for_input == 1:
        global anti_virus_enable_for_input
        anti_virus_enable_for_input = 0
    else:
        Window_AntiVirus()

def Window_AntiVirus(): #1st window; choose default or custom
    root = Tk()  # Creates the window; root is main window
    # Window size & Window priority
    root.geometry('800x500')
    root.attributes("-topmost", True)

    # TITLE OF FRAME & ICON
    root.title("SHIELD: A Next Generation Network Configuration Tool")
    root.iconbitmap("icon.ico")

    # CENTERING WINDOW
    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 3.3 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 3.3 - windowHeight / 2)
    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))

    # Invisible "containers" that goes into root
    topFrame = Frame(root)
    topFrame.pack()  #pack makes it display into the window
    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)

    #Labels & Buttons
    Label1 = Label(root, text="You have selected: Anti Virus", font="Helvetica 16 bold").pack()
    Label2 = Label(root, text="\n\nStep 1: Please choose at least one of the files listed below", font="Helvetica 13").pack()
    Label3 = Label(root, text="Step 2: Click Return\n", font="Helvetica 13").pack()


    checkbutton1 = Checkbutton(root, text="Uses IMAP4 Protocol with no attachments",command= IMAP4_without_enable).pack()
    checkbutton2 = Checkbutton(root, text="Uses IMAP4 Protocol with attachments", command=IMAP4_with_enable).pack()
    checkbutton3 = Checkbutton(root, text="Uses POP3 Protocol with no attachments", command=POP3_no_A_enable).pack()

    Lable13 = Label(root, text="\n \n").pack()

    button1 = Button(root, text="Return", command=root.destroy, width=16).pack()
    button2 = Button(root, text="Cancel", command=root.destroy, width=16).pack()

    global anti_virus_enable_for_input
    anti_virus_enable_for_input = 1

    root.mainloop()

def POP3_no_A_enable():
    global anti_virus_enable
    anti_virus_enable = 1
    global POP3_no_attachments_enable
    POP3_no_attachments_enable = 1

def IMAP4_with_enable():
    global anti_virus_enable
    anti_virus_enable = 1
    global IMAP4_with_A_enable
    IMAP4_with_A_enable = 1

def IMAP4_without_enable():
    global anti_virus_enable
    anti_virus_enable = 1
    global IMAP4_without_A_enable
    IMAP4_without_A_enable = 1

#########################
# LOADING PAGE
##########################
# we define our Main Functions, which will first define root, then call for call for "task(root)"
# --- that's your progressbar, and then call for thread1 simultaneously which will  execute your process_of_unknown_duration
# and at the end destroy/quit the root.
def Loading_Page():

    root = Tk()
    root.geometry('400x150')
    root.attributes("-topmost", True)
    # TITLE OF FRAME & ICON
    root.title("SHIELD: A Next Generation Network Configuration Tool")
    root.iconbitmap("icon.ico")

    # CENTERING WINDOW
    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 2.4 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2.2 - windowHeight / 2)
    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))

    # Content in window ; Welcome message & Shield logo
    Label2 = Label(root, text=" \n\n Program is running ", font="Helvetica 14 bold italic").pack()
    Label3 = Label(root, text="Please wait then click continue. \n",
                   font="Helvetica 13 italic").pack()

    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)

    global progressbar
    progressbar = ttk.Progressbar(orient=HORIZONTAL, length=200, mode='indeterminate')
    progressbar.pack()
    progressbar.start()

    global loading_button
    loading_button = Button(bottomFrame, text="Continue", command=lambda : transition_from_loading_to_result(root), width=16)

    root.mainloop()

# Define the process of unknown duration with root as one of the input. And once done, add root.quit() at the end.
def process_of_unknown_duration():
    setup()
    if URLenable == 1:
        URLFilter()

    if FileBlocking_enable == 1:
        FileBlocking()

    if anti_virus_enable == 1:
        anti_virus_folder_setup()

    if IMAP4_without_A_enable == 1:
        IMAP4_without_attachment()

    if IMAP4_with_A_enable == 1:
        IMAP4_with_attachments()

    if POP3_no_attachments_enable == 1:
        POP3_no_attachments()

    loading_button.pack(side=RIGHT, anchor='se')
    progressbar.destroy()

def transition_from_selection_to_loading():
    global finished_computing
    finished_computing = 0
    t1 = threading.Thread(target=process_of_unknown_duration)
    t1.start()

    Loading_Page()

def transition_from_loading_to_result(root):
    root.destroy()
    Window_Show_Results()

#########################
# WINDOW DISPLAYS THE RESULTS
##########################
def Window_Show_Results():

    root = Tk()  # Creates the window; root is main window
    # Window size & Window priority
    root.geometry('800x500')
    root.attributes("-topmost", True)

    # TITLE OF FRAME & ICON
    root.title("SHIELD: A Next Generation Network Configuration Tool")
    root.iconbitmap("icon.ico")

    # CENTERING WINDOW
    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 3.3 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 3.3 - windowHeight / 2)
    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))

    Label(root, text="\n \n \n TEST RESULTS", font="Helvetica 16 bold").pack()  # message on screen
    Label(root, text="\n Please see the complete results in the following file: ", font="Helvetica 12").pack()  # message on screen
    t1 = Text(root, width=58, height=2)
    t1.pack()
    filename=get_file_name()
    #print(filename)
    sys.stdout = t1.insert(END, filename)

    button1 = Button(root, text="Return", width=16, command=lambda: transition_one(root)).pack()
    button2 = Button(root, text="Exit", width=16, command=root.destroy).pack()


    root.mainloop()
