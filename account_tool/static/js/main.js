$(document).ready(function() {
	var dataTablesColDefs = [];

	for (var index in urlFieldIndices) {
	    var renderElement = {};
	    renderElement['targets'] = index;
	    renderElement['render'] = function( data, type, row, meta ) {
		return '<a target="_blank" href="' + data + '">' + data + '</a>';
	    };
	    dataTablesColDefs.push(renderElement);
	}

	var table = $('#resultsTable').DataTable( {
		responsive: true,
		data: resultsData,
		columns: columnSettings,
	    });

	//	for (var idx in visibleFields) {
	//	    if (visibleFields[idx] == 0) {
	//		table.column(idx).visible(false);
	//	    } else {
	//		table.column(idx).visible(true);
	//	    }
	//	}

	$('#resultsTable tbody').on('click', 'tr', function() {
		// *CWL* Attempts to allow a link-click without treating it as a row-click.
		// The following does not work - cell requires a 'td' event.
		// var colClickedIdx = table.cell(this).index().column;
		var data = table.row( this ).data();
		var recIdIdx = table.column('id:name').index();
		// var recUrlIdx = table.column('account_url:name').index();
		//		console.log('Clicked: ' + colClickedIdx + '| Url: ' + recUrlIdx); 
		//		if (colClickedIdx != recUrlIdx) {
		    key = data[recIdIdx];
		    $('#editField').val(key);
		    $('#editRecForm').submit();
		    //		}
		//		var recNameIdx = table.column('Name:name').index();
		//		var newTab = '';
		//		newTab += '<div class="tab-pane container fade" id="Tab' + data[recIdIdx] + '">';
		//		newTab += '<p>';
		//		newTab += '<a id="TabButton' + data[recIdIdx] + 
		//		    '" class="btn btn-info">Close Record</a>';
		//		newTab += '</p>';
		//		newTab += '<hr>';
		//		for (var idx=0; idx < data.length; idx++) {
		//		    newTab += '<p>' + dataHeaders[idx] + ': ';
		//		    newTab += data[idx] + '</p>';
		//		}
		//		newTab += '</div>';
		//		var newTabListItem = '';
		//		newTabListItem += '<li id="TabItem' + data[recIdIdx] + '" class="nav-item">';
		//		newTabListItem += '<a class="nav-link" data-toggle="tab"';
		//		newTabListItem += ' href="#Tab' + data[recIdIdx] + '">' + 
		//		    data[recNameIdx] + '</a></li>';
		//		$("#tabContent").append(newTab);
		//		$('#TabButton' + data[recIdIdx]).on('click', function(event) {
		//			$("#TabItem" + data[recIdIdx]).remove();
		//			$("#Tab" + data[recIdIdx]).remove();
		//			$("#resultsItem").trigger("click");
		//		    });
		//		$("#tabList").append(newTabListItem);
	    });
    });