function isvalidsearch(query, name, description, tags){
	if(name.includes(query)){
		return true;
	}
	if (description.includes(query)){
		return true;
	}
	for (let x = 0; x < tags.length; x++) {
		const tag = tags[x];
		if (tag.includes(query)) {
			console.log(tag)
			return true
		}
	}
	return false;
}


$("#searchbox").on("input", function(self){
	console.clear()
	query = $("#searchbox").val().toLowerCase()
	$(".inventoryrow").each(function( index ){
		if (query === ""){
			this.style.display = ""
			return
		}
		itemid = this.getAttribute("id")
		name = $("#" + itemid + "_name").text().toLowerCase()
		description = $("#" + itemid + "_description").text().toLowerCase()
		tags = []
		$("#" + itemid + "_tags").children().each(function(index){
			tags.push(this.innerHTML.toLowerCase())
		})
		if (isvalidsearch(query, name, description, tags)){
			this.style.display = ""
		}
		else{
			this.style.display = "none"
		}
	})
})