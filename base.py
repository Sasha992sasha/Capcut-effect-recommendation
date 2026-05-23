from key import api
from google import genai

client = genai.Client(api_key=api)

video = client.files.upload(file='1.mp4')

while video.state.name != 'ACTIVE':
    if video.state.name == "FAILED":
        raise Exception("Проблєма з завантаженням")
        
    video = client.files.get(name=video.name)
        

promt = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=['опиши шо робиться в відео',
    video
    ]
)

print(promt.text)