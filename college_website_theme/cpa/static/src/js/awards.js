
  gsap.registerPlugin(Draggable, InertiaPlugin);

var slideDelay = 4;
var slideDuration = 4;
var wrap = true;

var slides = document.querySelectorAll(".slide");
var prevButton = document.querySelector("#prevButton");
var nextButton = document.querySelector("#nextButton");
var progressWrap = gsap.utils.wrap(0, 1);

var numSlides = slides.length;

gsap.set(slides, {

  xPercent: i =&gt; i * 100
});

var wrapX = gsap.utils.wrap(-100, (numSlides - 1) * 100);
var timer = gsap.delayedCall(slideDelay, autoPlay);

var animation = gsap.to(slides, {
  xPercent: "+=" + (numSlides * 100),
  duration: 4,
  ease: "none",
  paused: true,
  repeat: -1,
  modifiers: {
    xPercent: wrapX
  }
});

var proxy = document.createElement("div");
var slideAnimation = gsap.to({}, {});
var slideWidth = 0;
var wrapWidth = 0;

var draggable = new Draggable(proxy, {
  trigger: ".slides-container",
  inertia: true,
  onPress: updateDraggable,
  onDrag: updateProgress,
  onThrowUpdate: updateProgress,
  snap: {
    x: snapX
  }
});

resize();

window.addEventListener("resize", resize);

prevButton.addEventListener("click", function() {
  animateSlides(1);
});

nextButton.addEventListener("click", function() {
  animateSlides(-1);
});

function updateDraggable() {
  timer.restart(true);
  slideAnimation.kill();
  this.update();
}

function animateSlides(direction) {

  timer.restart(true);
  slideAnimation.kill();
  var x = snapX(gsap.getProperty(proxy, "x") + direction * slideWidth);

  slideAnimation = gsap.to(proxy, {
    x: x,
    duration: slideDuration,
    onUpdate: updateProgress
  });
}

function autoPlay() {
  if (draggable.isPressed || draggable.isDragging || draggable.isThrowing) {
    timer.restart(true);
  } else {
    animateSlides(-1);
  }
}

function updateProgress() {
  animation.progress(progressWrap(gsap.getProperty(proxy, "x") / wrapWidth));
}

function snapX(value) {
  let snapped = gsap.utils.snap(slideWidth, value);
  return wrap ? snapped : gsap.utils.clamp(-slideWidth * (numSlides - 1), 0, snapped);
}

function resize() {

  var norm = (gsap.getProperty(proxy, "x") / wrapWidth) || 0;

  slideWidth = slides[0].offsetWidth;
 wrapWidth = (slideWidth + 20) * numSlides; // 👈 match the margin


  wrap || draggable.applyBounds({minX: -slideWidth * (numSlides - 1), maxX: 0});

  gsap.set(proxy, {
    x: norm * wrapWidth
  });

  animateSlides(0);
  slideAnimation.progress(1);
}



