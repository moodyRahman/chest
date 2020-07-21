function deleteitem(elem) {
	self = $(elem);

	console.log(self)
	self.html("ARE YOU SURE?")
	self.removeAttr("onclick");
	self.attr("onclick", "deleteitemfr(self)");
}

function deleteitemfr(elem) {
	self = $(elem);
	itemid = self.attr("id");
	itemnamenode = $("#" + itemid + "_name")
	itemdescriptionnode = $("#" + itemid + "_description")
	itemname = itemnamenode.text()
	description = itemdescriptionnode.text()

	data = {
		"itemid": itemid,
		"charid": charid,
		"itemname": itemname,
		"description": description,
		charid: charid
	};

	console.log(data)
	post(deleteurl, data);
}