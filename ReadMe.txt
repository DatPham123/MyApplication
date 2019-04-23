The following list is which programs correlate with
controlling the various components of the bird feeder.

MotionDetectorServer.py //listens for motion on the motion
			//detector

StreamingServer.py //must be run with python3 by using the
		   //command "python3 StreamingServer.py"
		   //on the command line while in the IoT
		   //directory. This listens for the
		   //command sent by the play button in
		   //the android app to begin streaming

ServoServer.py //listens for the command sent by the feed
	       //button in the Android app to make the
	       //motor move ~90 degrees to release food.

WeightSensorTest.py // returns 0 if there's not enough
		    //weight to trip it and 1 if there is.
		    //use of pre-loading it with quaters
		    //or something else can allow lower
		    //weights to trip it over to 1.

Issues:
-MotionDetectorServer.py and StreamignServer.py cannot
currently run at the same time, because they are both
accessing the pi camera.

-Servo Motor has a slight twitch to it for calibration,
which releases some food. This will probably be best
addressed with better bird feeder construction.

-The weight sensor programming is not integrated into
anything right now, it just returns 0 if there's not 
enough weight to trip it and 1 if there is.