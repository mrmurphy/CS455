#pragma strict

private var charCont:CharacterController;
var moveMult:float = 0.4;
// This is inverted. The higher the number, the slower the turn.
var turnSpeed:float = 1;

function Start () {
    charCont = GetComponent(CharacterController);
}

function Update () {
    animation.CrossFade("rest");
    var axis:float;
    if(Input.GetAxis("Horizontal")){
        // Move backwards and forwards
        axis = Input.GetAxis("Horizontal");
        charCont.Move(Vector3(0, 0, moveMult * axis * -1));
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
        // Move up and down
        axis = Input.GetAxis("Vertical");
        charCont.Move(Vector3(0, moveMult * axis, 0));
        animation.CrossFade("swim_normal");
    }

}