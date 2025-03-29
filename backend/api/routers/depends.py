from fastapi import HTTPException

from crud.user import UserCrudManager

UserCrud = UserCrudManager()


# Check if the user exists
async def check_user_id(uid: str):
    user = await UserCrud.get(uid)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")

    return user.uid
