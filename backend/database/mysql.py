from contextlib import asynccontextmanager
from sqlalchemy.schema import CreateTable, DropTable
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from database.gen_fakeDB import GenFakeDB
from database.init_db import FakeDB
from models.user import User

engine = create_async_engine(
    url="mysql+aiomysql://root:password@localhost:8888/test_database",
    echo=True,
    pool_pre_ping=True
)
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False, autocommit=False)
gen_fake_db = GenFakeDB()

@asynccontextmanager
async def get_db():
    async with SessionLocal() as db:
        async with db.begin():
            yield db


async def init_db():
    async with SessionLocal() as db:
        # gen_fake_db.generate()
        gen_fake_db.generate()

        async with db.begin():
            # Create tables
            await db.execute(CreateTable(User.__table__, if_not_exists=True))
            await FakeDB().create_entity_list(db)


async def close_db():
    async with SessionLocal() as db:
        async with db.begin():
            # Drop tables
            await db.execute(DropTable(User.__table__))
    await engine.dispose()


def db_session_decorator(func):
    async def wrapper(*args, **kwargs):
        async with get_db() as db_session:
            kwargs["db_session"] = db_session
            result = await func(*args, **kwargs)
            return result
        
    return wrapper


def crud_class_decorator(cls):
    for name, method in cls.__dict__.items():
        if callable(method):
            setattr(cls, name, db_session_decorator(method))

    return cls