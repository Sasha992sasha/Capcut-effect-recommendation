from key import api
from google import genai
from my_promt import *
import json

client = genai.Client(api_key=api)

file = client.files.upload(file='1.mp4')

while file.state.name != 'ACTIVE':
    if file.state.name == "FAILED":
        raise Exception("Проблєма з завантаженням")
        
    file = client.files.get(name=file.name)
    
print('Відео завантажене')

with open('1.json',"r",encoding="utf-8") as f:
    file1 = json.load(f)

smal = {
    "duration": file1.get("duration"),
    "tracks": file1.get("tracks", []),
    "video_effects": file1["materials"].get("video_effects", []),
    "transitions": file1["materials"].get("transitions", [])
}

print('Запитання відправлене')

promt = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[promt1,
    file,
    json.dumps(smal)
    ]
)

print(promt.text)