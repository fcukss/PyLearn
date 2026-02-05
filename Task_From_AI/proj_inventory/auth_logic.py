
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

# Указываем FastAPI, где брать токен (эндпоинт /token)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    if token != 'secret_token_house':
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not valid credentials',
            headers={'www-Authenticate': 'Bearer'}
        )
    return {'username':'dr_house', 'role':'doctor'}