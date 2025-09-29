 $(document).ready(function() {
    $('.tabs-list1 .nav-link').not('#drop_sidebar-li').on('click', function() {
        var $clubTabs = $('#all_tabs');

        // Check if #club_tabs exists
        if ($clubTabs.length) {
            // Scroll to the top of the container (#all_tabs)
            $('html, body').animate({
                scrollTop: $clubTabs.offset().top
            }, 600);
        }
        // If #club_tabs doesn't exist, simply do nothing and continue without any errors.
    });
});