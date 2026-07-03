const canvas = document.getElementById("canvas");
const canvasContext = canvas.getContext("2d");

const imgFantasmas = document.getElementById("ghosts");
const imgMapa = document.getElementById("map");

const fps = 30;
const oneBlockSize = 20;
const wallColor = "#342DCA";
const wallSpaceWidth = oneBlockSize / 1.5;
const wallOffset = (oneBlockSize - wallSpaceWidth) / 2;
const wallInnerColor = "black";


const DIRECTION_UP = 1;
const DIRECTION_LEFT = 2;
const DIRECTION_BOTTOM = 3;
const DIRECTION_RIGHT = 4;

let score = 0;


let map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 1, 0, 1, 1, 1, 2, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 2, 1, 0, 1, 1, 0, 1, 1, 0, 1, 2, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 2, 1, 0, 1, 1, 1, 1, 1, 0, 1, 2, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1],
    [1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
];

// Función auxiliar para dibujar rectángulos sencillos
let createRect = (x, y, width, height, color) => {
    canvasContext.fillStyle = color;
    canvasContext.fillRect(x, y, width, height);
};


let checkCollisions = (x, y, width, height) => {
    let leftSibling = Math.floor(x / oneBlockSize);
    let rightSibling = Math.floor((x + width - 1) / oneBlockSize);
    let topSibling = Math.floor(y / oneBlockSize);
    let bottomSibling = Math.floor((y + height - 1) / oneBlockSize);

    
    if (topSibling < 0 || bottomSibling >= map.length || leftSibling < 0 || rightSibling >= map[0].length) {
        return true;
    }

    return (
        map[topSibling][leftSibling] === 1 ||
        map[topSibling][rightSibling] === 1 ||
        map[bottomSibling][leftSibling] === 1 ||
        map[bottomSibling][rightSibling] === 1
    );
};

class Pacman {
    constructor(x, y, width, height, speed) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.speed = speed;
        this.direction = DIRECTION_RIGHT;
        this.nextDirection = this.direction;
    }

    moveProcess() {
        this.changeDirectionIfPossible();
        this.moveForward();
        if (checkCollisions(this.x, this.y, this.width, this.height)) {
            this.moveBackward();
        }
    }

    eat() {
        let mapX = Math.floor((this.x + this.width / 2) / oneBlockSize);
        let mapY = Math.floor((this.y + this.height / 2) / oneBlockSize);

        if (map[mapY] && map[mapY][mapX] === 2) {
            map[mapY][mapX] = 3; // 
            score++;
        }
    }

    moveForward() {
        switch (this.direction) {
            case DIRECTION_UP: this.y -= this.speed; break;
            case DIRECTION_LEFT: this.x -= this.speed; break;
            case DIRECTION_BOTTOM: this.y += this.speed; break;
            case DIRECTION_RIGHT: this.x += this.speed; break;
        }
    }

    moveBackward() {
        switch (this.direction) {
            case DIRECTION_UP: this.y += this.speed; break;
            case DIRECTION_LEFT: this.x += this.speed; break;
            case DIRECTION_BOTTOM: this.y -= this.speed; break;
            case DIRECTION_RIGHT: this.x -= this.speed; break;
        }
    }

    changeDirectionIfPossible() {
        if (this.direction === this.nextDirection) return;

        let tempDirection = this.direction;
        this.direction = this.nextDirection;
        this.moveForward();

        if (checkCollisions(this.x, this.y, this.width, this.height)) {
            this.moveBackward();
            this.direction = tempDirection;
        } else {
            this.moveBackward(); 
        }
    }

    draw() {
        canvasContext.beginPath();
        let angleStart = 0.2 * Math.PI;
        let angleEnd = 1.8 * Math.PI;

        // Rotar la boca según la dirección
        if (this.direction === DIRECTION_LEFT) { angleStart = 1.2 * Math.PI; angleEnd = 0.8 * Math.PI; }
        else if (this.direction === DIRECTION_UP) { angleStart = 1.7 * Math.PI; angleEnd = 1.3 * Math.PI; }
        else if (this.direction === DIRECTION_BOTTOM) { angleStart = 0.7 * Math.PI; angleEnd = 0.3 * Math.PI; }

        canvasContext.arc(
            this.x + this.width / 2,
            this.y + this.height / 2,
            this.width / 2,
            angleStart,
            angleEnd
        );
        canvasContext.lineTo(this.x + this.width / 2, this.y + this.height / 2);
        canvasContext.fillStyle = "yellow";
        canvasContext.fill();
        canvasContext.closePath();
    }
}


