from src.app.db.database import engine, Base
from src.app.models import user  # noqa


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
