from sense_of_humuor.schema import HumourSystemChatGPTCompanion, HumourUserChatGPTCompanion


def get_prompt(user_prompt: str):
    return HumourSystemChatGPTCompanion().model_dump(), HumourUserChatGPTCompanion(content=user_prompt).model_dump()
