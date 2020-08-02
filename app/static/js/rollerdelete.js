function deleteask(self) {
	console.log("<button id=" + $(self).attr("id") + " class='btn btn-warning' onclick='rollerdeletefr(this)'>are you sure?</button>")
	$(self).replaceWith("<button id=" + $(self).attr("id") + " class='btn btn-warning' onclick='rollerdeletefr(this)'>are you sure?</button>")
}

function rollerdeletefr(self) {
	console.log($(self).attr("id"))
	var data = {
		rollerid: $(self).attr("id"),
		charid: charid
	};

	post(rollersdeleteurl, data)
}