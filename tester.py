from subtitler import Video


v = Video("test.mp4")

v.addSubtitle("According to all known laws of aviation", "0:00:00.00", "0:00:10.00")
v.addSubtitle("there is no way that a bee should be able", "0:00:10.00", "0:00:20.00")
v.addSubtitle("to fly. It's tiny wings are too small", "0:00:20.00", "0:00:30.00")
v.addSubtitle("to get its fat little body off the ground", "0:00:30.00", "0:00:40.00")
v.addSubtitle("The bee of course, flies anyway for bees", "0:00:40.00", "0:00:50.00")
v.addSubtitle("don't care what humans think are impossible", "0:00:50.00", "0:01:00.00")

v.createVideo()