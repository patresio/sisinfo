$("#tbLaudos").DataTable({
    // Datatables Configuration
    paging: true, // Pagination
    pageLength: 10, // Data per page 
    lengthChange: true, // Show entries per page
    autoWidth: false,
    searching: true,
    bInfo: true,
    bSort: true,

    // Disable columns with specific filter A to Z, Z to A
    "columnDefs": [{
        "targets":[6],
        "orderable": false,
    }]
});