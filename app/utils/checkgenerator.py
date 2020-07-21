fin = open("item_categories.txt", "r").read().split("\n")

template ="""'{category}',"""

out = "["
for x in fin:
	if x == "---":
		out += "],\n ["
	else:
		out += template.format(category=x)
	# print(out)

out += "]"

open("out_html.txt", "w").write(out)