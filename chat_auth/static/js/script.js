document.getElementById('menuToggle').addEventListener('click', function() {
    const menu = document.getElementById('leftMenu');
    if (menu.style.width === '0px') {
        menu.style.width = '250px';
    } else {
        menu.style.width = '0';
    }
});

document.addEventListener('DOMContentLoaded', function () {
    const messages = document.querySelectorAll('.messages');
    if (messages.length > 0) {
        alert(messages[0].textContent);
    }
});

function resizePage() {
    const width = window.innerWidth;

    if (width >= 1200) {
        document.body.style.transform = "scale(1)";
    } else if (width >= 992 && width < 1200) {
        document.body.style.transform = "scale(0.95)";
    } else if (width >= 768 && width < 992) {
        document.body.style.transform = "scale(0.9)";
    } else if (width >= 600 && width < 768) {
        document.body.style.transform = "scale(0.85)";
    } else if (width < 600) {
        document.body.style.transform = "scale(0.8)";
    }
}

// Resize function on page load and resize event
window.addEventListener('resize', resizePage);
resizePage();