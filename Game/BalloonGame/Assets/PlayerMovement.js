#pragma strict

private var charCont:CharacterController;
var moveMult:float = 0.4;
// This is inverted. The higher the number, the slower the turn.
var turnSpeed:float = 1;

function Start () {
    charCont = GetComponent(CharacterController);
    audio.volume = 0;
    audio.loop = true;
}

function Update () {
    // Do some key reactions.
    var axis:float;
    if(Input.GetAxis("Horizontal") || Input.GetAxis("Vertical")){
        if(Input.GetAxis("Horizontal")){
            // Play audio
            fadeInAudio();
            // Move backwards and forwards
            var curZ = charCont.transform.position.z;
            axis = Input.GetAxis("Horizontal");
            if(curZ < 45 && axis < 0){
                charCont.Move(Vector3(0, 0, moveMult * axis * -1));
            }else if(curZ > -45 && axis > 0){
                charCont.Move(Vector3(0, 0, moveMult * axis * -1));
            }
            animation.CrossFade("swim_normal");

            // Take care of turning.
            var cur:float = charCont.transform.eulerAngles.y;
            var dif:float;
            if(axis < 0){
                if(cur != 0){
                    dif = 0 - cur;
                    if (dif < 1 && dif > -1){
                        charCont.transform.eulerAngles.y = 0;
                    }else{
                        charCont.transform.eulerAngles.y += dif / 6;
                    }
                }
            }else if(axis > 0){
                if(cur != 180){
                    dif = 180 - cur;
                    if (dif < 1 && dif > -1){
                        charCont.transform.eulerAngles.y = 180;
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
            if(curY < 45 && axis > 0){
                charCont.Move(Vector3(0, moveMult * axis, 0));
            }else if(curY > -45 && axis < 0){
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