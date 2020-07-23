fin = open("helpdiv.txt", "r").read().split("\n")


template = """ {{'text':'{text}', 'file':'{gifname}'}}, """

out = ""

for line in fin:
	words = line.split("|")
	out+= template.format(text=words[0], gifname=words[1])
	out += "\n"

open("helpdivout.txt", "w").write(out)