import requests
pixela_endpoint= "https://pixe.la/v1/users"
TOKEN="xaverian"
USERNAME="suryaanshpoddar1"
user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"

}
#requests.post(url=pixela_endpoint,json=user_params)
#print(response.text)
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params={
    "id":"graph1000",
    "name":"cycling graph",
    "unit":"Km",
    "type":"float",
    "color":"shibafu"
}
headers={
    "X-USER-TOKEN":TOKEN

}
#response=requests.post(url=graph_endpoint,json=graph_params,headers=headers)
#print(response.text)


pixel_endpoint=f"https://pixe.la/v1/users/suryaanshpoddar1/graphs/graph1000"

headers1={
    "X-USER-TOKEN":TOKEN

}
pixel_params={
    "date":"20260330",
    "quantity":"15"
}
response=requests.post(url=pixel_endpoint,json=pixel_params,headers=headers1)
print(response.text)



