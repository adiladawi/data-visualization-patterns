#Wiki Integration Script
This folder contains a Python script to integrate the markdown files for each pattern to create a wiki page for each one.
## Usage
1. Go to the directory that contains the markdown files of the patterns you want to integrate.
2. Copy all the files in the **_figures_** directory (the figures for the python pattern's implementation) and all the **_*_files_** directories (the figure for the R pattern's implementation) to the Wiki root directory (**_data-visualization-patterns.wiki_**).
3. Create a wiki integration configuration file based on the file **_wiki_config.txt_** and name the new file with the pattern's code in lowercase (e.g. **_a23.txt_**)
4. Run the script as: `$ python create_wiki_page.py a23.txt` where `a23.txt` should be the configuration file for the pattern you want to integrate.
5. Push wiki files to GitHub and you are done `:-)`.