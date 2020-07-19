fin = open("item_categories.txt", "r").read().split("\n")

template ="""\t<td>

\t\t<input type ="checkbox" class="form-check-input" id="tag-{category}" name="tag-{category}">
\t\t<label class="" for="tag-weapon">{category}</label>
\t</td>
"""

out = "<tr>\n"
for x in fin:
	if x == "---":
		out += "</tr>\n<tr>"
	else:
		out += template.format(category=x)
	# print(out)

out += "</tr>"

open("out_html.txt", "w").write(out)