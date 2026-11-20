from __future__ import annotations

"""Consent-gated customer and assessment API with durable PostgreSQL records."""
import os
import secrets
from datetime import datetime, timezone
from uuid import uuid4
from typing import Optional
from fastapi import APIRouter, Depends, Header, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, String, DateTime, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./assessments-dev.db')
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False} if DATABASE_URL.startswith('sqlite') else {}, pool_pre_ping=True)
SessionLocal = sessionmaker(engine)

class Base(DeclarativeBase):
    pass

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(String(36), primary_key=True)
    name = Column(String(200), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False)

class Assessment(Base):
    __tablename__ = 'assessments'
    id = Column(String(36), primary_key=True)
    customer_id = Column(String(36), ForeignKey('customers.id'), nullable=False)
    module = Column(String(32), nullable=False)
    scope = Column(String(1000), nullable=False)
    authorization_reference = Column(String(300), nullable=False)
    status = Column(String(24), nullable=False, default='draft')
    created_at = Column(DateTime(timezone=True), nullable=False)

class CustomerIn(BaseModel):
    name: str = Field(min_length=1, max_length=200)

class AssessmentIn(BaseModel):
    customer_id: str
    module: str
    scope: str = Field(min_length=5, max_length=1000)
    authorization_reference: str = Field(min_length=3, max_length=300)

router = APIRouter(prefix='/api', tags=['operator'])

def authorize(x_operator_key: Optional[str] = Header(default=None)):
    key = os.getenv('OPERATOR_API_KEY', '')
    if not key or not x_operator_key or not secrets.compare_digest(key, x_operator_key):
        raise HTTPException(status_code=401, detail='Operator API key required')

def db():
    with SessionLocal() as session:
        yield session

def customer_out(c):
    return {'id': c.id, 'name': c.name, 'created_at': c.created_at.isoformat()}

def assessment_out(a):
    return {'id': a.id, 'customer_id': a.customer_id, 'module': a.module, 'scope': a.scope, 'authorization_reference': a.authorization_reference, 'status': a.status, 'created_at': a.created_at.isoformat()}

@router.post('/customers', status_code=201, dependencies=[Depends(authorize)])
def create_customer(data: CustomerIn, session: Session = Depends(db)):
    c = Customer(id=str(uuid4()), name=data.name.strip(), created_at=datetime.now(timezone.utc))
    session.add(c); session.commit()
    return customer_out(c)

@router.get('/customers', dependencies=[Depends(authorize)])
def list_customers(session: Session = Depends(db)):
    return {'customers': [customer_out(c) for c in session.scalars(select(Customer).order_by(Customer.created_at.desc()))]}

@router.post('/assessments', status_code=201, dependencies=[Depends(authorize)])
def create_assessment(data: AssessmentIn, session: Session = Depends(db)):
    if data.module not in {'time-leak', 'ai-visibility', 'lead-response'}:
        raise HTTPException(422, 'Unknown assessment module')
    if session.get(Customer, data.customer_id) is None:
        raise HTTPException(404, 'Customer not found')
    a = Assessment(id=str(uuid4()), customer_id=data.customer_id, module=data.module, scope=data.scope, authorization_reference=data.authorization_reference, status='draft', created_at=datetime.now(timezone.utc))
    session.add(a); session.commit()
    return assessment_out(a)

@router.get('/assessments', dependencies=[Depends(authorize)])
def list_assessments(session: Session = Depends(db)):
    return {'assessments': [assessment_out(a) for a in session.scalars(select(Assessment).order_by(Assessment.created_at.desc()))]}

@router.post('/assessments/{assessment_id}/close', dependencies=[Depends(authorize)])
def close_assessment(assessment_id: str, session: Session = Depends(db)):
    a = session.get(Assessment, assessment_id)
    if a is None:
        raise HTTPException(404, 'Assessment not found')
    a.status = 'closed'; session.commit()
    return assessment_out(a)
