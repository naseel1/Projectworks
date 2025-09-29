 document.addEventListener('DOMContentLoaded', function() {
    const navToggler = document.getElementById('navToggler');
    const topMenuCollapse = document.getElementById('top_menu_collapse');

    navToggler.addEventListener('click', function() {
        // Toggle the 'show' class on the topMenuCollapse element
        topMenuCollapse.classList.toggle('show');
        navToggler.classList.toggle('menu-opened');
    });
});