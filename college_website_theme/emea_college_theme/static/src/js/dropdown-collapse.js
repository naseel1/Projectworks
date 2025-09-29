 document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.nav-item.dropdown .nav-link.dropdown-toggle').forEach(function(link, index) {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            var navbarCollapse = document.getElementById('emea_top_menu_collapse');
            if (!navbarCollapse.classList.contains('show')) {  // If the navbar is not collapsed (in mobile view)
                if (index === 1) {
                    window.open("https://emea.embase.in/admission/", "_blank");  // Open in new tab
                } else if (index === 2) {
                    window.location.href = "/academics";
                } else if (index === 7) {
                    window.location.href = "/Home/IQAC/Composition/172";
                }
                else if (index === 5) {
                    window.location.href = "/facilities";
                }
            }
        });
    });
});