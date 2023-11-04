console.log("Hello World")
window.addEventListener('DOMContentLoaded', (event) => {
    // Check if the URL contains an anchor (e.g., #target-section)
    if (window.location.hash) {
        const targetId = window.location.hash.substring(1);
        const targetElement = document.getElementById(targetId);
        if (targetElement) {
            // Scroll to the target section smoothly
            targetElement.scrollIntoView({ behavior: 'smooth' });
        }
    }
});