import json


f = open("./nine_request.json", "r")
data = f.read()
data = json.loads(data)
# print(data)
response = []

for show in data["payload"]:
	if("drm" in show and "episodeCount" in show and "image" in show and
			"slug" in show and "title" in show and show["drm"] == True and 
			show["episodeCount"] > 0):
		image = show["image"]["showImage"]
		slug = show["slug"]
		title = show["title"]
		filtered_show = {"image": image, "slug": slug, "title": title}
		response.append(filtered_show)

# print(response)
for filtered_show in response:
	print(filtered_show)
	print("\n")