
# Image Generation API Documentation

## Overview
The Image Generation API allows users to generate images based on textual prompts using a specified model. This API provides an endpoint to create multiple images with customizable dimensions.

## Base URL
```
http://127.0.0.1:8000/api/v1/images/generate
```

## Environment Configuration

Before using the API, you need to configure your environment by creating a `.env` file in the root of your project. Add the following line to the file:

```
REPLICATE_API_KEY="add your token"
```

Replace `"add your token"` with your actual Replicate API key.

## Endpoint
### POST /api/v1/images/generate

This endpoint generates images based on the provided prompt and model.

### Request

**Content-Type:** `application/json`

**Request Body:**
```json
{
    "model": "ibm-granite/granite-3.0-8b-instruct",
    "prompt": "a futuristic city skyline at sunset",
    "num_images": 2,
    "width": 512,
    "height": 512
}
```

#### Parameters

| Parameter | Type   | Required | Description                                        |
|-----------|--------|----------|----------------------------------------------------|
| model     | string | Yes      | The model to use for image generation.             |
| prompt    | string | Yes      | The textual prompt describing the image to generate.|
| num_images| integer| Yes      | The number of images to generate.                   |
| width     | integer| Yes      | The width of the generated images in pixels.       |
| height    | integer| Yes      | The height of the generated images in pixels.      |

### Example Request
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/images/generate" \
  -H "Content-Type: application/json" \
  -d '{
        "model": "ibm-granite/granite-3.0-8b-instruct",
        "prompt": "a futuristic city skyline at sunset",
        "num_images": 2,
        "width": 512,
        "height": 512
      }'
```

### Response

**Successful Response:**
```json
{
    "image_urls": [
        "https://example.com/image1.png",
        "https://example.com/image2.png"
    ],
    "prompt": "a futuristic city skyline at sunset",
    "model": "ibm-granite/granite-3.0-8b-instruct"
}
```

#### Response Fields

| Field       | Type     | Description                                 |
|-------------|----------|---------------------------------------------|
| image_urls  | array    | An array of URLs pointing to the generated images. |
| prompt      | string   | The original prompt used for image generation. |
| model       | string   | The model used for generating the images.  |

### Error Handling

The API may return the following error responses:

**Error Response:**
```json
{
    "error": "ReplicateError Details:\ntitle: Unauthenticated\nstatus: 401\ndetail: You did not pass an authentication token"
}
```
This error indicates that the API request was not authenticated. Ensure that you are providing a valid API key if authentication is required.

#### Common Error Codes

| HTTP Status Code | Error Message                              | Description                                      |
|------------------|--------------------------------------------|--------------------------------------------------|
| 400              | Bad Request                                | The request was invalid or malformed.            |
| 401              | Unauthenticated                            | Missing or invalid authentication token.         |
| 422              | Invalid version or not permitted           | The specified model version does not exist or access is denied. |

## Conclusion
This API enables the generation of images based on textual prompts, providing a flexible way to create visuals for various applications. Make sure to provide valid parameters and check the response for any errors during the request.

--- 

