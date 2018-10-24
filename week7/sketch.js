// Daniel Shiffman
// http://codingtra.in
// http://patreon.com/codingtrain

// Video: https://youtu.be/DZlw-IS5OkI

let angle = 0;
let kitten;
let cam;

// function preload() {
//   kitten = loadImage('kittens/kitten2.jpg');
// }

function setup() {
  createCanvas(400, 300, WEBGL);
  cam = createCapture(VIDEO);
  cam.size(640, 480);
  cam.hide();
}

function draw() {
  background(0);
  ambientLight(255);
  rotateX(angle);
  rotateY(angle * 1.3);
  rotateZ(angle * 0.7);
  //box(100);

  //fill(255);
  texture(cam);
  translate(-50, -50);
  beginShape();
  vertex(mouseY, 0, 0, 0, 0);
  vertex(mouseX, 0, 0, 1, 0);
  vertex(100, 100, 0, 1, 1);
  vertex(0, 200, 0, 0, 1);
  endShape(CLOSE);

  // angle += 0.03;
}
