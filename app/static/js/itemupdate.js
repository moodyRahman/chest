function itemeditor(elem) {
	var self = $(elem);
	var itemid = self.attr("id");
	var itemnamenode = $("#" + itemid + "_name")
	var itemdescriptionnode = $("#" + itemid + "_description")

	var itemnamefield = $('<input type="text" style="height:100%; display : inline; border: 2px solid red; border-radius: 10px;" class="form-control md-form" />')
	// itemnamefield = $('<textarea style="display : inline;" class="form-control md-form" />')
	var itemnamefield.val(itemnamenode.text())
	var itemnamefield.attr("id", itemid + "_name")

	// itemdescfield = $(('<input type="text" style="height:100px; display : inline;" class="form-control md-form" />'))
	var itemdescfield = $('<textarea style="display : inline; border: 2px solid red; border-radius: 10px;" rows="2" class="form-control md-form" />')
	var itemdescfield.attr("id", itemid + "_description")
	var itemdescfield.val(itemdescriptionnode.text())

	console.log(itemnamenode.prop("tagName"))

	if (itemnamenode.prop("tagName") !== "INPUT"){
		itemnamenode.replaceWith(itemnamefield)
		itemdescriptionnode.replaceWith(itemdescfield)
	}

	self.html("CONFIRM");
	self.removeAttr("onclick");
	self.attr("onclick", "updateitem(self)");

	newpopoverbuttons =`
					<button class='btn btn-outline-success btn-sm btn-block' id='`+ itemid +`' onclick='updateitem(this)'>confirm</button> 
					<br><br>
					<button data-toggle='modal' data-target='#copyconfirm' class='btn btn-outline-info btn-sm btn-block' id='`+ itemid +`' onclick='copyitem(this)'>copy</button>
					<br><br>
					<button class='btn btn-outline-danger btn-sm btn-block' id='`+ itemid +`' onclick='deleteitem(this)'>delete</button>`
	
	$("#" + itemid + "_popover").attr("data-content", newpopoverbuttons)
}



function updateitem(elem) {
	var self = $(elem);
	var itemid = self.attr("id");
	var itemnamenode = $("#" + itemid + "_name")
	var itemdescriptionnode = $("#" + itemid + "_description")
	
	console.log(itemnamenode)
	console.log(itemdescriptionnode)

	var itemname = itemnamenode.val()
	var description = itemdescriptionnode.val()

	
	data = {
		"itemid":itemid, 
		"charid":charid,
		"itemname":itemname, 
		"description":description 
	};


	console.log(data)


	post(updateurl, data);
}