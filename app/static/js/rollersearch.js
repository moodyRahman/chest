function isvalidsearchroller(query, name) {
	var name = name.toLowerCase()
	var query = query.toLowerCase()
	if (name.includes(query)) {
		return true;
	}
	return false;
}

function inventoryclick(self) {
	var name = self.dataset.name
	var desc = self.dataset.desc
	$('#descdisp').text(name + ": "  + desc)
}

$("#searchbox").on("input", function (self) {
	console.clear()
	var query = $("#searchbox").val().toLowerCase()

	$(".inventoryrow").each(function (index) {
		if (query === "") {
			this.style.display = ""
			return
		}

		var name = this.dataset.name

		if (isvalidsearchroller(query, name)) {
			this.style.display = ""
		}
		else {
			this.style.display = "none"
		}
	})
})

