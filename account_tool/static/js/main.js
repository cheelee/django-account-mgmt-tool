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
	$('#printList').click(function() {
		var widthDef = [];
		for (var i=0; i<printHeaderFields.length; i++) {
		    widthDef.push('auto');
		}
		var printContent = [];
		printContent.push(printHeaderFields);
		table.rows().every( function ( rowIdx, tableLoop, rowLoop ) {
			var rowContent = [];
			var data = this.data();
			for (var i=0; i<printHeaderFields.length; i++) {
			    var idx = table.column(printHeaderFields[i] + ':name').index();
			    rowContent.push(data[idx]);
			}
			printContent.push(rowContent);
		    } );
		var docDefinition = {
		    pageOrientation: 'landscape',
		    content: [ 
		{
		    layout: 'lightHorizontalLines', // optional
		    table: {
			// headers are automatically repeated if the table spans over 
			//   multiple pages
			headerRows: 1,
			widths: widthDef,
			body: printContent,
		    },
		},
			       ],
		};
		pdfMake.createPdf(docDefinition).open();
	    });

	$('#resultsTable tbody').on('dblclick', 'tr', function() {
		// The reason we do not use a simple click is because it causes clicks on
		//   URL links in the table to also trigger the edit option.
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