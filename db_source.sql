create database if not exists padaria;
use padaria;

create table if not exists products(
    id int(5) not null auto_increment,
    _name varchar(100) not null,
    price float not null,
    amount int not null,
    
    constraint pk_products primary key(id)
);