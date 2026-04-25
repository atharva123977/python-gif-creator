import imageio.v3 as iio

# Image files stored in project folder
filenames = [
    "team-pic1.png",
    "team-pic2.png"
]

images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite("team.gif", images, duration=1000, loop=0)

print("GIF created successfully!")
