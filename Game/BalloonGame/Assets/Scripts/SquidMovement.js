#pragma strict

private var trans:Transform;
private var player:GameObject;
public var distance:Vector3;
public var velocity:float;
public var sensitivity:int;
public var rot:Quaternion;
public var restRotation:Quaternion;
public var moveRange:int;

function Start () {
    trans = GetComponent(Transform);
    player  = GameObject.FindWithTag("Player");
    restRotation = trans.rotation;
    sensitivity = 10;
    velocity = 8;
    moveRange = 40;
}

function Update () {
    animation.Play("swim");
    distance = trans.position - player.transform.position;
    if(distance.magnitude < sensitivity){ flee(); }
    else { restState(); }
    stayInBounds();
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
