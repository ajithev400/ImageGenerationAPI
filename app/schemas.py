from pydantic import BaseModel

class ImageGenerationRequest(BaseModel):
    prompt: str
    model: str = "ibm-granite/granite-3.0-8b-instruct"
    num_images: int = 1
    width: int = 512
    height: int = 512
