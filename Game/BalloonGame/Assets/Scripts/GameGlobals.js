#pragma strict

var numFreddies:int;
var numInSchool:int;
var limit:int;
var Freddy:Transform;
var lastCaptured:Transform;
var scoreText:GUIText;
var messageText:GUIText;
var clockText:GUIText;
private var showEndScreen:boolean;
var endTime:float;
var playTime:float;
var timeLeft:int;

function Start () {
    numFreddies = 20;
    numInSchool = 0;
    limit = 45;
    playTime = 100; // In seconds.
    showEndScreen = false;

    // Instantiate Freddies:
    for (var i = numFreddies; i > 0; i--) {
        var randPos:Vector3 = Vector3(Random.Range(limit, -limit),
                                       Random.Range(limit, -limit),
                                       0);
        Instantiate(Freddy, randPos, Quaternion.identity);
    }

    // Set turtle to be the last captured, since nobody is yet:
    lastCaptured = GameObject.FindWithTag("Player").transform;

    // Take care of the message text:
    messageText.text = "";

    // Set up the timer
    endTime = Time.time + playTime;
    Time.timeScale = 1;
}

function Update () {
    scoreText.text = numInSchool + "/" + numFreddies + " Freddies in school.";
    if(numInSchool == numFreddies) {GameOver("Great Job!");}

    // Update clock
    timeLeft = endTime - Time.time;
    if (timeLeft <= 0) { GameOver("Oops, too late!"); }
}

function OnGUI (){
    clockText.text = "Time left: " + timeLeft;
    if(showEndScreen){
        if (GUI.Button (new Rect(10, 10, 200, 100),"Start Over")){
            Application.LoadLevel(0);
        }
    }

}

function GameOver (message:String) {
    showEndScreen = true;
    messageText.text = message;
    Time.timeScale = 0;
}
