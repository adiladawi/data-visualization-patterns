import sys

def create_wiki_page(config_file):
    """Open the three markdown files of a pattern and create the Wiki page""" 
    
    # Open configuracion file
    conf = [line.rstrip() for line in open(config_file)]
    files = {conf[i]:conf[i + 1] for i in xrange(0, len(conf), 2)}
    
    main_page = open(files['source_path'] + files['main_page']).read()
    py_page = open(files['source_path'] + files['py_page']).read()
    r_page = open(files['source_path'] + files['r_page']).read()

    wiki_page = open(files['dest_path'] + files['new_page'], 'w')
    wiki_page.write(main_page)
    wiki_page.write(py_page)
    wiki_page.write(r_page)

    wiki_page.close()
    print "Wiki page '%s' successfully created." % (files['new_page'])

def main():
    if len(sys.argv) != 2:
        print "usage: ./create_wiki_page.py wiki_config.txt"
    else:
        create_wiki_page(sys.argv[1])

if __name__ == '__main__':
    main()