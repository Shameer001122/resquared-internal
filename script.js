// JavaScript to toggle the mobile menu
const hamburger = document.getElementById('hamburger');
const navMenu = document.getElementById('nav-menu');

hamburger.addEventListener('click', () => {
    navMenu.classList.toggle('show');
});


//hamburger
(() => {
    const hamburger = document.getElementById('hamburger');
    const nav = document.getElementById('nav');

    // Toggle navigation menu and hamburger active state
    hamburger.addEventListener('click', () => {
        nav.classList.toggle('show');         // Show/hide navigation menu
        hamburger.classList.toggle('active'); // Switch between hamburger and close icon
    });
})();




//footer section
document.querySelectorAll('.footer-column h4').forEach(header => {
    header.addEventListener('click', () => {
        const list = header.nextElementSibling;
        list.style.display = list.style.display === 'block' ? 'none' : 'block';
    });
});

