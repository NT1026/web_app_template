from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.mysql import crud_class_decorator
from models.user import User as UserModel


@crud_class_decorator
class AuthCrudManager:
    async def user_login(self, uid: str, db_session: AsyncSession):
        stmt = select(UserModel.uid, UserModel.password, UserModel.name).where(
            UserModel.uid == uid
        )
        result = await db_session.execute(stmt)
        user = result.first()

        return user if user else None
