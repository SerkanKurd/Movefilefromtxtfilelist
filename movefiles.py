import os
import shutil

<<<<<<< HEAD
# get script runnig path
df_path = os.getcwd() + "\\"
print('\nDefault path is:', df_path)

# get source directory
=======
#get script runnig path 
df_path = os.getcwd() + "\\"
print('\nDefault path is:', df_path)

#get source directory
>>>>>>> fcde3251d1a195ba03cf207db26bf6d315399146
src_dir = input('\nInput the directory to search in (Default Path Press Enter): ')
if src_dir == "":
    src_dir = df_path
elif not os.path.exists(src_dir):
    print('\nDirectory is not exist')
    exit()
print('\nDirectory to search in:', src_dir)

<<<<<<< HEAD
# get txt file
=======
#get txt file
>>>>>>> fcde3251d1a195ba03cf207db26bf6d315399146
txtfile = input('\nInput the TEXT file name without .txt extention (Path must be same as Directory to search in): ')
if txtfile == "":
    print('No file name input')
    exit()
else:
    txtfile_path = str(src_dir) + str(txtfile) + ".txt"
if os.path.isfile(txtfile_path):
    print('\nFile is found', txtfile_path)
else:
<<<<<<< HEAD
    print('\n', txtfile_path, 'Text file is not exist')
=======
    print('\n',txtfile_path,'Text file is not exist')
>>>>>>> fcde3251d1a195ba03cf207db26bf6d315399146
    exit()

dst_dir = input('\nInput the directory to move the files to (Default same as TEXT file name): ')
if dst_dir == "":
    dst_dir = src_dir + txtfile
else:
    dst_dir = src_dir + dst_dir
<<<<<<< HEAD

if os.path.exists(dst_dir):
    print('\nDirectory to move the files is', dst_dir)
    print('\nDirectory is exist')
else:
    print('\nDirectory to move the files is', dst_dir)
    os.mkdir(dst_dir)
    print('\nDirectory is created')
=======
    
if os.path.exists(dst_dir):
    print ('\nDirectory to move the files is', dst_dir)
    print ('\nDirectory is exist')
else:
    print ('\nDirectory to move the files is', dst_dir)
    os.mkdir(dst_dir)
    print ('\nDirectory is created')
>>>>>>> fcde3251d1a195ba03cf207db26bf6d315399146

file_counter = 0
file_errorc = 0
with open(txtfile_path, 'r') as file_names:
    for file_name in file_names:
        file_name = file_name.strip()
        file_name = file_name.strip('"')
        src_file = os.path.join(src_dir, file_name)
        dst_file = os.path.join(dst_dir, file_name)
        if os.path.isfile(src_file):
            file_counter += 1
            print("\n", src_file, "--->", dst_file, "moved")
            shutil.move(src_file, dst_file)
        else:
<<<<<<< HEAD
            print("\n", src_file, "file not found")
            file_errorc += 1
print("\n", file_counter,  " files moved ", file_errorc, " files not found ")
txtfile_dst = dst_dir + "\\" + txtfile + ".txt"
shutil.move(txtfile_path, txtfile_dst)
print("\n", txtfile_path, "--->", txtfile_dst,
      "TEXT file moved to new location")
=======
            print("\n",src_file, "file not found")
            file_errorc += 1
print ("\n", file_counter,  " files moved ", file_errorc, " files not found ")
txtfile_dst = dst_dir + "\\" + txtfile + ".txt"
shutil.move(txtfile_path, txtfile_dst)
print ("\n", txtfile_path, "--->", txtfile_dst, "TEXT file moved to new location")
>>>>>>> fcde3251d1a195ba03cf207db26bf6d315399146
