 document.addEventListener('DOMContentLoaded', function() {
    const navToggler = document.getElementById('navToggler');
    const topMenuCollapse = document.getElementById('top_menu_collapse');
    const Wrap = document.getElementById('wrapwrap');

    navToggler.addEventListener('click', function() {
        // Toggle the 'show' class on the topMenuCollapse element
        topMenuCollapse.classList.toggle('show');
         Wrap.classList.toggle("lock-scroll");
        navToggler.classList.toggle('menu-opened');

    });
});
