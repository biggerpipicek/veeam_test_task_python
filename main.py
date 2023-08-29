import os
import sys
import shutil
import time

# Syncing ONLY one-way - source to replica; NOT both ways!

# Paths for the source and replica folder and log file
source = "source/"
replica = "replica/"

log = open("log.txt", "a")


# Functions for the Copy, Create and Delete operations (*Probably will need to add a function or statement to check if the files were changed in some way*)
def copy(src, target):
  txt = f"Copying to {target} from {src} forlder!"
  log.write(txt)

  print(txt)


def create(src, target):
  txt = f"Creating in {target} from {src} forlder!"
  log.write(txt)

  print(txt)


def delete(src, target):
  txt = f"Deleting from {src} and {target} folder!"
  log.write(txt)

  print(txt)


def sync_func(src, target):

  print("Bruh")


def all_commands():
  commands = []
  def command(cmd):
    def folder_paths():
      print("Folder paths")
    def sync_interval():
      print("Syncing interval")
    def log_file_path():
      print("log file path")

copy(src=source, target=replica)
create(src=source, target=replica)
delete(src=source, target=replica)

log.close()
