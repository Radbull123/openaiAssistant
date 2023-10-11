from pydantic import BaseModel, Field


class ChatGPTCompanion(BaseModel):
    role: str
    content: str


class SystemChatGPTCompanion(ChatGPTCompanion):
    role: str = Field(default="system", frozen=True)
    content: str

    
class UserChatGPTCompanion(ChatGPTCompanion):
    role: str = Field(default="user", frozen=True)
    content: str
