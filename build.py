

def read_base_html():
	base_html = open("./templates/base.html").read()
	return base_html
	



def main(page):
	base = read_base_html()
	content_html = open("./contents/"+page+".html").read()
	base.replace("{{title}}", page.capitalize())
	page_html = base.replace("{{content}}", content_html)
	open("docs/"+page+".html", "w+").write(page_html)
	
	
	

main("blog")
main("index")
main("online_resume")



pages = [
	{
	"filename" : "contents/blog.html",
	"output" : "docs/blog.html",
	"title" : "Blog",
	},
	{
	"filename" : "contents/index.html",
	"output" : "docs/index.html",
	"title" : "About Me",
	},
	{
	"filename" : "contents/online_resume.html",
	"output" : "docs/online_resume.html",
	"title" : "Resume",
	}

]

for page in pages:
	print(page["title"])
	

