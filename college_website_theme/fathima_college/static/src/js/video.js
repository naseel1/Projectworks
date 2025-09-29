  function playPause(videoId) {
    var video = document.getElementById(videoId);
    var playButtonImage = document.getElementById('playButtonImage');

    if (video.paused) {
        video.play();
        playButtonImage.classList.add('hidden');
    } else {
        video.pause();
        playButtonImage.classList.remove('hidden');
    }
}