document.addEventListener('DOMContentLoaded', function() {
    var searchButton = document.querySelector('.search-button');
    var searchInput = document.querySelector('.search-input');

    if (searchButton && searchInput) {
        searchButton.addEventListener('click', function() {
            if (searchInput.style.display === 'none' || searchInput.style.display === '') {
                searchInput.style.display = 'block';
            } else {
                searchInput.style.display = 'none';
            }
        });
    }
});