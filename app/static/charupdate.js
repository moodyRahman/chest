function charupdate(elem) {
	self = $(elem);
	console.log(elem);
	charnamenode = $("#charname")
	charclassnode = $("#charclass")
	chardescnode = $("#chardesc")

	charnamefield = $('<input id="charname" placeholder="character name here" type="text" style="height:100%; display : inline; line-height: 2em; font-size:2em; color:green" class="form-control md-form" />')
	// itemnamefield = $('<textarea style="display : inline;" class="form-control md-form" />')
	charnamefield.val(charnamenode.text())

	charclassfield = $('<input id="charclass" placeholder="character class here" type="text" style="height:100%; display : inline; line-height: 2em; font-size:2em; color:green" class="form-control md-form" />')
	charclassfield.val(charclassnode.text())

	// itemdescfield = $(('<input type="text" style="height:100px; display : inline;" class="form-control md-form" />'))
	chardescfield = $('<textarea id="chardesc" placeholder="character description here"  rows="2" class="form-control md-form" />')
	chardescfield.val(chardescnode.text())



	charnamenode.replaceWith(charnamefield)
	charclassnode.replaceWith(charclassfield)
	chardescnode.replaceWith(chardescfield)

	// chardeletebutton = $('<button class="btn btn-danger" style="float: right;" onclick="chardelete(this)" data-toggle="modal" data-target="#chardeletemodal">DELETE THIS CHARACTER</button>')
	chardeletebutton = $('<button type="button" class="btn btn-danger" style="float: right;" data-toggle="modal" data-target="#deletecharmodal">DELETE CHARACTER</button >')
	chardeletebutton.insertAfter(self)
	// self.insertAfter(chardeletebutton)
	self.html("CONFIRM EDIT");
	self.removeAttr("onclick");
	self.attr("onclick", "charupdatefr(self)");
}

function charupdatefr(elem) {
	console.log("it's been confirmed")
	charnamenode = $("#charname")
	charclassnode = $("#charclass")
	chardescnode = $("#chardesc")

	data = {
		name: charnamenode.val(),
		class: charclassnode.val(),
		description: chardescnode.val(),
		charid: charid
	}

	console.log(data)

	console.log(charupdateurl)

	post(charupdateurl, data)
}