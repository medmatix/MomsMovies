'''
MomsMovies.py
Created on Oct 8, 2018
@summary: A project to construct and access a Home Movies Database. Links to IMDB database for movie details. 
@version: 0.01
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
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
import sys as sys
# ##########################
# Classes
# ##########################
class MomsMovies(object):
    ''' 
    Main class module for Movies Database Application
    '''
    def __init__(self):
        '''
        Constructor for Mom
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
        db.execute("CREATE TABLE IF NOT EXISTS movies (MovieNumber INTEGER, MovieTitle STRING(60), Genre STRING(10), RunTime INT(4), Year DATE,Rating STRING(3), OnlineId STRING(50))")
        db.close()
        
    def getAllMovies(self):
        '''
        Return all records
        '''
        AllMovies = list() 
        db = sqlite3.connect('MomsMovies.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM movies")
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
        cursor.execute('SELECT * FROM Movies WHERE MovieTitle LIKE ?', (partialTitle,))
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
        cursor.execute('SELECT * FROM Movies WHERE MovieNumber = ?', (mNumber,))
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
        cursor.execute('SELECT * FROM Movies WHERE Genre = ?', (mGenre,))
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
        cursor.execute('SELECT * FROM Movies WHERE Rating = ?', (mRating,))
        for row in cursor:
            mQuery.append(row)
        db.close()
        return mQuery
    
    def deleteMoviefromList(self, mNumber):
        '''
        Remove a movie entry
        '''
        print(self)
        db = sqlite3.connect('MomsMovies.db')
        print("Opened database successfully")
        thisMovie = self.findMoviebyNumber(mNumber)
        #=======================================================================
        # print("Delete\? {}".format(thisMovie))
        # ans = input("Do you want to go ahead? (y/n)")
        # if ans == 'y':
        #=======================================================================
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
    #===========================================================================
    # def deleteMoviefromList(self, mNumber):
    #     '''
    #     Remove a movie entry
    #     '''
    #     db = sqlite3.connect('MomsMovies.db')
    #     print("Opened database successfully")
    #     thisMovie = self.findMoviebyNumber(mNumber)
    #     print("Delete\? {}".format(thisMovie))
    #     ans = input("Do you want to go ahead? (y/n)")
    #     if ans == 'y':
    #         db.execute("DELETE FROM movies WHERE movieNumber = ?", (mNumber,))
    #         db.commit()
    #         print("Total number of rows deleted :{}".format(db.total_changes))
    #         print("Operation done successfully")
    #         db.close() 
    #     else:
    #         print("Delete aborted . . .")
    #         db.close
    #         return
    #===========================================================================
        
    def updateMovieinList(self, row):
        '''
        Edit a movie entry
        '''
        db = sqlite3.connect('MomsMovies.db')
        db.execute("UPDATE movies SET (movieTitle = ?, Genre = ?, RunTime = ?, Year = ?, Rating = ?, OnlineId = ?) WHERE movieNumber = ?", (row[1], row[2], row[3], row[4], row[5], row[6], row[0]))
        db.commit
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
        
    def do_showAll(self):
        listAll = self.getAllMovies()
        print(listAll)
        for row in listAll:
            self.scrolList.insert(tk.END, row)
        # self.scrolList.insert(tk.END, listAll)
        
    def do_delete_rec(self):
        # mNumber=input("Movie number to delete;")
        mNumber = simpledialog.askinteger("Delete Movie", "Movie Number to Delete?")
        self.deleteMoviefromList(mNumber)
        
    def do_addDummyRec(self):
        ''' Add a dummy test record'''        
        imovieNumber = 999
        smovieTitle = 'Terrible-pan'
        sGenre = 'AD'
        iRunTime = 127
        dYear = 1980
        sRating = 'R'
        sOnlineId = 'tt99999999'
        row = (imovieNumber, smovieTitle, sGenre, iRunTime, dYear, sRating, sOnlineId)
        mm.addMovietoList(row)    
        mNumber = imovieNumber
        movieTitle = mm.findMoviebyNumber(mNumber)
        if movieTitle.__len__()==0:
            print("No Records added with this ID number")
        else: 
            print(movieTitle)
            
    # #####################################
    # Independent Diablogs and Pop-ups
    # #####################################
    def info(self):
        mBox.showinfo('About Mom\'s Movies, ' , 'Debby\'s Own Movie List Application\n\n (c) David A York, 2018\n http:crunches-data.appspot.com \nVersion: 0.1, development version 0.03a \nlicense: MIT')
    
        
    # #####################################
    # GUI Widgets Creation and interface methods 
    # #####################################
    
    def createWidgets(self):  
        '''
        GUI interface creation
        '''
        frm = ttk.Frame(self.win, width= 400, height=400)            # Create a tab
        frm.pack()
        
        # Creating a container frame to hold tab2 widgets ============================
        self.list = ttk.LabelFrame(frm, text=' Movie(s) ', width=56)
        self.list.grid(column=0, row=0, padx=8, pady=4, sticky='W')
        
        self.listctl = ttk.LabelFrame(self.list, width=56)
        self.listctl.grid(column=0, row=0, padx=8, pady=4, sticky='W')
        
        scrolW1  = 56; scrolH1  =  20
        self.scrolList = scrolledtext.ScrolledText(self.list, width=scrolW1, height=scrolH1, wrap=tk.WORD)
        self.scrolList.grid(column=0, row=6, padx=4, pady=4, sticky='WE', columnspan=3)
        
        self.action_clrlist = ttk.Button(self.listctl, text="CLEAR")
        self.action_clrlist.grid(column=0, row=0, padx=4, pady=6)
        
        self.action_prtlist = ttk.Button(self.listctl, text="PRINT")
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
        listMenu.add_command(label="New")
        listMenu.add_command(label="Open")
        listMenu.add_command(label="Save")
        listMenu.add_command(label="Copy")
        listMenu.add_separator()
        listMenu.add_command(label="Exit", command=self._quit)
        menuBar.add_cascade(label="List", menu=listMenu)
        
        # Add an Edit Menu
        editMenu = Menu(menuBar, tearoff=0)
        editMenu.add_command(label="Cut")
        editMenu.add_command(label="Copy")
        editMenu.add_command(label="Paste")
        editMenu.add_command(label="Delete")
        editMenu.add_command(label="Clear All")
        editMenu.add_command(label="Select")
        editMenu.add_separator()
        editMenu.add_command(label="Enter")
        editMenu.add_command(label="Options")
        menuBar.add_cascade(label="Edit", menu=editMenu)
        
        # Add an View Menu
        viewMenu = Menu(menuBar, tearoff=0)
        viewMenu.add_command(label="View a Number")
        viewMenu.add_command(label="View a Title") #, command=lambda:displaydfTable(self))
        viewMenu.add_command(label="View a Genre")
        viewMenu.add_command(label="View a Rating  ")
        viewMenu.add_command(label="View All Numerically", command=lambda: self.do_showAll())
        viewMenu.add_command(label="View All Alphabetically")
        menuBar.add_cascade(label="View", menu=viewMenu)
                      
        # Add an tools Menu
        toolsMenu = Menu(menuBar, tearoff=0)
        toolsMenu.add_command(label="Add Movie")
        toolsMenu.add_command(label="Add Dummy", command=lambda: self.do_addDummyRec())
        toolsMenu.add_command(label="Delete Movie", command=lambda: self.do_delete_rec())
        toolsMenu.add_command(label="Sort")
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
    # #############################
    # TEST fetching All records
    # #############################
    # AllMovies = mm.getAllMovies()
    # print(AllMovies)
    
    # ########################################
    # TEST record retrieval by partial title
    # ########################################
    #===========================================================================
    # partialTitle = '%dog%'
    # movieTitle = mm.findMoviebyTitle(partialTitle)
    # if movieTitle.__len__()==0:
    #     print("No Records with this in title")
    # else: 
    #     print(movieTitle)
    #===========================================================================
    
    # ##################################
    # TEST record retrieval bu number
    # ##################################
    #===========================================================================
    # mNumber = 275
    # movieTitle = mm.findMoviebyNumber(mNumber)
    # if movieTitle.__len__()==0:
    #     print("No Records with this ID number")
    # else: 
    #     print(movieTitle)
    #===========================================================================
    
    ###############################
    # TEST record addition
    ###############################
    # (movieNumber int, movieTitle string, Genre string, RunTime int, Year date, Rating string, OnlineId string)
    # (int,string,string,int,date,string,string)
    
    #===========================================================================
    # imovieNumber = 843
    # smovieTitle = 'Shogun'
    # sGenre = 'AD DR'
    # iRunTime = 125
    # dYear = 1980
    # sRating = 'PG'
    # sOnlineId = 'tt0083069'
    # row = (imovieNumber, smovieTitle, sGenre, iRunTime, dYear, sRating, sOnlineId)
    # mm.addMovietoList(row)    
    # mNumber = imovieNumber
    # movieTitle = mm.findMoviebyNumber(mNumber)
    # if movieTitle.__len__()==0:
    #     print("No Records added with this ID number")
    # else: 
    #     print(movieTitle)
    #===========================================================================
    
    # ##################################
    # TEST record retrieval bu Genre
    # ##################################
    
    #===========================================================================
    # mGenre = "AD"
    # movieTitle = mm.findMoviesbyGenre(mGenre)
    # if movieTitle.__len__()==0:
    #     print("No Records for this Genre")
    # else: 
    #     for row in movieTitle:
    #         print(row)
    #===========================================================================
    
    # ##################################
    # TEST record retrieval by Rating
    # ##################################
    
    #===========================================================================
    # mRating = "R"
    # movieTitle = mm.findMoviesbyRating(mRating)
    # if movieTitle.__len__()==0:
    #     print("No Records for this Genre")
    # else: 
    #     for row in movieTitle:
    #         print(row)
    #===========================================================================
    
    #===========================================================================
    # imovieNumber = 999
    # smovieTitle = 'Terrible-pan'
    # sGenre = 'AD'
    # iRunTime = 127
    # dYear = 1980
    # sRating = 'R'
    # sOnlineId = 'tt99999999'
    # row = (imovieNumber, smovieTitle, sGenre, iRunTime, dYear, sRating, sOnlineId)
    # mm.addMovietoList(row)    
    # mNumber = imovieNumber
    # movieTitle = mm.findMoviebyNumber(mNumber)
    # if movieTitle.__len__()==0:
    #     print("No Records added with this ID number")
    # else: 
    #     print(movieTitle)
    #===========================================================================
    
    #===========================================================================
    # mNumber = 999
    # mm.deleteMoviefromList(mNumber)
    #===========================================================================
