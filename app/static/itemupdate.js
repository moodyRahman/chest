function itemeditor(elem) {
	self = $(elem);

	row = self.parent().parent();
	row.attr("contenteditable", "true")
	row.removeClass('text-secondary');
	row.addClass("text-success");
	self.html("UPDATE");
	self.removeAttr("onclick");
	self.attr("onclick", "updateitem(self)");
}



function updateitem(elem) {
	self = $(elem);
	row = self.parent().parent();
	// print(row)
	console.log(row)
	kids = row.children();
	itemid = parseInt(kids[0].innerHTML);
	itemname = kids[1].innerHTML;
	description = kids[2].innerHTML;
	data = {
		"itemid":itemid, 
		"charid":charid,
		"itemname":itemname, 
		"description":description 
	};
	console.log(url);
	// data = JSON.stringify(data)
	console.log(data);
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