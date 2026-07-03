const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

const input = new InputHandler();
const mario =  new Player(canvas.width, canvas.height);

function gameloop(){
    ctx.clearRect(0,0, canvas.width, canvas.height);

    SpriteManager.drawBackground(ctx, canvas.width, canvas.height);

    mario.update(input);

    mario.draw(ctx);

    requestAnimationFrame(gameloop);
}

gameloop();