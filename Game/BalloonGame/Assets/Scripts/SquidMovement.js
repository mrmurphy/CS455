#pragma strict

public var trans:Transform;
public var player:GameObject;
public var globals:GameGlobals;
public var distance:Vector3;
public var distanceToSchool:Vector3;
public var velocity:float;
public var sensitivity:int;
public var rot:Quaternion;
public var restRotation:Quaternion;
public var moveRange:int;
private var captured:boolean;
public var captureRange:int;
public var following:Transform;
public var inSchool:boolean;

function Start () {
    trans = GetComponent(Transform);
    player  = GameObject.FindWithTag("Player");
    globals = GameObject.FindWithTag("Globals").GetComponent(GameGlobals);
    restRotation = trans.rotation;
    sensitivity = 10;
    velocity = 8;
    moveRange = globals.limit;
    captured = false;
    captureRange = 3;

}

function Update () {
    distanceToSchool = trans.position - Vector3(-45, -45, 0);
    if(inSchool && distanceToSchool.magnitude > 1){
        goToSchool();
    }else if(!inSchool){
        animation.Play("swim");
        distance = trans.position - player.transform.position;
        if(distance.magnitude < captureRange && !captured){
            doCapture();
        }
        if(captured) {
            if (distanceToSchool.magnitude < 5) {
                inSchool = true;
                globals.numInSchool += 1;
                globals.lastCaptured = player.transform;
                goToSchool();
            }else{follow();}
        }
        else if(distance.magnitude < sensitivity){
            flee();
            stayInBounds();
        }
        else { restState(); }
    }
}

function doCapture() {
    captured = true;
    following = globals.lastCaptured;
    globals.lastCaptured = transform;
}

function follow() {
    var newPos:Vector3 = following.position;
    newPos.x += 2 * player.GetComponent(PlayerMovement).xDirection;
    newPos.z = 0;
    moveTo(newPos);
}

function flee () {
    // Figure out the numbers.
    var move = distance.normalized;
    move.z = 0;
    // Rotate the character.
    rot = Quaternion.LookRotation(distance, -1 * Vector3.forward);
    rot.x = 0;
    rot.y = 0;
    trans.rotation = Quaternion.Slerp(trans.rotation, rot, Time.deltaTime * velocity);
    // Move the character.
    moveTo(trans.position + move);
}

function restState(){
    trans.rotation = Quaternion.Slerp(trans.rotation, restRotation, Time.deltaTime * velocity);
}

function stayInBounds(){
    if (trans.position.x > moveRange){moveTo(Vector3(moveRange, trans.position.y, 0));}
    else if (trans.position.x < -moveRange){moveTo(Vector3(-moveRange, trans.position.y, 0));}
    if (trans.position.y > moveRange){moveTo(Vector3(trans.position.x, moveRange, 0));}
    else if (trans.position.y < -moveRange){moveTo(Vector3(trans.position.x, -moveRange, 0));}
}

function moveTo(newPos:Vector3){
    trans.position = Vector3.Lerp(trans.position, newPos, Time.deltaTime * velocity);
}

function goToSchool(){
    moveTo(Vector3(-50, -50, 0));
}
