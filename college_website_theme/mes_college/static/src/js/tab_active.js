document.addEventListener("DOMContentLoaded", function() {
    // Get the first tab link and tab content
    var firstTabLink = document.querySelector('.tabs-lists .nav-link');
    var firstTabContent = document.querySelector('.s_tabs_contents .tab-pane');

    // Add the 'active' class to the first tab link and tab content
    firstTabLink.classList.add('active');
    firstTabContent.classList.add('show', 'active');
});