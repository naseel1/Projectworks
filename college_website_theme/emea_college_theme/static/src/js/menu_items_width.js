document.addEventListener('DOMContentLoaded', function() {
    // Function to update the width of the menu item
    function updateMenuItemWidth() {
        var dropdownMenu = document.querySelector('#drop_down.show');
        var menuItem = document.querySelector('.menu-item-type-post_type');

        if (dropdownMenu) {
            menuItem.style.width = '100%';
        } else {
            menuItem.style.width = ''; // Reset to default if the dropdown is not shown
        }
    }

    // Call the function initially to set the correct width
    updateMenuItemWidth();

    // Add event listeners for dropdown show and hide events
    var dropdownToggle = document.querySelector('.dropdown-toggle');
    dropdownToggle.addEventListener('click', function() {
        // Update the width when the dropdown is toggled
        updateMenuItemWidth();
    });
});
