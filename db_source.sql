create database if not exists bakery DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

use bakery;

create table if not exists products(
    id int(5) not null auto_increment,
    _name varchar(100) not null,
    price float not null,
    amount int unsigned not null,
    photo longblob null,
    
    constraint pk_products primary key(id)
) DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

create table if not exists clients (
    cpf varchar(11) not null,
    _name varchar(100) not null,
    birthdate date not null,
    email varchar(100) not null,
    p_phone bigint(12) not null,
    s_phone bigint(12) null,
    photo longblob null,
    
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
    cpf_client varchar(11) not null,
    id_product int(5) not null,
    product_name varchar(100) not null,
    amount int unsigned not null,
    final_price float not null,
    
    city varchar(30) not null,
    district varchar(20) not null,
    street varchar(70) not null,
    num int(3) not null,
    
    start_datetime datetime not null,
    end_datetime datetime,
    done bit default 0,
    
    constraint pk_deliveries primary key (id),
    constraint fk_deliveries_clients foreign key (cpf_client) references clients (cpf) on delete cascade on update cascade,
    constraint fk_deliveries_products foreign key (id_product) references products (id) on delete cascade on update cascade
) DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

create table if not exists settings (
    cpf_client varchar(11) NOT null,
    notifications bit default 1,
    
    constraint fk_settings_clients foreign key (cpf_client) references clients (cpf) on delete cascade on update cascade
) DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

create table if not exists security (
    cpf_client varchar(11) NOT null,
    salt binary(32) not null,
    
    unique (salt),
    constraint fk_security_clients foreign key (cpf_client) references clients (cpf) on delete cascade on update cascade
) DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

create table if not exists notifications (
    id int(5) not null auto_increment,
    cpf_client varchar(11) NOT null,
    text varchar(200),
    received bit default 0,
    timestamp datetime not null,
    
    constraint pk_notifications primary key(id),
    constraint fk_notifications_clients foreign key (cpf_client) references clients (cpf) on delete cascade on update cascade
) DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;


DELIMITER //

CREATE TRIGGER delivery_finished
AFTER UPDATE ON deliveries
FOR EACH ROW
BEGIN
  SET @DONE = INSERTED.done;
  SET @CPF = INSERTED.cpf_client;

  IF @DONE = 1 THEN
    INSERT INTO notifications (cpf_client, text, timestamp) VALUES (@CPF, "Produto entregue", NOW());
  END IF;
END//


CREATE TRIGGER delivery_canceled
AFTER DELETE ON deliveries
FOR EACH ROW
BEGIN
  SET @PRODUCT = DELETED.id_product;
  SET @AMOUNT = DELETED.amount;
  SET @CPF = DELETED.cpf_client;
  
  UPDATE products SET amount = amount + @AMOUNT WHERE id = @PRODUCT;
  
  INSERT INTO notifications (cpf_client, text, timestamp) VALUES (@CPF, "Pedido rejeitado", NOW());
END//

DELIMITER ;