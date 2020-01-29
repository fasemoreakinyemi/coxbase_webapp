$(document).ready(function()
{

var dict = {
	142: [ "MST ID", "cox2", "cox5", "cox18", "cox20", "cox22", "cox37", "cox51", "cox56", "cox57", "cox61"]};

function json2table(json){
	var cols = dict[142] //Object.keys(json[0]);
	var headerRow = '';
	var bodyRows = '';
	function capitalizeFirstLetter(string) {
		return string;
		}
	cols.map(function(col) {
	 headerRow += '<th>' + capitalizeFirstLetter(col) + '</th>';
		});

json.map(function(row) {
	bodyRows += '<tr>';
	cols.map(function(colName) {
		bodyRows += '<td>' + row[colName] + '</td>';
				});
	bodyRows += '<td><button class="btnView">View profile entries</button></td>';
	bodyRows += '</tr>';

	});
	return '<table id="resulttable"><tr>' + headerRow + '</tr>' + bodyRows + '</table>';
};

function create_table(header_array){
var num_cols = header_array.length;
var num_rows = 1;
var table_body = "<table class='query_table'>";
for (var i=0;i<num_rows;i++){
	table_body+="<tr>";
	$.each(header_array, function(index,value){
		table_body+="<th class='query_table_header'>" + value + "</th>";
	});
	table_body+="</tr>"
	table_body+="<tr>"
	$.each(header_array, function(index,value){
		table_body+="<td><input class='tr_entry' name=" + value + " type='number'></td>"
	});
	table_body+="</tr>";
	table_body+="</table>";
};
return table_body
}


$('#select_panel').change(function() {
var key = ($("#select_panel option:selected").val());
var panel = dict[key]
$('#table_div').html(create_table(panel))


});

$( "#mst_form" ).submit(function( event ) {
var empty_field = [];
var map = {};
$(".tr_entry").each(function(){
	map[$(this).attr("name")] = $(this).val();
});
var len = Object.values(map).length;
var hst = location.host;
var url = "https://" + hst + "/webapp/mst_query"
for (var i=0; i<len; i++) {
	if(Object.values(map)[i] == "")
	{
		url+="/" + 0
		empty_field.push(i);
	} else {
		url+="/" + Object.values(map)[i]
	}
};
if (len === empty_field.length) {
	throw_empty_error()
} else {
	$('#empty_error').empty()
	$.get(url, 'json').done(function(results) {
		if(results.hasOwnProperty('STATUS')){
			render_No_match()

		}
		else {
		create_result(results)
		}
	}).fail(function (e){
		if (e.error) {
		alert("error due to" + e.error)
		}
		});
}
event.preventDefault();
});


$( ".submitMST" ).click(function( event ) {
var empty_field = [];
var map_list = [];
$(".entry").each(function(){
	if ($(this).text() == " Not detected") {
		var empty_cell = 0
		map_list.push(empty_cell)
	} else {

	map_list.push($(this).text());
	}

});

var len = map_list.length;
var hst = location.host;
var url = "https://" + hst + "/webapp/mst_query"
for (var i=0; i<len; i++) {
		url+="/" + map_list[i]
}
	$.get(url, 'json').done(function(results) {
		create_result(results)
	}).fail(function (e){
		if (e.error) {
		alert("error due to" + e.error)
		}
		});

event.preventDefault();
});

function create_result(data){
$('#result').html("<div class='result_header'><h1>Found profile(s)</h1></div>" + json2table(data))
};

function render_No_match(){
$('#result').html("<div class='result_header'><h1>Found profile(s)</h1><h3 style='color:red; padding:20px;'> No match in the database for the queried MST profile</h3></div>" )
};

function throw_empty_error(){
	$('#result').empty()
	$('#empty_error').html("<div class='container'><div class='well blue'><span class='error_well'><i class='fas fa-exclamation-triangle fa-2x'></i></span></div><div class='well white'>At least one input field should have an entry</div></div>")

}

$(".result_info").on("click", ".btnView",function(){
	var currentRow=$(this).closest("tr");
	var MLVAID=currentRow.find("td:eq(0)").text();
	var hst = location.host;
	var url = "https://" + hst + "/webapp/eview/mst/" + MLVAID
	window.open(url, '_blank');

});

$("#sampleQuery").click(function() {
	$('input[name="ms01"]').val(4);
	$('input[name="ms03"]').val(6);
	$('input[name="ms20"]').val(3);
	$('input[name="ms21"]').val(5);
	$('input[name="ms22"]').val(6);
	$('input[name="ms23"]').val(2);
	$('input[name="ms24"]').val(8);
	$('input[name="ms26"]').val(2);
	$('input[name="ms27"]').val(5);
	$('input[name="ms28"]').val(6);
})
});	
