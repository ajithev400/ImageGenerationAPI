from fastapi import APIRouter, HTTPException
from app.schemas import ImageGenerationRequest
from app.services import generate_images

router = APIRouter()


@router.post("/generate")
async def generate(request: ImageGenerationRequest):
    """
    Generate images based on the provided prompt and model.

    - **model**: The model to use for image generation.
    - **prompt**: The textual prompt describing the image to generate.
    - **num_images**: The number of images to generate.
    - **width**: The width of the generated images in pixels.
    - **height**: The height of the generated images in pixels.

    **Example Request**:
    ```
    {
        "model": "ibm-granite/granite-3.0-8b-instruct",
        "prompt": "a futuristic city skyline at sunset",
        "num_images": 2,
        "width": 512,
        "height": 512
    }
    ```

    **Returns**:
    - A JSON object containing the generated image URLs and prompt details.
    """
    try:
        result = await generate_images(
            prompt=request.prompt,
            model=request.model,
            num_images=request.num_images,
            width=request.width,
            height=request.height
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))