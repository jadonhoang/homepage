

def read_base_html():
	base_html = open("./templates/base.html").read()
	return base_html
	

def generate_pages(lists):
	base = read_base_html()
	for page in lists:
		html = open(page['filename']).read()
		page_html = base.replace("{{content}}", html)
		open(page['output'], "w+").write(page_html)


pages = [
	{
	"filename" : "./contents/blog.html",
	"output" : "./docs/blog.html",
	"title" : "Blog",
	},
	{
	"filename" : "./contents/index.html",
	"output" : "./docs/index.html",
	"title" : "About Me",
	},
	{
	"filename" : "./contents/online_resume.html",
	"output" : "./docs/online_resume.html",
	"title" : "Resume",
	}

]





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


	for page in pages:
		base = read_base_html()
		title = base.replace("{{title}}", page['title'])
		print(title)

	#basically, all of the "hard-code" above is simplified and 
	#goes into the generate_pages function
	generate_pages(pages)
		
	
	

main()
	

