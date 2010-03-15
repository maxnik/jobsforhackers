$(document).ready(function () {
  $('.ajax').live('click', function () {
    if (!this.title || confirm(this.title)) {
      $.ajax({
	clickedLink: this,
	beforeSend: function (XMLHttpRequest) {
	  $(this.clickedLink).replaceWith('<img id="busy" src="/static/busy.gif" />');
	},
	complete: function (XMLHttpRequest, textStatus) {
	  $('#busy').replaceWith(this.clickedLink);
	},
	success: function (data, textStatus) { 
	  for (var id in data) {
	    $('#'+id).replaceWith(data[id]);
	  }
	},
	type: 'POST',
	data: '', // without this jQuery doesn't send Content-Length headers for POST requests
	url: this.href,
	dataType: 'json'
      });
    }
    return false;
  }).attr('rel', 'nofollow');
});
