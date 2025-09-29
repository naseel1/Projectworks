 document.addEventListener('DOMContentLoaded', function() {
    const navToggler = document.getElementById('navToggler');
    const menuOverlay = document.getElementById('menu-overlay');

    // Function to check and update the display property of the menu overlay
    function updateMenuOverlay() {
        if (navToggler.classList.contains('menu-opened')) {
            menuOverlay.style.display = 'block';
        } else {
            menuOverlay.style.display = 'none';
        }
    }

    // MutationObserver to detect class changes on the navToggler element
    const observer = new MutationObserver(updateMenuOverlay);

    // Observe attribute changes (specifically class changes) on the navToggler element
    observer.observe(navToggler, { attributes: true, attributeFilter: ['class'] });

    // Initial check
    updateMenuOverlay();
});