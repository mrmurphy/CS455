#pragma strict

private var charCont:CharacterController;
var moveMult:float = 0.4;
// This is inverted. The higher the number, the slower the turn.
var turnSpeed:float = 1;
var moveRange:int = 45;

function Start () {
    charCont = GetComponent(CharacterController);
    audio.volume = 0;
    audio.loop = true;
}

function Update () {
    // Do some key reactions.
    var axis:float;
    var dif:float;
    if(Input.GetAxis("Horizontal") || Input.GetAxis("Vertical")){
        if(Input.GetAxis("Horizontal")){
            // Play audio
            fadeInAudio();
            // Move backwards and forwards
            var curX = charCont.transform.position.x;
            axis = Input.GetAxis("Horizontal");
            if(curX < moveRange && axis < 0){
                charCont.Move(Vector3(moveMult * axis * -1, 0, 0));
            }else if(curX > -moveRange && axis > 0){
                charCont.Move(Vector3(moveMult * axis * -1, 0, 0));
            }
            animation.CrossFade("swim_normal");

            // Take care of turning.
            var cur:float = charCont.transform.eulerAngles.y;
            if(axis < 0){
                if(cur != 90){
                    dif = 90 - cur;
                    if (dif < 1 && dif > -1){
                        charCont.transform.eulerAngles.y = 90;
                    }else{
                        charCont.transform.eulerAngles.y += dif / 6;
                    }
                }
            }else if(axis > 0){
                if(cur != 270){
                    dif = 270 - cur;
                    if (dif < 1 && dif > -1){
                        charCont.transform.eulerAngles.y = 270;
                    }else{
                        charCont.transform.eulerAngles.y += dif / 6;
                    }
                }
            }
        }
        if(Input.GetAxis("Vertical")){
            fadeInAudio();
            // Move up and down
            var curY = charCont.transform.position.y;
            axis = Input.GetAxis("Vertical");
            if(curY < moveRange && axis > 0){
                charCont.Move(Vector3(0, moveMult * axis, 0));
            }else if(curY > -moveRange && axis < 0){
                charCont.Move(Vector3(0, moveMult * axis, 0));
            }
            animation.CrossFade("swim_normal");
        }
    }else{
        assumeRestState();
    }

}

function assumeRestState(){
    // Set up rest state
    animation.CrossFade("rest");
    fadeOutAudio();
}

function fadeOutAudio(){
    var step:float = 0.04;
    if(audio.volume > 0){
        audio.volume -= step;
    }
}
function fadeInAudio(){
    var step:float = 0.04;
    if(audio.volume < 0.7){
        audio.volume += step;
    }
}
