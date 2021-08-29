$(function() {

  // Simple calculacting
  let now = Date.now();
  let dob = new Date(2003, 2, 15);
  let age = Math.floor((now - dob) / (1000*60*60*24*365));

  $(".typed").typed({
    strings: [
      "stat mindestroyer.human<br/>" +
      `><span class='caret'>$</span> years: ${age} </br>` +
      "><span class='caret'>$</span> skills: python, docker, git, bash<br/> ^100" +
      "><span class='caret'>$</span> job status: <a href='https://freelancehunt.com/freelancer/github-localhost.html'>freelancer</a></br> ^100" +
      "><span class='caret'>$</span> hobbies: books, travel, code ❤️ <br/> ^300" +
      "><span class='caret'>$</span> alias: github-localhost <br/>"


    ],
    showCursor: true,
    cursorChar: '_',
    autoInsertCss: true,
    typeSpeed: 0.001,
    startDelay: 50,
    loop: false,
    showCursor: false,
    onStart: $('.message form').hide(),
    onStop: $('.message form').show(),
    onTypingResumed: $('.message form').hide(),
    onTypingPaused: $('.message form').show(),
    onComplete: $('.message form').show(),
    onStringTyped: function(pos, self) {$('.message form').show();},
  });
  $('.message form').hide()
});
