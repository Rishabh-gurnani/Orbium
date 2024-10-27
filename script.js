document.querySelectorAll('nav ul li a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

document.querySelector('.explore-btn').addEventListener('click', () => {
    document.querySelector('#missions').scrollIntoView({
        behavior: 'smooth'
    });
});
