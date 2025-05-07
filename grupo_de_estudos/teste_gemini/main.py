API_KEY_GEMINI = 'AIzaSyBCfA45yx8WeodySNKPOIZZoU12dohbVn4'

from google import genai

client = genai.Client(api_key=API_KEY_GEMINI)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works in a few words in brazilian portuguese.",
)

print(response.text)