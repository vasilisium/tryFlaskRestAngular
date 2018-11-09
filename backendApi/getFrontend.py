from os import listdir, path, remove
from shutil import copy2
from bs4 import BeautifulSoup

frontend_dir = "..\\frontend\\dist\\balistica\\"
backend_dir = ".\\backendApi\\"

static = "static"
templates = "templates"

def DeleteOld():
    curDir = path.join(backend_dir, static)
    [remove(path.abspath(path.join(curDir, file))) for file in listdir(curDir)]
    curDir = path.join(backend_dir, templates)
    [remove(path.abspath(path.join(curDir, file))) for file in listdir(curDir)]

def copy(frontend_dir, backend_dir):
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

def htmlParse():
    templates_dir = path.join(backend_dir, templates)
    files = listdir(templates_dir)
    for file in files:
        f = open(path.join(templates_dir,file),'r')
        soup = BeautifulSoup(f.read(), 'html.parser')
        scripts = soup.find_all('script')
        for script in scripts:
            # src = script['src']
            script['src'] = "{{ url_for('static', filename='"+script['src']+"') }}"
        f = open(path.join(templates_dir,file),'w')
        f.write(soup.prettify())
    return

DeleteOld()
copy(frontend_dir, backend_dir)
htmlParse()
