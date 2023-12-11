from fastapi import FastAPI 
from apscheduler.schedulers.background import BackgroundScheduler 
from contextlib import asynccontextmanager 
import nest_asyncio
import uvicorn 

counter = 1

def job_counter(): 
  global counter 
  print("cron job: call you https requests here...")
  counter = counter + 1

@asynccontextmanager
async def lifespan(_: FastAPI):
  print("app started...")
  scheduler = BackgroundScheduler()
  scheduler.add_job(
    id="job1", 
    func=job_counter, 
    trigger="cron", 
    second="*/2", 
  )
  scheduler.start()
  yield 
  print("app stoped...")
  scheduler.shutdown(wait=False)
  print("scheduler shutdowned...")

app = FastAPI(lifespan=lifespan) 

if __name__ == "__main__": 
  nest_asyncio.apply() 
  uvicorn.run(app)