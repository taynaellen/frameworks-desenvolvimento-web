const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const img = new Image();
    img.src = 'https://img.freepik.com/vetores-gratis/cima-baixo-direita-esquerda-setas-em-circulos_78370-1297.jpg';
    
    const imgWidth = 200;
    const imgHeight = 200;
    let posX = (canvas.width - imgWidth) / 2; //centraliza
    let posY = (canvas.height - imgHeight) / 2; //centraliza



    img.onload = function() {
        ctx.drawImage(img, posX, posY, imgWidth, imgHeight); //desenha a imagem na posição inicial
    }

    
    function drawImage() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(img, posX, posY, imgWidth, imgHeight); 
    }


    document.addEventListener('keydown', function(event) {
        const step = 10;

        if (event.key === 'ArrowRight' && posX + imgWidth + step <= canvas.width) {
        posX += step;
        }
        if (event.key === 'ArrowLeft' && posX - step >= 0) {
        posX -= step; 
        }
        if (event.key === 'ArrowUp' && posY - step >= 0) {
        posY -= step; 
        }
        if (event.key === 'ArrowDown' && posY + imgHeight + step <= canvas.height) {
        posY += step;
        }
        drawImage();
    });