from fastapi import FastAPI,Depends,status

from pydantic import BaseModel

import models ,schemas

from database import engine,SessionLocal

from sqlalchemy.orm import Session



app = FastAPI()


# this will create all below mentioned
models.Base.metadata.create_all(engine)


def get_db():
    
   db=SessionLocal()
   
   try:
       
       yield db
       
   finally:
    
       db.close()
       
       
       
       
       
class User(BaseModel):
    id:int
    name:str
    email:str
    password:str
    
    
    
# Create new user

@app.post("/create-user")
def createUser(request:User,db:Session=Depends(get_db)):
    
    new_user=models.Users(name=request.name,email=request.email,password=request.password)
    
    db.add(new_user)
    
    db.commit()
    
    db.refresh(new_user)
    
    return f'A new user has been created successfully with name : {new_user.name}'



# Get all users

@app.get("/users")
def getAllUsers(db:Session=Depends(get_db)):
    allUsers=db.query(models.Users).all()
    return allUsers




# Delete user


@app.delete('/user/{id}',status_code=status.HTTP_200_OK)
def delete_user(id, db:Session=Depends(get_db)):
    db.query(models.Users).filter(models.Users.id==id).delete(synchronize_session=False)
    db.commit()
    return 'Message : User has been deleted successfully'
    
    


# Update user

@app.put('/{id}', status_code=status.HTTP_200_OK)
def update_user(id, request: schemas.User, db: Session = Depends(get_db)):
    updated=db.query(models.Users).filter(models.Users.id==id).update({'name':request.name,'email':request.email,'password':request.password})
    db.commit()
    return 'New values has been updated successfully'



   
    