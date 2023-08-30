import os, sys, getopt, shutil, time

# Syncing ONLY one-way - source to replica; NOT both ways!

# Paths for the source and replica folder and log file
source = "source/"
replica = "replica/"

log = open("log.txt", "a")


# Functions for the file Copy_Create and Delete operations (*Probably will need to add a function or statement to check if the files were changed in some way*)

def copy_create(src, target):
  # Listing the files from src and target folders
  files_in_src = os.listdir(src)
  files_in_target = os.listdir(target)

  # Checking if the src_file is in the target folder
  # If not, create the file (or files) that are not in the target folder  
  for src_file in files_in_src:
    if src_file not in files_in_target:
      print(f"File {src_file} doesn't exist in {target} folder!")
      shutil.copy(src=os.path.join(source, src_file), dst=os.path.join(target, src_file))
      print(f"File/s were created in {target} folder!")
  txt = f"Creating in {target} from {src} forlder!\n"
  log.write(txt)

  print(txt)


def delete(src, target):
  # Listing the files from src and target folders
  files_in_src = os.listdir(src)
  files_in_target = os.listdir(target)

  delete_these = []

  # Checking if the target_file is in the source folder
  # If not, delete the file (or files) that are not in the target folder  
  for target_file in files_in_target:
    if target_file not in files_in_src:
      print(f"File {target_file} doesn't exist in {src} folder!")
      delete_these.append(target_file)
    
    txt = "No files are missing or being deleted!"
    print(txt)

  for delete_this in delete_these:
    file_path = os.path.join(target, delete_this)
    os.remove(file_path)
    print(f"File/s were deleted from {target} folder!")
  
    txt = f"Deleting from {target} forlder!\n"
  
  log.write(txt)

  print(txt)


def sync_func(src, target):

  print("Bruh")

copy_create(src=source, target=replica)
delete(src=source, target=replica)

log.close()