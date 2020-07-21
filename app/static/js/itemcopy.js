function copyitem(elem){
	self = $(elem)
	console.log(self)
	id = self.attr("id")
	console.log(id)
	copyitemname = $("#" + id + "_name").text()
	copyitemdesc = $("#" + id + "_description").text()

	console.log(copyitemname)
	console.log(copyitemdesc)

	$("#newname").attr("value", copyitemname)
	$("#newdesc").attr("value", copyitemdesc)

}