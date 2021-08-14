import utils
import sys

print("This is argv:", sys.argv)


command = sys.argv[1]
if command == 'build':
    utils.main
elif command == 'new':
    open("contents/new_content_page.html", "w+").write("<div>New Content</div>")
else:
    print("Please specify 'build' or 'new'")




