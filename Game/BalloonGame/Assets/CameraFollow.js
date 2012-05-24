#pragma strict

var target:GameObject;
private var trans:Transform;

function Start (){
    trans = GetComponent(Transform);
}

function Update () {
    trans.position.y  = target.transform.position.y;
    trans.position.z  = target.transform.position.z;
}