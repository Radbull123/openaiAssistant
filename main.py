import openai
import uvicorn

from fastapi import FastAPI, Depends
from fastapi.responses import StreamingResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from base.schema import UserChatGPTCompanion
from sense_of_humuor.app import get_prompt as humour_get_prompt


app = FastAPI(debug=True, title="AI Generator")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("funny/gpt-4")
def get_output(user_input: UserChatGPTCompanion = Depends(UserChatGPTCompanion)):
    resp = openai.ChatCompletion.create(
        model="gpt-4",
        messages=humour_get_prompt(user_prompt=user_input.content),
        temperature=0.8,
        max_tokens=1000,
    )
    return resp['choices'][0].message.content


@app.get("/image")
def get_image_output(user_input: UserChatGPTCompanion = Depends(UserChatGPTCompanion)):
    response = openai.Image.create(
        prompt=user_input.content,
        n=1,
        size="1024x1024"
    )
    return RedirectResponse(response['data'][0]['url'])


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)