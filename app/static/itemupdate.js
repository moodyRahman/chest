function itemeditor(elem) {
	self = $(elem);
	itemid = self.attr("id");
	itemnamenode = $("#" + itemid + "_name")
	itemdescriptionnode = $("#" + itemid + "_description")

	console.log(itemid)
	console.log(itemnamenode.text())
	console.log(itemdescriptionnode.text())

	itemnamefield = $('<input type="text" style="display : inline;" class="form-control md-form" />')
	itemnamefield.val(itemnamenode.text())
	itemnamefield.attr("id", itemid + "_name")

	itemdescfield = $(('<input type="text" style="display : inline;" class="form-control md-form" />'))
	itemdescfield.attr("id", itemid + "_description")
	itemdescfield.val(itemdescriptionnode.text())


	itemnamenode.replaceWith(itemnamefield)
	itemdescriptionnode.replaceWith(itemdescfield)

	self.html("UPDATE");
	self.removeAttr("onclick");
	self.attr("onclick", "updateitem(self)");
}



function updateitem(elem) {
	self = $(elem);
	itemid = self.attr("id");
	itemnamenode = $("#" + itemid + "_name")
	itemdescriptionnode = $("#" + itemid + "_description")
	itemname = itemnamenode.val()
	description = itemdescriptionnode.val()
	data = {
		"itemid":itemid, 
		"charid":charid,
		"itemname":itemname, 
		"description":description 
	};
	console.log(url);
	// data = JSON.stringify(data)
	console.log(data);
	console.log(itemnamenode)
	post(url, data);
}



function post(path, params, method = 'post') {
	const form = document.createElement('form');
	form.method = method;
	form.action = path;

	for (const key in params) {
		if (params.hasOwnProperty(key)) {
			const hiddenField = document.createElement('input');
			hiddenField.type = 'hidden';
			hiddenField.name = key;
			hiddenField.value = params[key];

			form.appendChild(hiddenField);
		}
	}

	document.body.appendChild(form);
	form.submit();
}