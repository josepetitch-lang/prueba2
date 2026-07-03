class SpriteManager {
    static drawBackground(ctx, canvasWidth, canvasHeight) {
        ctx.fillStyle = '#4c8c14';
        ctx.fillRect(0, 350, canvasWidth, canvasHeight - 350);
    }
}