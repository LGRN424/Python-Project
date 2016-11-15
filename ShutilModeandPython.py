import os
import shutil


root_src_dir = 'C:\Python27\Folder B'
root_dst_dir = 'C:\Python27\Folder A'

for src_dir, dirs, files in os.walk(root_src_dir):
    dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst_dir, file_)
        if os.path.exists(dst_file):
            os.remove(dst_file)
        shutil.move(src_file, dst_dir)
        print os.path.join(dst_dir, file_)
        
        
included_extenstions = ['txt']
file_names = [fn for fn in os.listdir(root_dst_dir)
              if any(fn.endswith(ext) for ext in included_extenstions)]


