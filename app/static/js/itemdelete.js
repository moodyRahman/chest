function deleteitem(elem) {
	var self = $(elem);

	console.log(self)
	self.html("ARE YOU SURE?")
	self.removeAttr("onclick");
	self.attr("onclick", "deleteitemfr(self)");
}

function deleteitemfr(elem) {
	var self = $(elem);
	var itemid = self.attr("id");
	var itemnamenode = $("#" + itemid + "_name")
	var itemdescriptionnode = $("#" + itemid + "_description")
	var itemname = itemnamenode.text()
	var description = itemdescriptionnode.text()

	var data = {
		"itemid": itemid,
		"charid": charid,
		"itemname": itemname,
		"description": description,
		charid: charid
	};

	console.log(data)
	post(deleteurl, data);
}