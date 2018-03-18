ready(app);

function ready(fn) {
  if (document.attachEvent ? document.readyState === "complete" : document.readyState !== "loading"){
    fn();
  } else {
    document.addEventListener('DOMContentLoaded', fn);
  }
}

let clock, timer, timerEnd;

function app() {
    clock = document.querySelector('.duration');

    if (clock) {
        timer = moment.duration(clock.innerText);
        timerEnd = setInterval(fireCountdown,1000);
    }
}

function fireCountdown() {
    timer.subtract(1, 'second');
    showCountdown();

    if(timer.asSeconds() === 0) {
        clearInterval(timerEnd);
    }
}

function showCountdown() {
    if (clock) {
        clock.innerText = `${timer.hours() >= 10 ? timer.hours() : '0' + timer.hours()}:${timer.minutes() >= 10 ? timer.minutes() : '0' + timer.minutes()}:${timer.seconds() >= 10 ? timer.seconds() : '0' + timer.seconds()}`;
    }
}