document.addEventListener("DOMContentLoaded", function() {
	function runcheck() {
		var jqXHR = $.ajax({
			type: "POST",
			url: "/check",
			async: false,
			data: { mydata: url }
		});
	}

	let ele = document.createElement("script")
	ele.setAttribute("src", "https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js")
	ele.textContent = "runCheck()"
	document.head.appendChild(ele)
})