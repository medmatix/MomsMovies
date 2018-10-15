'''
MomsMovies.py
Created on Oct 8, 2018
@summary: A project to construct and access a Home Movies Database. Links to IMDB database for movie details. 
@version: 0.02
@author: David York
@contact: 
@copyright: David York 2018
@license: MIT
'''
# ######################
# imports
# ######################
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import simpledialog
from tkinter import font
from datetime import date as dt
import sys
import tempfile
import win32api
import win32print

# ##########################
# Classes
# ##########################

class insertionForm(object):
    '''
    class insertionForm  
    @summary: A form to collect movie data to add to list, and send to addMovietoList function. A Part of MomsMovies application
    @see: refer to main module (MomsMovies) documentation
    created: Oct 14, 2018
        @
    '''
    def __init__(self, goal):
        '''
        Constructor for Add data dialog window
        '''
        
        # Create instance
        self.goal=goal
        self.frm = tk.Tk()
        # Add a title
        self.frm.title("Add a Movie")
        self.aForm()
        self.frm.mainloop() 

    def aForm(self):
        ''' The form '''
        lbfr = ttk.LabelFrame(self.frm, text=' Input Form ')
        lbfr.grid(column=0, row=0, padx=10, pady=10, sticky='W')
        self.lbl0 = tk.Label(lbfr, text="ID: ").grid(column=0, row=0)
        self.e0 = tk.Entry(lbfr, width=4)
        self.e0.grid(column=1, row=0, padx=5, pady=4, sticky='W')
        self.lbl1 = tk.Label(lbfr, text="Title: ").grid(column=0, row=1)
        self.e1 = tk.Entry(lbfr,width=50)
        self.e1.grid(column=1, row=1, padx=5, pady=4, sticky='W')
        self.lbl2 = tk.Label(lbfr, text="Genre: ").grid(column=0, row=2)
        self.e2 = tk.Entry(lbfr,width=12)
        self.e2.grid(column=1, row=2, padx=5, pady=4, sticky='W')
        self.lbl3 = tk.Label(lbfr, text="Run Time: ").grid(column=0, row=3)
        self.e3 = tk.Entry(lbfr,width=4)
        self.e3.grid(column=1, row=3, padx=5, pady=4, sticky='W')
        self.lbl4 = tk.Label(lbfr, text="Year: ").grid(column=0, row=4)
        self.e4 = tk.Entry(lbfr,width=4)
        self.e4.grid(column=1, row=4, padx=5, pady=4, sticky='W')
        self.lbl5 = tk.Label(lbfr, text="Rating: ").grid(column=0, row=5)
        self.e5 = tk.Entry(lbfr,width=5)
        self.e5.grid(column=1, row=5, padx=5, pady=4, sticky='W')
        self.lbl6 = tk.Label(lbfr, text="Online ID: ").grid(column=0, row=6)
        self.e6 = tk.Entry(lbfr,width=12)
        self.e6.grid(column=1, row=6, padx=5, pady=4, sticky='W')
        
        self.btn1 = ttk.Button(lbfr, text="Add", command=lambda: self.on_click()).grid(column=0,row=7,padx=8, pady=4, sticky='W')
        self.btn2 = ttk.Button(lbfr, text="Cancel", command=lambda: self.on_cancel()).grid(column=1,row=7,padx=8, pady=4, sticky='W')
    def on_click(self):
        #mNumber = int(self.e0.get())
        row = (self.e0.get(), self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get(), self.e5.get(),self.e6.get())
        ''' the activation of the form'''
        if self.goal=="add": 
            print("added")
            MomsMovies.addMovietoList(self,row)

        if self.goal=="update": 
            print("updated")
            MomsMovies.updateMovieinList(self,row)
            
        print("Form closed")
        self.frm.destroy()
        
    def on_cancel(self):
        print("Cancelled action")
        self.frm.destroy()

