from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class UrlsModel(Base):
    __tablename__ = 'urls'

    id: Mapped[int] = mapped_column(primary_key=True)
    full_urls: Mapped[str] = mapped_column(unique=True)
    short_urls: Mapped[str] = mapped_column(unique=True)
