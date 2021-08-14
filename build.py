import glob
import os
from jinja2 import Template

def read_base_html():
	base_html = open("./templates/base.html").read()
	return base_html


pages = [
#	{"filename" : "./contents/blog.html","output" : "./docs/blog.html","title" : "Blog",},
#	{"filename" : "./contents/index.html","output" : "./docs/index.html","title" : "About Me",},
#	{"filename" : "./contents/online_resume.html","output" : "./docs/online_resume.html","title" : "Resume",}

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


def generate_pages(lists):
	base = read_base_html()
	for page in lists:
		html = open(page['filename']).read()
		template = Template(base)
		page_html = template.render(
			content = html,
			title = page["title"]
		)
		open(page['output'], "w+").write(page_html)



def main():
#   base = read_base_html()
#	blog = open("./contents/blog.html").read()
#	index = open("./contents/index.html").read()
#	resume = open("./contents/online_resume.html").read()

#	blog_html = base.replace("{{content}}", blog)
#	index_html = base.replace("{{content}}", index)
#	resume_html = base.replace("{{content}}", resume)
#	open("docs/blog.html", "w+").write(blog_html)
#	open("docs/index.html", "w+").write(index_html)
#	open("docs/online_resume.html", "w+").write(resume_html)

		

	#basically, all of the "hard-code" above is simplified and 
	#goes into the generate_pages function
	generate_pages(pages)
		
	


main()