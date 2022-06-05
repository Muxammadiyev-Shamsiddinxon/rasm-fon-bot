import requests
import logging

url = "https://background-removal.p.rapidapi.com/remove"

headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Host": "background-removal.p.rapidapi.com",
	"X-RapidAPI-Key": "dd51770201msh0a2aaf1c3b38cdbp1136d3jsn24b131b455cc"
          }
  # test payload
  # payload = "image_url=https%3A%2F%2Fobjectcut.com%2Fassets%2Fimg%2Fraven.jpg"

async def remove_background(img_url):
    payload = f"image_url={img_url}"
    response = requests.request("POST", url, data=payload, headers=headers)
    # logging.info(response.json()['response']['image_url'])
    return response.json()['response']['image_url']