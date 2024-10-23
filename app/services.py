import replicate
from app.config import settings


client = replicate.Client(api_token=settings.replicate_api_key)

async def generate_images(prompt: str, model: str, num_images: int, width: int, height: int):
    
    try:
        
        result = client.run(
            # "ibm-granite/granite-3.0-8b-instruct",
            f"{model}",
            input={
                "prompt": prompt,
                "num_outputs": num_images,
                "width": width,
                "height": height
            }
        )
    except Exception as e:
        print(f"Error while generating images: {str(e)}")
        return {"error": str(e)}


    image_urls = [output for output in result]

    return {
        "image_urls": image_urls,
        "prompt": prompt,
        "model": model
    }
