function isvalidsearchroller(query, name) {
	name = name.toLowerCase()
	query = query.toLowerCase()
	if (name.includes(query)) {
		return true;
	}
	return false;
}

function inventoryclick(self) {
	name = self.dataset.name
	desc = self.dataset.desc
	$('#descdisp').text(name + ": "  + desc)
}

$("#searchbox").on("input", function (self) {
	console.clear()
	query = $("#searchbox").val().toLowerCase()

	$(".inventoryrow").each(function (index) {
		if (query === "") {
			this.style.display = ""
			return
		}

		name = this.dataset.name

		if (isvalidsearchroller(query, name)) {
			this.style.display = ""
		}
		else {
			this.style.display = "none"
		}
	})
})

