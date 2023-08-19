from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

@app.get('/numbers')
async def get_numbers(url: str):
    urls = url.split(',')
    valid_numbers = []

    for url in urls:
        num = await fetch_numbers_from_url(url)
        if num is not None:
            valid_numbers.extend(num)

    sorted_unique_numbers = sorted(set(valid_numbers))
    return {"numbers": sorted_unique_numbers}

async def fetch_numbers_from_url(url):
    try:
        response = await requests.get(url, timeout=0.5)
        if response.status_code == 200:
            data = response.json()
            if "numbers" in data and isinstance(data["numbers"], list):
                return data["numbers"]
    except requests.exceptions.Timeout:
        pass
    except:
        pass
    return None
