var DFX = 200

var glSizeX=150
var glSizeY=54
var on=false
var getLuckySong;
function setup() {
  createCanvas(400, 560);
}

function preload(){
  backgroundImage = loadImage ("images/background.png");
  DF = loadImage("images/DF.png");
  getLucky = loadImage("images/Get Lucky.png");
  getLuckySong = loadSound ("songs/get lucky music.mp3");
}

function draw() {
  background(220);
  
  imageMode(CENTER);
  image(backgroundImage,width/2,height/2,400,560);
  image(DF,DFX,240,360,220)
  
  if (mouseIsPressed && mouseX>0 && mouseX<400 && mouseY>150 && mouseY<350){
    DFX=mouseX
  }
  
  image(getLucky,200,520,glSizeX,glSizeY);
  if (on){
    glSizeX=140
    glSizeY=50
    //getLuckySong.pause();
  }else{
    glSizeX=170
    glSizeY=64
    //getLuckySong.loop();
  }
  
  textAlign(CENTER,CENTER);
  textSize(20);
  text("Press Get Lucky to Play~", width/2,40)
}

function mousePressed(){
  if (mouseIsPressed && mouseX>120 && mouseX<250 && mouseY>500 && mouseY<560){
     if(on){
     on=false;
     getLuckySong.pause();
   }else{
     on=true;
     getLuckySong.loop();
   }
  }
  
}
