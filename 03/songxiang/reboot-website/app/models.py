#!/usr/bin/env python
# coding:utf-8
from app import db

class Idc(db.Model):
    __tablename__        = "idc"
    id                   = db.Column(db.Integer, primary_key = True)
    name                 = db.Column(db.String(50), index = True, nullable = False, unique = True)
    idc_name             = db.Column(db.String(50), nullable=False)
    address              = db.Column(db.String(255), nullable=False)
    phone                = db.Column(db.String(20), nullable=False)
    email                = db.Column(db.String(50), nullable=False)
    user_interface       = db.Column(db.String(50), nullable=False)
    user_phone           = db.Column(db.String(20), nullable=False)
    rel_cabinet_num      = db.Column(db.Integer, nullable=False)
    pact_cabinet_num     = db.Column(db.Integer, nullable=False)

class Cabinet(db.Model):
    __tablename__        = "cabinet"
    id                   = db.Column(db.Integer, primary_key = True)
    name                 = db.Column(db.String(30), nullable = False, unique = True)
    idc_id               = db.Column(db.Integer, nullable=False)
    power                = db.Column(db.String(20))


class Manufactures(db.Model):
    __tablename__        = "manufactures"
    id                   = db.Column(db.Integer, primary_key = True)
    name                 = db.Column(db.String(50), nullable = False, unique = True)


class Supplier(db.Model):
    __tablename__        = "supplier"
    id                   = db.Column(db.Integer, primary_key = True)
    name                 = db.Column(db.String(100),nullable = False, unique = True)

class Servertype(db.Model):
    __tablename__        = "Servertype"
    id                   = db.Column(db.Integer, primary_key = True)
    type                 = db.Column(db.String(20),nullable = False, unique = True)
    manufacturers_id                 = db.Column(db.Integer,nullable = False, unique = True, index = True)

class Raid(db.Model):
    __tablename__        = "raid"
    id                   = db.Column(db.Integer, primary_key = True)
    name                 = db.Column(db.String(20),nullable = False, unique = True)

class Raidtype(db.Model):
    __tablename__        = "raidtype"
    id                   = db.Column(db.Integer, primary_key = True)
    name                 = db.Column(db.String(50),nullable = False, unique = True)

class Status(db.Model):
    __tablename__        = "raidtype"
    id                   = db.Column(db.Integer, primary_key = True)
    name                 = db.Column(db.String(20),nullable = False, unique = True)
# class Product(db.Model):
#     __tablename__        = "product"
#     id                   = db.Column(db.Integer, primary_key = True)
#     name                 = db.Column(db.String(50),nullable = False, unique = True)
#     name                 = db.Column(db.String(50), nullable=False, unique=True)
#     name                 = db.Column(db.String(50), nullable=False, unique=True)
#     name                 = db.Column(db.String(50), nullable=False, unique=True)

