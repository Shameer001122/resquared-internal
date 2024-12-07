// JavaScript to toggle the mobile menu
const hamburger = document.getElementById('hamburger');
const navMenu = document.getElementById('nav-menu');

hamburger.addEventListener('click', () => {
    navMenu.classList.toggle('show');
});

//footer section
document.querySelectorAll('.footer-column h4').forEach(header => {
    header.addEventListener('click', () => {
        const list = header.nextElementSibling;
        list.style.display = list.style.display === 'block' ? 'none' : 'block';
    });
});