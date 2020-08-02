function drawdice(data){

	results = []
	var out = ""
	var cumsum = 0
	var dice = data["dice"]
	// console.log(dice)
	dice.forEach(element => {
		out += (element["n"] + "d" + element["s"] + " (")
		
		for (let i = 0; i < parseInt(element["n"]) - 1; i++) {
			let res = Math.floor((Math.random() * parseInt(element["s"])) + 1)
			out += res + ", "
			cumsum += res
			results.push(res)
		}

		final = Math.floor((Math.random() * parseInt(element["s"])) + 1)
		out += final
		cumsum += final
		results.push(final)
		out += ") <br>"
	});
	out += cumsum + "  +  " + data["modifier"]
	out += "<h2>" + (cumsum + parseInt(data["modifier"])) + "</h2>"

	var cardtemplate = $(`
	<div class="card py-0 text-white bg-dark" id="card_${data["id"]}" style="max-width: 100%;">
		<h4 class="card-title">${data["name"]}</h4>
		<div class="card-body">
			<p class="card-text">${cumsum + parseInt(data["modifier"])}</p>
		</div>
	</div>
		`
	)

	return {
		out:out, 
		cumsum: cumsum + parseInt(data["modifier"]), 
		results:results, 
		card:cardtemplate
	}
}


function roll(self) {

	var dice = []
	$("#data_" + $(self).attr("id")).children().each(function (index) {
		dice.push(
			{
				n: $(this).attr("n"),
				s: $(this).attr("s")
			}
		)
	}
	)


	
	var data = {
		modifier: $("#data_" + $(self).attr("id")).attr("modifier"),
		dice:dice, 
		id:$(self).attr("id"), 
		name: $(self).attr("rname")
	}

	var card = $(`
	<div class="card py-0 text-white bg-dark" id="card_${data["id"]}" style="max-width: 100%;">
		<div class="card-body">
			<p class="card-text">mdn</p>
		</div>
	</div>
		`
	)
	var res = drawdice(data)

	$("#allroller").append(res["card"])


	console.log(res)
	console.log(data)

	var modal = $(
		`
		<div data-toggle="modal" class="modal fade" id="modal_${data["id"]}" tabindex="-1" role="dialog" aria-hidden="true">
			<div class="modal-dialog" role="document">
				<div class="modal-content">
					<div class="modal-header">
						<h5 class="modal-title" id="chardeletemodal"></h5>
						<button type="button" class="close" data-dismiss="modal" aria-label="Close">
							<span aria-hidden="true">&times;</span>
						</button>
					</div>
					<div class="modal-body">
						<h6>${res["out"]}</h6>
					</div>
					<div class="modal-footer">
						
					</div>
				</div>
			</div>
		</div>
		`
	)

	$(document.body).append(modal)
	$("#modal_" + data["id"]).modal()
	$("#modal_" + data["id"]).on('hidden.bs.modal', function () {
		$(this).remove()
	})
}