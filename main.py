from typing import List
from models import ImageList
from fastapi import FastAPI, Query, Path
from data import dogs, cats
import random

BASEURL = "https://res.cloudinary.com/nametest/image/upload/"

data_set = {
    "dog": dogs,
    "cat": cats
}
app = FastAPI(title="Random Animal Image API",
              version="1.0",
              description="Get Random Animal Images Such As Cats, Dogs Etc.",
              contact={
                  "name": "Bijay Kumar Nayak",
                  "email": "bijay6779@gmail.com"
              })


def gen_random_img(selector: List[str], limit: int) -> ImageList:
    arr = []
    data = ImageList()
    for _ in range(limit):
        rand_img = random.choice(selector)
        arr.append(BASEURL + rand_img)
        data.results = arr
    return data


@app.get("/", response_model=ImageList, tags=["Get Random Image"])
async def get_random_image(limit: int = Query(default=1, description="Number Of Random Image To Fetch", gt=0, le=10)):
    """
    Get Random Animal Images Such As Cats, Dogs Etc.
    """
    random_category = random.choice(list(data_set.keys()))
    selector = data_set[random_category]
    data = gen_random_img(selector, limit)
    return data


@app.get("/random/{animal}", response_model=ImageList, tags=["Get Random Image"])
async def get_random_image_by_animal_type(animal: str = Path(example="dog", description="Get Particular Animal Image"),
                                     limit: int = Query(default=1, description="Number Of Random Image To Fetch", gt=0,
                                                        le=10)):
    """
        Get Customised Animal List Such As 10 Random Dog Images.

        Accepted Value: dog, cat
    """
    if animal in data_set:
        selector = data_set[animal]
        data = gen_random_img(selector, limit)
        return data
