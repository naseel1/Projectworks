 document.addEventListener("DOMContentLoaded", function () {
    // Ensure navigation and dropdowns load first
    const navElement = document.getElementById('site-navigation');

    // Add event listeners for dropdowns
    const dropdownToggles = navElement.querySelectorAll('.dropdown-toggle');

    dropdownToggles.forEach(function (toggle) {
        toggle.addEventListener('click', function (e) {
            e.preventDefault();
            const parent = toggle.parentElement;
            const dropdownMenu = parent.querySelector('.dropdown-menu');

            // Toggle dropdown visibility
            if (dropdownMenu.classList.contains('show')) {
                dropdownMenu.classList.remove('show');
            } else {
                // Close other open dropdowns if needed
                navElement.querySelectorAll('.dropdown-menu').forEach(function (openMenu) {
                    openMenu.classList.remove('show');
                });
                dropdownMenu.classList.add('show');
            }
        });
    });
});
