var timer = new easytimer.Timer();




	timer.addEventListener('secondsUpdated', function (e) {
	    $('#basicUsage').html(timer.getTimeValues().toString());
	});

  function __log(e, data) {
    log.innerHTML += "\n" + e + " " + (data || '');
  }
  var i;
  var audio_context;
  var recorder;
  function startUserMedia(stream) {
  	audio_context = new AudioContext;
    var input = audio_context.createMediaStreamSource(stream);
    //__log('Media stream created.');
    // Uncomment if you want the audio to feedback directly
    //input.connect(audio_context.destination);
    //__log('Input connected to audio context destination.');
    
    recorder = new Recorder(input);
    //__log('Recorder initialised.');
  }
  function startRecording(button) {
  	i=0;
  	timer.start();
    recorder && recorder.record();
    button.disabled = true;
    $( "#stop" ).prop( "disabled", false );
    $( "#pause" ).prop( "disabled", false );
    //button.nextElementSibling.disabled = false;
    //__log('Recording...');
  }
  function stopRecording(button) {
  	timer.stop()
    recorder && recorder.stop();
    button.disabled = true;
    button.previousElementSibling.disabled = false;
    //__log('Stopped recording.');
    
    // create WAV download link using audio data blob
    createDownloadLink();
    
    recorder.clear();

    $("#1").toggleClass('active disabled');
    $("#2").addClass('active');
  }
  function pauseRecording(button) {
    if (recorder.recording){
		//pause
		timer.pause()
		recorder.stop();
		button.innerHTML="Reprendre";
	}else{
		//resume
		timer.start();
		recorder.record()
		button.innerHTML="Pause";

	}
  }
  function createDownloadLink() {
    recorder && recorder.exportWAV(function(blob) {
      var url = URL.createObjectURL(blob);
      var li = document.createElement('li');
      var au = document.createElement('audio');
      var hf = document.createElement('a');

      console.log(url);
      
      au.controls = true;
      au.src = url;
      hf.href = url;
      hf.download = new Date().toISOString() + '.wav';
      hf.innerHTML = hf.download;
      //li.appendChild(au);
      //li.appendChild(hf);
      //recordingslist.appendChild(li);
      hf.click();


      $.ajax({
        url: '/ajax/synthetiseur/',
        data: {'url': hf.download},
        dataType: 'json',
        success: function (texte) {
            //alert(texte['texte']);
            alert(texte['texte']);

            $(".card").toggleClass('text-center');
            $(".card-body").load('../listeMaladies/', texte);
          }
        }
		);
    });
  }
  window.onload = function init() {
    try {
      // webkit shim
      window.AudioContext = AudioContext
      navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia;
      window.URL = window.URL || window.webkitURL;
      
      //__log('Audio context set up.');
      //__log('navigator.getUserMedia ' + (navigator.getUserMedia ? 'available.' : 'not present!'));
    } catch (e) {
      alert('No web audio support in this browser!');
    }
    
    navigator.getUserMedia({audio: true}, startUserMedia, function(e) {
      //__log('No live audio input: ' + e);
    });
  };

  $('#start').click(function () {
  	startRecording(this);	
  });

  $("#stop").click(function () {
  	stopRecording(this);
  		
  });

  $("#pause").click(function () {
  	pauseRecording(this);
  		
  });