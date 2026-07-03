class Player{
    constructor(canvasWidth, canvasHeight){
        this.width = 32;
        this.height = 40;
        this.x = 100;
        this.groundY = 350;
        this.y = this.groundY - this.height;

        this.speed = 5;
        this.velX= 0;
        this.velY = 0;
        this.gravity = 0.6;
        this.friction = 0.85;
        this.grounded = true;
    }

    update(input){
        //left or right movements
        if (input.isPressed('ArrowRight')){
            if(this.velX < this.speed) this.velX++;
        }
        if (input.isPressed('ArrowLeft')){
            if(this.velX > -this.speed) this.velX--;
        }

        //jump (jumpman) (shutup)

        if(input.isPressed('Space') && this.grounded){
            this.velY= -12;
            this.grounded = false;
        }

        console.log("Antes:", this.y, this.velY, this.gravity)

        this.velX *= this.friction;
        this.velY += this.gravity;

        this.x += this.velX;
        this.y += this.VelY;

        console.log("Antes:", this.y)

        if ( isNaN(this.y)|| (this.y + this.height >= this.groundY)){
            this.y = this.groundY - this.height;
            this.velY= 0;
            this.grounded = true;
        }

        if(this.x < 0) this.x = 0;
        if(this.x + this.width > 800) this.x = 800 - this.width;

    }

    draw(ctx){
        console.log(this.x, this.y);
        ctx.fillStyle = '#E52521';
        ctx.fillRect(this.x, this.y, this.width, this.height);

        ctx.fillStyle = '#002FBE';
        ctx.fillRect(this.x + 4, this.y + 20, this.width - 8, this.height - 20);

    }
}


    
    
