 $(document).ready(function() {
    // Ensure the DOM is fully loaded before attaching event listeners
    document.querySelectorAll('.drop-emea .nav-link.dropdown-toggle').forEach(link => {
        link.addEventListener('show.bs.dropdown', function() {
            if (navbarCollapse.classList.contains('show')) {
                this.closest('.nav-item').style.flex = '0 0 100%';
            }
        });

        link.addEventListener('hide.bs.dropdown', function() {
            if (navbarCollapse.classList.contains('show')) {
                this.closest('.nav-item').style.flex = '0 0 50%';
            }
        });
    });

    // Check if the mobile navbar is collapsed or shown
    var navbarCollapse = document.getElementById('site-navigation');
    if (navbarCollapse.classList.contains('show')) {
        // Adjust flex properties or apply styles as needed for mobile view
        document.querySelectorAll('.drop-emea .nav-link.dropdown-toggle').forEach(link => {
            link.closest('.nav-item').style.flex = '0 0 100%';
        });
    }
});