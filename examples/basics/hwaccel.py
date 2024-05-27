import av
import av.datasets
import time

n = 10

ti = time.time()
for i in range(n):
    container = av.open(av.datasets.curated("pexels/time-lapse-video-of-night-sky-857195.mp4"))
    for frame in container.decode(video=0):
        pass
print('CPU decoder: {} [s]'.format(time.time()-ti))

hwaccel = {'device_type_name': 'cuda'}
ti = time.time()
for i in range(n):
    container = av.open(av.datasets.curated("pexels/time-lapse-video-of-night-sky-857195.mp4"), hwaccel=hwaccel)
    for frame in container.decode(video=0):
        pass
print('GPU decoder: {} [s]'.format(time.time()-ti))