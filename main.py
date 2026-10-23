from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import GenerateRequest
from app.security import verify_api_key
from app.services.image_service import create_image
app=FastAPI(title="PIXEYATO GEN AI API",version="1.0.0")
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=False,allow_methods=["*"],allow_headers=["*"])
@app.get("/")
async def root(): return {"ok":True,"app":"PIXEYATO GEN AI API","docs":"/docs"}
@app.get("/health")
async def health(): return {"ok":True,"status":"healthy"}
@app.post("/api/v1/images/generate",dependencies=[Depends(verify_api_key)])
async def generate(req:GenerateRequest):
    return {"ok":True,**(await create_image(req.prompt,req.size,req.quality,req.style))}
