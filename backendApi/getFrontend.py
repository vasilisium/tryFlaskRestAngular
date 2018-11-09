from os import listdir, path
from shutil import copy2

frontend_dir = "..\\frontend\\balistica\\dist\\balistica\\"
backend_dir = ".\\backendApi\\"
static = "static"
templates = "templates"


files = listdir(frontend_dir)
for file in files:
    src = ''
    dist = ''
    if file.endswith('.html'):
        src = path.abspath(path.join(frontend_dir,file))    
        dist = path.abspath(path.join(backend_dir,templates,file))
    else:
        src =path.abspath(path.join(frontend_dir,file))
        dist = path.abspath(path.join(backend_dir,static,file))
    copy2(src,dist)

