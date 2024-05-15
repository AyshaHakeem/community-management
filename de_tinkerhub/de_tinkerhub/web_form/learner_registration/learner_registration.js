frappe.ready(function() {

    let anchor = document.querySelector('.edit-button');

    if (anchor) {
        // Change the text content of the anchor tag
        anchor.textContent = 'Edit Profile';
    }

    let sidebar_item = document.querySelectorAll('.sidebar-item');

    if (sidebar_item[0]) {
        
        let anchorTag = sidebar_item[0].querySelector('a');

        if (anchorTag) {
            // Change the href attribute
            anchorTag.href = `/learner/${frappe.session.user}`; 
        }
    }
})