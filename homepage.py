top_html = open("./templates/top.html").read()
bottom_html = open("./templates/bottom.html").read()
middle_html = open("./contents/index.html").read()

combined_html = top_html + middle_html + bottom_html
open("docs/index.html", "w+").write(combined_html)


top_html = open("./templates/top.html").read()
bottom_html = open("./templates/bottom.html").read()
middle_html = open("./contents/blog.html").read()

combined_html = top_html + middle_html + bottom_html
open("docs/blog.html", "w+").write(combined_html)


top_html = open("./templates/top.html").read()
bottom_html = open("./templates/bottom.html").read()
middle_html = open("./contents/online_resume.html").read()

combined_html = top_html + middle_html + bottom_html
open("docs/online_resume.html", "w+").write(combined_html)
