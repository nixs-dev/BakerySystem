create database if not exists bakery DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

use bakery;

create table if not exists products(
    id int(5) not null auto_increment,
    _name varchar(100) not null,
    price float not null,
    amount int not null,
    
    constraint pk_products primary key(id)
) DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

create table if not exists clients (
    cpf bigint(11) not null,
    _name varchar(100) not null,
    birthdate date not null,
    email varchar(100) not null,
    p_phone bigint(12) not null,
    s_phone bigint(12) null,
    
    cep int(8) not null,
    city varchar(30) not null,
    district varchar(20) not null,
    street varchar(70) not null,
    num int(3) not null,
    password varchar(30) not null,
    
    constraint pk_clients primary key (cpf)
) DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

create table if not exists deliveries (
    id int(10) not null auto_increment,
    cpf_client bigint(11) not null,
    id_product int(5) not null,
    amount int not null,
    final_price float not null,
    
    city varchar(30) not null,
    district varchar(20) not null,
    street varchar(70) not null,
    num int(3) not null,
    
    start_datetime datetime not null,
    end_datetime datetime,
    done bit default 0,
    
    constraint pk_deliveries primary key (id),
    constraint fk_deliveries_clients foreign key (cpf_client) references clients (cpf),
    constraint fk_deliveries_products foreign key (id_product) references products (id)
) DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;