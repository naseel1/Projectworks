document.addEventListener('DOMContentLoaded', function() {
    // Select all links with the class `o_image`
    var links = document.querySelectorAll('a.o_image');

    links.forEach(function(link) {
        // Get the current href value
        var href = link.getAttribute('href');

        // Check if the href contains `download=true`
        if (href.includes('download=true')) {
            // Remove the `download=true` parameter
            href = href.split('&amp;download=true')[0];
            link.setAttribute('href', href);
        }
    });
});