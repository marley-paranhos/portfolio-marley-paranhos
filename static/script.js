// Abre e fecha o menu quando clicar no icone: hamburguer e x

const menuMobile = document.querySelector('.menu-mobile');
const body = document.querySelector('body');

menuMobile.addEventListener('click', () => {
    menuMobile.classList.contains('bi-list')
        ? menuMobile.classList.replace('bi-list', 'bi-x')
        : menuMobile.classList.replace('bi-x', 'bi-list');
    body.classList.toggle('menu-nav-active');
});

// Fecha o menu quando clicar em um item do menu
const navItem = document.querySelectorAll('.nav-item');
navItem.addEventListener('click', () => {
    menuMobile.classList.replace('bi-x', 'bi-list');
    body.classList.remove('menu-nav-active');
});

navItem.forEach((item) => {
    item.addEventListener('click', () => {
        if (body.classList.contains('menu-nav-active')) {
            body.classList.remove('menu-nav-active');
            menuMobile.classList.replace('bi-x', 'bi-list');
        }
    });
}
