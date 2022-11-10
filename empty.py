from win32com.client import gencache
import win32com
shell = win32com.client.gencache.EnsureDispatch('Shell.Application')
print(shell)