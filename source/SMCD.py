# curl -output downloaded_video.mp4 "https://scontent.cdninstagram.com/v/t66.30100-16/10000000_1147394612884876_8892301864761697522_n.mp4?_nc_ht=scontent.cdninstagram.com&_nc_cat=104&_nc_ohc=fQvrgkb8AgEAX95ZnvA&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfDzH2730qQIo_1jiXys44hli2yDO8tiPd2drlhF1mMJzg&oe=6522426A&_nc_sid=10d13b"

import requests

url = "https://scontent.cdninstagram.com/v/t66.30100-16/10000000_1147394612884876_8892301864761697522_n.mp4?_nc_ht=scontent.cdninstagram.com&_nc_cat=104&_nc_ohc=fQvrgkb8AgEAX95ZnvA&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfDzH2730qQIo_1jiXys44hli2yDO8tiPd2drlhF1mMJzg&oe=6522426A&_nc_sid=10d13b"

response = requests.get(url)

if response.status_code == 200:
	with open("downloaded_video.mp4", "wb") as file:
		file.write(response.content)
		print("Video downloaded successfully.")
else:
	print(f"Failed to download the video. Status code: {response.status_code}")

