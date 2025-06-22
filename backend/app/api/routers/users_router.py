from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status

from app.api.deps_auth import get_current_user
from app.api.deps_auth import get_user_service
from app.api.schemas.users_schemas import Token, User, UserCreate, UserResponse

from app.domain.services.user_service import UserService
from app.domain.entities.user_entity import User as UserDomain
from app.infra.auth.jwt_functions import create_access_token, authenticate_user

from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="", tags=["Users"])

ACCESS_TOKEN_EXPIRE_MINUTES = 30


@router.post(
    "/login",
    summary="Authenticate user and issue token",
    description="Authenticate a user using CPF (username) and password, returning a JWT access token for subsequent requests.",
    response_model=Token,
    responses={401: {"description": "Incorrect username or password"}},
)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    user_service: UserService = Depends(get_user_service),
):
    """This endpoint is used to authenticate a user and return an access token."""

    try:
        user = await authenticate_user(
            form_data.username, form_data.password, user_service
        )
        if user is None:
            raise ValueError("Invalid credentials")
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.cpf}, # type: ignore
        expires_delta=access_token_expires,  # type: ignore
    )
    return Token(access_token=access_token, token_type="bearer")


@router.post(
    "/register",
    summary="Register new user",
    description="Register a new user in the system. Returns the created user (without password).",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    responses={400: {"description": "User with this CPF already exists"}},
)
async def register_user(
    user: UserCreate,
    user_service: UserService = Depends(get_user_service),
):
    """This endpoint allows the registration of a new user in the system."""
    try:
        existing_user = await user_service.get_by_cpf(user.cpf)
    except ValueError:
        existing_user = None

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this CPF already exists",
        )

    user_entity = UserDomain(
        cpf=user.cpf,
        name=user.name,
        password=user.password,
    )
    created_user = await user_service.create(user_entity)
    return UserResponse.from_domain(created_user)


@router.get(
    "/users/me",
    summary="Get current authenticated user",
    description="Retrieve the profile of the currently authenticated user.",
    response_model=UserResponse,
    responses={401: {"description": "Unauthorized: invalid or missing token"}},
)
async def read_users_me(
    current_user: UserDomain = Depends(get_current_user),
):
    """This endpoint retrieves the current authenticated user."""

    return UserResponse.from_domain(current_user)
