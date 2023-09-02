import os, sys, getopt, shutil, time

# Syncing ONLY one-way - source to replica; NOT both ways!

# Paths for the source and replica folder and log file
source = "source/"
replica = "replica/"

log = open("log.txt", "a")


# Functions for the file operations

# Copy_Create function
def copy_create(src, target):
    # Listing the files and directories from src and target folders
    items_in_src = os.listdir(src)
    items_in_target = os.listdir(target)

    for item in items_in_src:
        src_item_path = os.path.join(src, item)
        target_item_path = os.path.join(target, item)

        if os.path.isdir(src_item_path):
            # If it's a directory, handle the case where the target directory already exists
            if item not in items_in_target:
                txt = f"Directory {item} doesn't exist in {target} folder!\n"
                log.write(txt)
                print(txt)
            
            if os.path.exists(target_item_path):
                shutil.rmtree(target_item_path) 

            shutil.copytree(src_item_path, target_item_path)

            txt = f"Directory {item} and its contents were copied to {target}!\n"
            log.write(txt)
            print(txt)
        elif os.path.isfile(src_item_path):
            if item not in items_in_target:
                txt = f"File {item} doesn't exist in {target} folder!\n"
                log.write(txt)
                print(txt)

            shutil.copy2(src_item_path, target_item_path)

            txt = f"File {item} was copied to {target}!\n"
            log.write(txt)
            print(txt)
        else:
            txt = f"Item {item} is neither a file nor a directory!\n"
            log.write(txt)
            print(txt)
    
    txt = "No items were created in the target folder!\n"
    log.write(txt)
    print(txt)


# Delete function
def delete(src, target):
  # Listing the files from src and target folders
  files_in_src = os.listdir(src)
  files_in_target = os.listdir(target)

  delete_these = []

  # Checking if the target_file is in the source folder
  # If not, delete the file (or files) that are not in the target folder  
  for target_file in files_in_target:
    if target_file not in files_in_src:
      txt = f"File {target_file} doesn't exist in {src} folder!"
      print(txt)
      log.write(txt)
      delete_these.append(target_file)
    
  txt = "No files are missing or being deleted!"
  print(txt)

  for delete_this in delete_these:
    file_path = os.path.join(target, delete_this)
    os.remove(file_path)
    txt = f"File/s were deleted from {target} folder!\n"
    print(txt)
    log.write(txt)
  
  txt = f"No file/s were deleted from {target} folder!\n"
  print(txt)
  log.write(txt)

# Trying to make this (↓) synchronization to work periodically ( but don't know how to do it :( )
# Interval time
interval = 90
def sync_func(src, target):
  number_of_iteration = 10
  curr_iteration = 1

  while curr_iteration <= number_of_iteration:
    copy_create(src=source, target=replica)
    delete(src=source, target=replica)
    txt = "Synchronization completed!\n"
    log.write(txt)
    print(txt)
    txt = "Waiting 30 seconds for next synchronization.."
    log.write(txt)
    print(txt)
    log.flush()
    time.sleep(interval)
    curr_iteration+=1

    #print("End!")

#copy_create(src=source, target=replica)
#delete(src=source, target=replica)


# CLA - Command Line Arguments
arg = sys.argv[1]
if arg == "-h":
  print("Help:\n-log_file → Prints the location of log_file")
  print("-src → Prints the location of source folder")
  print("-target → Prints the location of target folder")
  print("-interval → Prints the interval time for synchronization")
  print("-sync → Starts One-way synchronization")
elif arg == "-log_file":
  log_file = "log.txt"
  log_path = os.path.join(os.getcwd(), log_file)
  print(f"The location of {log_file} is {log_path}!")
elif arg == "-src":
  src_folder = source
  src_folder_path = os.path.join(os.getcwd(), src_folder)
  print(f"The location of {src_folder} folder is {src_folder_path}!")
elif arg == "-target":
  target_folder = replica
  target_folder_path = os.path.join(os.getcwd(), target_folder)
  print(f"The location of {target_folder} folder is {target_folder_path}!")
elif arg == "-interval":
  print(f"The synchronization interval is {interval} seconds!")
elif arg == "-sync":
   print("Staring the synchronization...")
   sync_func(src=source, target=replica)
else:
  print(f"You provided a wrong argument: {arg}!")

log.close()

#sync_func(src=source, target=replica)