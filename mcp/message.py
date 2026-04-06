from pydantic import BaseModel

class MCPMessage(BaseModel):
    sender: str
    receiver: str
    content: str
    metadata: dict = {}