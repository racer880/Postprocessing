from tkinter import *
import os

class CreatePath():

   # --------------------------------------------------------------------------------------------
   # Constructor
   def __init__(self, path, directory_folder, sub_folder_1, sub_folder_2, sub_folder_3, sub_folder_4, sub_folder_5):
      super().__init__()

      try:
         os.makedirs(path + '/' + directory_folder)
      except FileExistsError:
         print("Directory folder already create!")
         pass

      if sub_folder_1 is not None:
         try:
            os.makedirs(path + '/' + directory_folder + '/' + sub_folder_1)
         except FileExistsError:
            print("Sub folder 1 already create!")
            pass

      if sub_folder_2 is not None:
         try:
            os.makedirs(path + '/' + directory_folder + '/' + sub_folder_2)
         except FileExistsError:
            print("Sub folder 2 already create!")
            pass

      if sub_folder_3 is not None:
         try:
            os.makedirs(path + '/' + directory_folder + '/' + sub_folder_3)
         except FileExistsError:
            print("Sub folder 3 already create!")
            pass

      if sub_folder_4 is not None:
         try:
            os.makedirs(path + '/' + directory_folder + '/' + sub_folder_4)
         except FileExistsError:
            print("Sub folder 4 already create!")
            pass

      if sub_folder_5 is not None:
         try:
            os.makedirs(path + '/' + directory_folder + '/' + sub_folder_5)
         except FileExistsError:
            print("Sub folder 5 already create!")
            pass




