class MediaFile:
    def __init__(self, media):
        self._media = media

    def play():
        pass

    def __str__(self):
        return f"Media Filename:{self._media}"


class AudioFile(MediaFile):
    def __init__(self, file):
        super().__init__(file)
        self.file = file

    def play(self):
        print(f"Playing audio file {self.file}")


class VideoFile(MediaFile):
    def __init__(self, file):
        super().__init__(file)
        self.file = file

    def play(self):
        print(f"Playing video file {self.file}")


media_files = [
    AudioFile("song.mp3"),
    VideoFile("movie.mp4"),
    AudioFile("podcast.wav"),
    VideoFile("tutorial.avi"),
]

for media in media_files:
    print(media)
    media.play()
