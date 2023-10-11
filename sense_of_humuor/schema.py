from pydantic import Field

from base.schema import SystemChatGPTCompanion, UserChatGPTCompanion as HumourUserChatGPTCompanion


class HumourSystemChatGPTCompanion(SystemChatGPTCompanion):
    content: str = Field(default="Provide sense of humour to an answer")
