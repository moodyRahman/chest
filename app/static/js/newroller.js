$(document).ready(function () {
	var x = window.scrollX, y = window.scrollY;
	document.getElementById("newname").focus()
	window.scrollTo(x, y);
});

var dcount = 0;
function newelem(self) {
	dcount++;
	const dtemplate = `<div class="input-group dice">
				<input oninput="numonly(this)" name="dn-${dcount}" type="number" placeholder="dice" class="dn form-control">
				<span class="input-group-addon">&nbsp;d&nbsp;</span>
				<input oninput="numonly(this)" name="ds-${dcount}" type="number" placeholder="dice count" class="ds form-control"><br>
			</div>
			`
	$("#dice").append(dtemplate)
	console.log(dtemplate)
	event.preventDefault()
}

const regex = /^([+-]?[0-9]\d*|0)$/;

function numonly(self) {
	// console.log(self.value)
}

const plus = '<button id="dicemod" onclick="tominus(this)" class="btn btn-dark">+</button>'
const minus = '<button id="dicemod" onclick="toplus(this)" class="btn btn-dark">-</button>'
function tominus(self) {
	$(self).replaceWith(minus)
	event.preventDefault()
}

function toplus(self) {
	$(self).replaceWith(plus)
	event.preventDefault()
}

function rollersubmit() {
	var newname = $("#newname").val()
	var diceout = []
	$(".dice").each(function (index) {
		n = this.children[0].value
		s = this.children[2].value

		diceout.push(("n_" + n) + "_" + index)
		diceout.push(("s_" + s) + "_" + index)
	})

	var modifiersign = $("#dicemod").text()
	var modifier = $("#modifier").val()

	var data = {
		name: newname,
		alldice: diceout,
		sign: modifiersign,
		modifier: modifier,
		charid: charid
	}

	console.log(data)

	post(rollerurl, data)



	event.preventDefault()
}