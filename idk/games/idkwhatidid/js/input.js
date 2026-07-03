class InputHandler {
    constructor(){
        this.keys = {};

        window.addEventListener('keydown', (e) => {
            this.keys[e.code] = true;
        });

        window.addEventListener('keyup', (e) => {
            this.keys[e.code] = true;
        });
    }

    isPressed(keyCode){
        return !!this.keys[keyCode];
    }
}

//this is just for fun xd, it´s not really a game :v