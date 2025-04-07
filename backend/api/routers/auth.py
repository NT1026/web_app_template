from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import JSONResponse

from auth.jwt import create_token_pair, verify_token
from auth.passwd import verify_password
from crud.auth import AuthCrudManager
from schemas import auth as AuthSchema

exception_invalid_login = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect username or password",
    headers={"WWW-Authenticate": "Bearer"},
)

invalid_token = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid token",
    headers={"WWW-Authenticate": "Bearer"},
)

AuthCrud = AuthCrudManager()
router = APIRouter(prefix="/auth", tags=["Users"])


@router.post("/login", response_model=AuthSchema.Token)
async def login(form_data: AuthSchema.login_form_schema):
    """
    Login with the following information:
    - **username**
    - **password**

    """
    user_in_db = await AuthCrud.user_login(form_data.username)

    if user_in_db is None:
        raise exception_invalid_login

    if not verify_password(form_data.password, user_in_db.password):
        raise exception_invalid_login

    # Create access_token and refresh_token
    token_pair = await create_token_pair(user_in_db)

    # Set cookies for access_token and refresh_token
    response = JSONResponse(content=token_pair.model_dump())
    response.set_cookie(
        key="access_token",
        value=token_pair.access_token,
        httponly=True,
        secure=True,
        samesite="None",
        path="/",
    )
    response.set_cookie(
        key="refresh_token",
        value=token_pair.refresh_token,
        httponly=True,
        secure=True,
        samesite="None",
        path="/",
    )

    return response


@router.post("/refresh", response_model=AuthSchema.Token)
async def refresh(request: Request):
    """
    Use the refresh_token (in Cookie header) to generate a new access token pair.
    """
    payload: dict = await verify_token(request.cookies.get("refresh_token"))
    if payload is None:
        raise invalid_token

    uid: str = payload.get("uid")
    if uid is None:
        raise invalid_token

    user_in_db = await AuthCrud.user_login(uid)

    # Create access_token and refresh_token
    token_pair = await create_token_pair(user_in_db)

    # Set cookies for access_token and refresh_token
    response = JSONResponse(content=token_pair.model_dump())
    response.set_cookie(
        key="access_token",
        value=token_pair.access_token,
        httponly=True,
        secure=True,
        samesite="None",
        path="/",
    )
    response.set_cookie(
        key="refresh_token",
        value=token_pair.refresh_token,
        httponly=True,
        secure=True,
        samesite="None",
        path="/",
    )

    return response


@router.post("/logout")
async def logout():
    """
    Delete the access_token and refresh_token cookies.
    """
    response = JSONResponse(content={"message": "Logged out successfully"})
    response.set_cookie(
        key="access_token",
        value="",
        httponly=True,
        secure=True,
        samesite="None",
        path="/",
        max_age=0,
    )
    response.set_cookie(
        key="refresh_token",
        value="",
        httponly=True,
        secure=True,
        samesite="None",
        path="/",
        max_age=0,
    )

    return response
