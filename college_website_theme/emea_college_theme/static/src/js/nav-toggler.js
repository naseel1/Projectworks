document.addEventListener('DOMContentLoaded', function() {
    const navToggler = document.getElementById('navToggler');
    const topMenuCollapse = document.getElementById('site-navigation');
     const Wrap = document.getElementById('wrap');
    const foot = document.getElementById('bottom');

    navToggler.addEventListener('click', function() {
    // Toggle the 'show' class on the topMenuCollapse element
    topMenuCollapse.classList.toggle('show');
    Wrap.classList.toggle("lock-scroll");
     foot.classList.toggle("lock-scroll");
    navToggler.classList.toggle('menu-opened');
    });
});