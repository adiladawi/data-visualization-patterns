import sys

def create_wiki_page(params):
    """Open the three markdown files of a pattern and create the Wiki page""" 
    main_page = open(params[4] + params[0]).read()
    py_page = open(params[4] + params[1]).read()
    r_page = open(params[4] + params[2]).read()

    wiki_page = open(params[5] + params[3], 'w')
    wiki_page.write(main_page)
    wiki_page.write(py_page)
    wiki_page.write(r_page)

    wiki_page.close()
    print "Wiki page '%s' successfully created." % (params[3])

def main():
    if len(sys.argv) != 7:
        print "usage: ./create_wiki_page.py main_wiki, py_wiki, r_wiki file_name"
    else:
        create_wiki_page(sys.argv[1:7])



if __name__ == '__main__':
    main()