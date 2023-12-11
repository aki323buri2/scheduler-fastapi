import uvicorn 
import nest_asyncio

if __name__ == "__main__": 
  nest_asyncio.apply() 
  uvicorn.run("app.main:app")