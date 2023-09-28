from sqlalchemy import Column, create_engine, inspect, select, func
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

Base = declarative_base()


class Client(Base):

    __tablename__ = "client_account"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cpf = Column(String(9))
    address = Column(String(9))

    account = relationship(
        "Account", back_populates="client", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Client(id= {self.id}, name={self.name}, cpf={self.cpf}, Address={self.address}):"


class Account(Base):

    __tablename__ = "account"
    id = Column(Integer, primary_key=True)
    type = Column(String)
    agency = Column(String)
    num = Column(Integer)
    id_client = Column(Integer, ForeignKey("client_account.id"))

    client = relationship("Client", back_populates="account")

    def __repr__(self):
        return f"Address (id={self.id}, type={self.type}, agency={self.agency}, num={self.num})"


engine = create_engine("sqlite://")


Base.metadata.create_all(engine)


inspetor_engine = inspect(engine)

print(inspetor_engine.has_table("Account"))