class MomsMovies(object):
    ''' 
    Main class module for Movies Database Application, MomsMovies
    '''
    def __init__(self):
        '''
        Constructor for MomsMovies
        '''
        # Create instance
        self.win = tk.Tk()
           
        # Add a title
        self.win.title("Mom's Movies")
        # Add a icon
        if not sys.platform.startswith('linux'):
            self.win.iconbitmap('medmatix.ico')
            
        # Initialize widgets
        self.createWidgets()
    
    # ########################
    # Database methods
    # ########################
    def createNewList(self):
        '''
        Create a NEW blank database if not already existing
        '''
        db = sqlite3.connect('MomsMovies.db')
        db.execute("CREATE TABLE IF NOT EXISTS movies (MovieNumber INTEGER, MovieTitle STRING(60), Genre STRING(10), RunTime INT(4), Year DATE,Rating STRING(3), ImdbURL STRING(50))")
        db.close()
        
    def getAllMoviesbyNumber(self):
        '''
        Return all records
        '''
        AllMovies = list() 
        db = sqlite3.connect('MomsMovies.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM movies ORDER BY MovieNumber")
        for row in cursor:
            AllMovies.append(row)
        db.close()
        return AllMovies
    
    def getAllMoviesbyTitle(self):
        '''
        Return all records
        '''
        AllMovies = list() 
        db = sqlite3.connect('MomsMovies.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM movies ORDER BY MovieTitle")
        for row in cursor:
            AllMovies.append(row)
        db.close()
        return AllMovies
        
    def addMovietoList(self, row):
        '''
        Add a new movie entry
        '''
        print(row)
        db = sqlite3.connect('MomsMovies.db')
        cursor = db.cursor()
        cursor.execute('INSERT INTO movies (MovieNumber, MovieTitle, Genre, RunTime, Year, Rating, OnlineId) VALUES (?, ?, ?, ?, ?, ?, ?)', (row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
        db.commit()
        db.close()
        
    def findMoviebyTitle(self, partialTitle):
        '''
        Find a record of records with a given Title
        '''
        mQuery = list()
        db = sqlite3.connect('MomsMovies.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Movies WHERE MovieTitle LIKE "%{}%"'.format(partialTitle,))
        for row in cursor:
            mQuery.append(row)
        db.close()
        return mQuery
    def findMoviebyNumber(self, mNumber):
        '''
        Find a record of records with a given Title
        "SELECT ? FROM Data where ?=?", (column, goal, constrain,)
        '''
        mQuery = list()
        db = sqlite3.connect('MomsMovies.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Movies WHERE MovieNumber LIKE "%{}%"'.format(mNumber,))
        for row in cursor:
            mQuery.append(row)
        db.close()
        return mQuery
    
    def findMoviesbyGenre(self, mGenre):
        '''
        Find a record of records with a given Title
        '''
        mQuery = list()
        db = sqlite3.connect('MomsMovies.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Movies WHERE Genre LIKE "%{}%"'.format(mGenre,))
        for row in cursor:
            mQuery.append(row)
        db.close()
        return mQuery

        
    def findMoviesbyRating(self, mRating):
        '''
        Find a record of records with a given Title
        '''
        mQuery = list()
        db = sqlite3.connect('MomsMovies.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Movies WHERE Rating LIKE "{}%"'.format(mRating,))
        for row in cursor:
            mQuery.append(row)
        db.close()
        return mQuery
    
    def findMoviesbyYear(self, mYear):
        '''
        Find a record of records with a given Title
        '''
        mQuery = list()
        db = sqlite3.connect('MomsMovies.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Movies WHERE Year LIKE "{}%"'.format(mYear,))
        for row in cursor:
            mQuery.append(row)
        db.close()
        return mQuery
    
    def deleteMoviefromList(self, mNumber):
        '''
        Remove a movie entry
        '''
        db = sqlite3.connect('MomsMovies.db')
        print("Opened database successfully")
        thisMovie = self.findMoviebyNumber(mNumber)
        if mBox.askokcancel("Delete", thisMovie):
            db.execute("DELETE FROM movies WHERE movieNumber = ?", (mNumber,))
            db.commit()
            print("Total number of rows deleted :{}".format(db.total_changes))
            print("Operation done successfully")
            db.close() 
        else:
            print("Delete aborted . . .")
            db.close
            return
        
    def updateMovieinList(self, row):
        '''
        Edit a movie entry
        '''
        db = sqlite3.connect('MomsMovies.db')
        db.execute("UPDATE movies SET movieNumber=?, MovieTitle=?, Genre=?, RunTime=?, Year=?, Rating=?, OnlineId=?  WHERE MovieNumber=?", (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[0]))
        db.commit()
        print("Total number of rows updated :"), db.total_changes
        db.close()  
    
    # #################################
    # Other functions 
    # #################################   
    # -- Exit GUI cleanly -------------
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        print('run is done, exited normally!')
        exit()
        
    def do_showAllByNumber(self):
        self.do_clearView()
        listAll = self.getAllMoviesbyNumber()
        print(listAll[0])
        for row in listAll:
            self.do_formatedList(row)
            
    def do_showAllByTitle(self):
        self.do_clearView()
        listAll = self.getAllMoviesbyTitle()
        print(listAll[0])
        for row in listAll:
            self.do_formatedList(row)
            
    def do_addMovie(self):
        goal = "add"
        insertionForm(goal)
        
    def do_updateMovie(self):
        goal = "update"
        insertionForm(goal)
        
    def do_delete_rec(self):
        # mNumber=input("Movie number to delete;")
        mNumber = simpledialog.askinteger("Delete Movie", "Movie Number to Delete?")
        self.deleteMoviefromList(mNumber)
        
    def do_clearView(self):
        self.scrolList.delete(1.0,tk.END)
        
    def do_getTitles(self):    
        answer = simpledialog.askstring("Input", "What Titles to search for?", parent=self.win)
        self.do_clearView()
        if answer is not None:
            print("Fetching all like {}".format(answer))
            listTitles = self.findMoviebyTitle(answer)
            for row in listTitles:
                self.do_formatedList(row)
        else:
            print("Cancelled or No search criteria provided") 
            
    def do_getNumbers(self):    
        answer = simpledialog.askinteger("Input", "What number to retrieve?", parent=self.win)
        self.do_clearView()
        if answer is not None:
            listNumbers = self.findMoviebyNumber(answer)
            for row in listNumbers:
                self.do_formatedList(row)
        else:
            print("Cancelled or No search criteria provided")
     
    def do_getYear(self):    
        answer = simpledialog.askstring("Input", "What Year to Search for?", parent=self.win)
        self.do_clearView()
        if answer is not None:
            listYear=self.findMoviesbyYear(answer)
            for row in listYear:
                self.do_formatedList(row)
        else:
            print("Cancelled or No search criteria provided")
           
    def do_getGenres(self):    
        answer = simpledialog.askstring("Input", "What Genre to Search for?", parent=self.win)
        self.do_clearView()
        if answer is not None:
            listGenres=self.findMoviesbyGenre(answer)
            for row in listGenres:
                self.do_formatedList(row)
        else:
            print("Cancelled or No search criteria provided")
            
    def do_getRating(self):    
        answer = simpledialog.askstring("Input", "What Rating to Search for?", parent=self.win)
        self.do_clearView()
        if answer is not None:
            listRating=self.findMoviesbyRating(answer)
            for row in listRating:
                self.do_formatedList(row)
        else:
            print("Cancelled or No search criteria provided")
            
    def do_formatedList(self, row):
        self.scrolList.insert(tk.END,row[0])
        self.scrolList.insert(tk.END,'\t')
        mTitle = row[1]
        titleLength = len(mTitle)+(60-len(mTitle))
        mTitle = mTitle.ljust(titleLength)
        self.scrolList.insert(tk.END,mTitle)
        self.scrolList.insert(tk.END,'\t')
        mGenre = row[2]
        genreLength = len(row[2])+(12-len(row[2]))
        mGenre = mGenre.ljust(genreLength)
        self.scrolList.insert(tk.END,mGenre)
        self.scrolList.insert(tk.END,'\t\t')
        mRuntime = str(row[3])
        runtimeLength = len(mRuntime)+(4-len(mRuntime))
        mRuntime = mRuntime.ljust(runtimeLength)
        self.scrolList.insert(tk.END,mRuntime)
        self.scrolList.insert(tk.END,'\t\t\t')
        self.scrolList.insert(tk.END,row[4])
        self.scrolList.insert(tk.END,'\t\t')
        self.scrolList.insert(tk.END,row[5])
        self.scrolList.insert(tk.END,'\t\t\t')
        self.scrolList.insert(tk.END,row[6])
        self.scrolList.insert(tk.END,'\n')
    
    def do_printViewDefault(self):
        filename = tempfile.mktemp (".txt")
        open (filename, "w").write (self.scrolList.get(1.0, tk.END))
        win32api.ShellExecute (0, "printto",filename, '"%s"' % win32print.GetDefaultPrinter (),  ".",  0)
            
    # #####################################
    # Independent Diablogs and Pop-ups
    # #####################################
    def info(self):
        mBox.showinfo('About Mom\'s Movies, ' , 'Debby\'s Own Movie List Application\n\n (c) David A York, 2018\n http:crunches-data.appspot.com \nVersion: 0.2, development version 0.01b \nlicense: MIT')
    
       
    # #####################################
    # GUI Widgets Creation and interface methods 
    # #####################################
    
    def createWidgets(self):  
        '''
        GUI interface creation
        '''
        frm = ttk.Frame(self.win, width= 400, height=600)            # Create a tab
        frm.pack()
        
        # Creating a container frame to hold tab2 widgets ============================
        self.list = ttk.LabelFrame(frm, text=' Movie(s) ', width=120)
        self.list.grid(column=0, row=0, padx=8, pady=4, sticky='W')
        
        self.listctl = ttk.LabelFrame(self.list, width=56)
        self.listctl.grid(column=0, row=0, padx=8, pady=4, sticky='W')
        
        self.listView = ttk.LabelFrame(self.list, width=120)
        self.listView.grid(column=0, row=6, padx=8, pady=4, sticky='W')
        
        ttk.Label(self.listView, text="ID \t Title \t\t\t\t\t\t\t\t\t\tGenre\t\t     Run Time\tYear\tRating\t\tOnline ID (IMDB)").grid(column=0, row=0, padx=4, pady=4,sticky='W')
        
        scrolW1  = 120; scrolH1  =  20
        self.scrolList = scrolledtext.ScrolledText(self.listView, width=scrolW1, height=scrolH1, wrap=tk.WORD)
        self.scrolList.grid(column=0, row=1, padx=4, pady=4, sticky='WE', columnspan=3)
        
        self.action_clrlist = ttk.Button(self.listctl, text="CLEAR", command=lambda: self.do_clearView())
        self.action_clrlist.grid(column=0, row=0, padx=4, pady=6)
        
        self.action_prtlist = ttk.Button(self.listctl, text="PRINT", command=lambda: self.do_printViewDefault())
        self.action_prtlist.grid(column=1, row=0, padx=4, pady=6)
        
        self.action_loglist = ttk.Button(self.listctl, text="LOG IT")
        self.action_loglist.grid(column=2, row=0, padx=4, pady=6)
        self.action_savelist = ttk.Button(self.listctl, text="SAVE")
        self.action_savelist.grid(column=3, row=0, padx=4, pady=6)
        self.action_loadlist = ttk.Button(self.listctl, text="LOAD")
        self.action_loadlist.grid(column=4, row=0, padx=4, pady=6)
        
              
        # Creating a Menu Bar ---------------------------------------------------------------------
        menuBar = Menu(self.win)
        self.win.config(menu=menuBar)

        # Add menu items
        listMenu = Menu(menuBar, tearoff=0)
        listMenu.add_command(label="New", command=lambda: self.createNewList())
        listMenu.add_command(label="Open")
        listMenu.add_command(label="Save")
        listMenu.add_command(label="Copy Database")
        listMenu.add_separator()
        listMenu.add_command(label="Exit", command=self._quit)
        menuBar.add_cascade(label="List", menu=listMenu)
        
        # Add an Edit Menu
        editMenu = Menu(menuBar, tearoff=0)
        editMenu.add_command(label="Cut")
        editMenu.add_command(label="Copy")
        editMenu.add_command(label="Paste")
        editMenu.add_command(label="Delete")
        editMenu.add_command(label="Clear")
        editMenu.add_command(label="Select")
        editMenu.add_separator()
        editMenu.add_command(label="Options")
        menuBar.add_cascade(label="Edit", menu=editMenu)
        
        # Add an View Menu
        viewMenu = Menu(menuBar, tearoff=0)
        viewMenu.add_command(label="View a Number", command=lambda: self.do_getNumbers())
        viewMenu.add_command(label="View a Title", command=lambda: self.do_getTitles()) #, command=lambda:displaydfTable(self))
        viewMenu.add_command(label="View a Genre", command=lambda: self.do_getGenres())        
        viewMenu.add_command(label="View a Year", command=lambda: self.do_getYear())
        viewMenu.add_command(label="View a Rating ", command=lambda: self.do_getRating())
        viewMenu.add_command(label="View All Numerically", command=lambda: self.do_showAllByNumber())
        viewMenu.add_command(label="View All Alphabetically", command=lambda: self.do_showAllByTitle())
        menuBar.add_cascade(label="View", menu=viewMenu)
                      
        # Add an tools Menu
        toolsMenu = Menu(menuBar, tearoff=0)
        toolsMenu.add_command(label="Add a Movie", command=lambda: self.do_addMovie())
        toolsMenu.add_command(label="Update a Movie", command=lambda: self.do_updateMovie())
        toolsMenu.add_command(label="Delete a Movie", command=lambda: self.do_delete_rec())
        toolsMenu.add_separator()
        toolsMenu.add_command(label="Print Alpha")
        toolsMenu.add_command(label="Print Numeric")
        menuBar.add_cascade(label="Tools", menu=toolsMenu)

        # Add another Menu to the Menu Bar and an item
        helpMenu = Menu(menuBar, tearoff=0)
        helpMenu.add_command(label="Context Help")
        helpMenu.add_command(label="Documentation")
        helpMenu.add_command(label="About", command=self.info)
        menuBar.add_cascade(label="Help", menu=helpMenu)

        # ~ end of menu bar ~ ------------------------------------------------- 
    
if __name__ == '__main__':
    mm = MomsMovies()
    mm.win.mainloop()
    
