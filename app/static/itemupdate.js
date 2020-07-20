function itemeditor(elem) {
	self = $(elem);
	itemid = self.attr("id");
	itemnamenode = $("#" + itemid + "_name")
	itemdescriptionnode = $("#" + itemid + "_description")

	itemnamefield = $('<input type="text" style="height:100%; display : inline;" class="form-control md-form" />')
	// itemnamefield = $('<textarea style="display : inline;" class="form-control md-form" />')
	itemnamefield.val(itemnamenode.text())
	itemnamefield.attr("id", itemid + "_name")

	// itemdescfield = $(('<input type="text" style="height:100px; display : inline;" class="form-control md-form" />'))
	itemdescfield = $('<textarea style="display : inline;" rows="2" class="form-control md-form" />')
	itemdescfield.attr("id", itemid + "_description")
	itemdescfield.val(itemdescriptionnode.text())

	console.log(itemnamenode.prop("tagName"))

	if (itemnamenode.prop("tagName") !== "INPUT"){
		itemnamenode.replaceWith(itemnamefield)
		itemdescriptionnode.replaceWith(itemdescfield)
	}

	self.html("CONFIRM");
	self.removeAttr("onclick");
	self.attr("onclick", "updateitem(self)");

	newpopoverbuttons =`<button class='btn btn-outline-success btn-sm btn-block' id='`+ itemid +` ' onclick='updateitem(this)'>confirm</button> 
					<br><br>
					<button data-toggle='modal' data-target='#copyconfirm' class='btn btn-outline-info btn-sm btn-block' id='`+itemid+`' onclick='copyitem(this)'>copy</button>
					<br><br>
					<button class='btn btn-outline-danger btn-sm btn-block' id='`+itemid+`' onclick='deleteitem(this)'>delete</button>" `
	
	$("#" + itemid + "_popover").attr("data-content", newpopoverbuttons)
}



function updateitem(elem) {
	self = $(elem);
	itemid = self.attr("id");
	itemnamenode = $("#" + itemid + "_name")
	itemdescriptionnode = $("#" + itemid + "_description")
	
	console.log(itemnamenode)
	console.log(itemdescriptionnode)

	itemname = itemnamenode.val()
	description = itemdescriptionnode.val()

	console.log(itemname)
	console.log(description)
	
	data = {
		"itemid":itemid, 
		"charid":charid,
		"itemname":itemname, 
		"description":description 
	};
	// data = JSON.stringify(data)
	// console.log(data);
	// console.log(itemnamenode)
	// post(updateurl, data);
}