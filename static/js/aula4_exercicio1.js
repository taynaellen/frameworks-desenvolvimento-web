const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
let img = new Image();
let x = 0; 
let y = 0; 


function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    y = (canvas.height - 100) / 2;
    redraw();
}

img.src = '/static/img/setas.png';
img.onload = () => {
    resizeCanvas();
};

window.addEventListener('resize', resizeCanvas);

function redraw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(img, x, y, 100, 100);
}

document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' && x + 110 < canvas.width) x += 10;
    if (e.key === 'ArrowLeft' && x > 0) x -= 10;
    redraw();
});
