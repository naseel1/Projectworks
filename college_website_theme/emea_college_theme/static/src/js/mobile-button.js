 document.addEventListener('DOMContentLoaded', function() {
    const searchButton = document.querySelector('.mobile-button');
    const searchInput = document.querySelector('.mobile-search');

    searchButton.addEventListener('click', function() {
        if (searchInput.style.display === 'none' || searchInput.style.display === '') {
            searchInput.style.display = 'block';
        } else {
            searchInput.style.display = 'none';
        }
    });
});