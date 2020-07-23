fin = open("item_color_categories.txt", "r").read()

template = '"{category}":"{color}", '

out = "{"
for x in fin.split("\n"):
	if x != "---":
		line = x.split("|")
		out += template.format(category = line[0], color = line[1])

out = out[:-2]
out += "}"
open("catecolordictout.txt", "w").write(out)