class Ghost {
    constructor(x, y, width, height, speed, imageX, imageY) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.speed = speed;
        this.direction = DIRECTION_RIGHT;
        this.imageX = imageX;
        this.imageY = imageY;
    }

    moveProcess() {
        this.changeDirectionRandomly();
        this.moveForward();
        if (checkCollisions(this.x, this.y, this.width, this.height)) {
            this.moveBackward();
            // Si choca, fuerza un cambio inmediato de dirección para no quedarse trabado
            let directions = [DIRECTION_UP, DIRECTION_LEFT, DIRECTION_BOTTOM, DIRECTION_RIGHT];
            this.direction = directions[Math.floor(Math.random() * directions.length)];
        }
    }

    moveForward() {
        switch (this.direction) {
            case DIRECTION_UP: this.y -= this.speed; break;
            case DIRECTION_LEFT: this.x -= this.speed; break;
            case DIRECTION_BOTTOM: this.y += this.speed; break;
            case DIRECTION_RIGHT: this.x += this.speed; break;
        }
    }

    moveBackward() {
        switch (this.direction) {
            case DIRECTION_UP: this.y += this.speed; break;
            case DIRECTION_LEFT: this.x += this.speed; break;
            case DIRECTION_BOTTOM: this.y -= this.speed; break;
            case DIRECTION_RIGHT: this.x -= this.speed; break;
        }
    }

    changeDirectionRandomly() {
        
        if (Math.random() < 0.05) {
            let directions = [DIRECTION_UP, DIRECTION_LEFT, DIRECTION_BOTTOM, DIRECTION_RIGHT];
            this.direction = directions[Math.floor(Math.random() * directions.length)];
        }
    }

    draw() {
        if (imgFantasmas && imgFantasmas.complete) {
            canvasContext.drawImage(
                imgFantasmas,
                this.imageX, this.imageY, 20, 20, // 
                this.x, this.y, this.width, this.height
            );
        } else {
            canvasContext.beginPath();
            canvasContext.arc(this.x + this.width/2, this.y + this.height/2, this.width/2, 0, 2*Math.PI);
            canvasContext.fillStyle = "red";
            canvasContext.fill();
        }
    }
}


let pacman = new Pacman(oneBlockSize, oneBlockSize, oneBlockSize, oneBlockSize, oneBlockSize / 5);
let ghosts = [
    new Ghost(9 * oneBlockSize, 10 * oneBlockSize, oneBlockSize, oneBlockSize, oneBlockSize / 5, 0, 0),
    new Ghost(10 * oneBlockSize, 10 * oneBlockSize, oneBlockSize, oneBlockSize, oneBlockSize / 5, 20, 0),
    new Ghost(11 * oneBlockSize, 10 * oneBlockSize, oneBlockSize, oneBlockSize, oneBlockSize / 5, 40, 0),
    new Ghost(10 * oneBlockSize, 9 * oneBlockSize, oneBlockSize, oneBlockSize, oneBlockSize / 5, 60, 0)
];


let drawWalls = () => {
    for (let i = 0; i < map.length; i++) {
        for (let j = 0; j < map[0].length; j++) {
            if (map[i][j] === 1) {
                createRect(j * oneBlockSize, i * oneBlockSize, oneBlockSize, oneBlockSize, wallColor);
                
                
                if (j > 0 && map[i][j - 1] === 1) {
                    createRect(j * oneBlockSize, i * oneBlockSize + wallOffset, wallSpaceWidth + wallOffset, wallSpaceWidth, wallInnerColor);
                }
                if (j < map[0].length - 1 && map[i][j + 1] === 1) {
                    createRect(j * oneBlockSize + wallOffset, i * oneBlockSize + wallOffset, wallSpaceWidth + wallOffset, wallSpaceWidth, wallInnerColor);
                }
                if (i > 0 && map[i - 1][j] === 1) {
                    createRect(j * oneBlockSize + wallOffset, i * oneBlockSize, wallSpaceWidth, wallSpaceWidth + wallOffset, wallInnerColor);
                }
                if (i < map.length - 1 && map[i + 1][j] === 1) {
                    createRect(j * oneBlockSize + wallOffset, i * oneBlockSize + wallOffset, wallSpaceWidth, wallSpaceWidth + wallOffset, wallInnerColor);
                }
            }
        }
    }
};

let drawFoods = () => {
    for (let i = 0; i < map.length; i++) {
        for (let j = 0; j < map[0].length; j++) {
            if (map[i][j] === 2) {
                createRect(
                    j * oneBlockSize + oneBlockSize / 2 - 2,
                    i * oneBlockSize + oneBlockSize / 2 - 2,
                    4, 4, "white"
                );
            }
        }
    }
};

let drawScore = () => {
    canvasContext.font = "18px 'Courier New', monospace";
    canvasContext.fillStyle = "white";
    canvasContext.fillText("SCORE: " + score, 15, 20);
};


let gameLoop = () => {
    // 1. Lógica de movimiento
    pacman.moveProcess();
    pacman.eat();
    for (let i = 0; i < ghosts.length; i++) {
        ghosts[i].moveProcess();
    }

   
    createRect(0, 0, canvas.width, canvas.height, "black");
    
   
    if (imgMapa && imgMapa.complete) {
        canvasContext.drawImage(imgMapa, 0, 0, canvas.width, canvas.height);
    }
    
    drawWalls();
    drawFoods();
    pacman.draw();
    for (let i = 0; i < ghosts.length; i++) {
        ghosts[i].draw();
    }
    drawScore();
};

let gameInterval = setInterval(gameLoop, 1000 / fps);


window.addEventListener("keydown", (event) => {
    let k = event.key; 

    if (k === "ArrowLeft" || k === "a" || k === "A") {        
        pacman.nextDirection = DIRECTION_LEFT;
    } else if (k === "ArrowUp" || k === "w" || k === "W") { 
        pacman.nextDirection = DIRECTION_UP;
    } else if (k === "ArrowRight" || k === "d" || k === "D") {
        pacman.nextDirection = DIRECTION_RIGHT;
    } else if (k === "ArrowDown" || k === "s" || k === "S") {
        pacman.nextDirection = DIRECTION_BOTTOM;
    }
});