import glob
import os
from jinja2 import Template

def read_base_html():
	base_html = open("./templates/base.html").read()
	return base_html


pages = [

]


#reads the html file in contents, automatically appends
#filename, output, and title to the pages list
html_files = glob.glob("contents/*.html")	
for html_file in html_files:
	file_path = html_file
	file_name = os.path.basename(file_path)
	name_only, extension = os.path.splitext(file_name)
	pages.append({"filename" : html_file, 
				  "output" : "docs/"+file_name,
				  "title" : name_only})


#this function generates the html pages and puts the final html pages into the docs folder
def generate_pages(lists):
	base = read_base_html()
	for page in lists:
		html = open(page['filename']).read()
		template = Template(base)
		page_html = template.render(
			content = html,
			pages = pages,
			title = page["title"]
		)
		open(page['output'], "w+").write(page_html)



def main():

	generate_pages(pages)
		
	


