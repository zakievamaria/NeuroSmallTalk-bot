import os
from gigachat import GigaChat

def get_client():
    return GigaChat(
        credentials=os.environ["GIGACHAT_CREDENTIALS"],
        scope=os.getenv("GIGACHAT_SCOPE", "GIGACHAT_API_PERS"),
        verify=os.getenv("GIGACHAT_VERIFY", True),
    )
