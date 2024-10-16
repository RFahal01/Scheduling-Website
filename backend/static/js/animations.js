document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('button');

    buttons.forEach(button => {
        button.addEventListener('mouseover', () => {
            button.style.transform = 'scale(1.05)';
            button.style.transition = '0.3s';
        });

        button.addEventListener('mouseout', () => {
            button.style.transform = 'scale(1)';
            button.style.transition = '0.3s';
        });
    });

    const pages = document.querySelectorAll('.page-transition');
    pages.forEach(page => {
        page.style.opacity = 0;
        setTimeout(() => {
            page.style.opacity = 1;
            page.style.transition = '1s ease-in-out';
        }, 100);
    });
});
