document.addEventListener("DOMContentLoaded", function() {
    const tabs = document.querySelectorAll(".nav-link");
    const tabContents = document.querySelectorAll(".tab-content");

    // Define the activateTab function globally
    window.activateTab = function(event, tabId) {
        if (event) event.preventDefault(); // Prevent default anchor behavior if event exists
        tabs.forEach(tab => tab.classList.remove("active"));
        tabContents.forEach(content => content.classList.remove("active"));

        const activeTab = document.querySelector(`.nav-link[href="#${tabId}"]`);
        const activeContent = document.getElementById(tabId);

        if (activeTab) activeTab.classList.add("active");
        if (activeContent) activeContent.classList.add("active");

        history.pushState(null, null, `#${tabId}`);
    }

    function loadTabFromURL() {
        const hash = window.location.hash.substring(1);
        if (hash) {
            activateTab(null, hash); // No event to pass, so null is passed
        }
    }

    window.addEventListener("popstate", loadTabFromURL);

    loadTabFromURL(); // Load the correct tab based on the URL hash on page load
});