'''
Created on Oct 15, 2018

@author: david
'''
import tempfile
import win32api
import win32print




print(win32print.GetPrinter(win32print.OpenPrinter(win32print.GetDefaultPrinter)))


#===============================================================================
# filename = tempfile.mktemp (".txt")
# open (filename, "w").write ("This is a test")
# win32api.ShellExecute (
#   0,
#   "printto",
#   filename,
#   '"%s"' % win32print.GetDefaultPrinter (),
#   ".",
#   0
# )
#===============================================================================

