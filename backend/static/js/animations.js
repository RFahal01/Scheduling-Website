document.addEventListener('DOMContentLoaded', function () {
    // Select all button elements
    const buttons = document.querySelectorAll('button');

    // Add hover effects to each button
    buttons.forEach(button => {
        button.addEventListener('mouseover', () => {
            // Scale up the button on mouseover
            button.style.transform = 'scale(1.05)';
            button.style.transition = 'transform 0.3s';
        });

        button.addEventListener('mouseout', () => {
            // Scale down the button on mouseout
            button.style.transform = 'scale(1)';
            button.style.transition = 'transform 0.3s';
        });
    });

    // Select all elements with the class 'page-transition'
    const pages = document.querySelectorAll('.page-transition');

    // Add fade-in effect to each page element
    pages.forEach(page => {
        // Set initial opacity to 0
        page.style.opacity = 0;
        // Delay the transition to allow for the initial load
        setTimeout(() => {
            // Fade in the page element
            page.style.opacity = 1;
            page.style.transition = 'opacity 1s ease-in-out';
        }, 100);
    });
});