CREATE TABLE fabricante(
	idFabricante integer primary key autoincrement,
	marca text not null,
	site text not null,
	telefone text not null,
	UF text not null
);
CREATE TABLE produto(
	id_produto integer primary key autoincrement,
	nome text not null,
	valorCompra float not null,
	valorVenda float not null,
	valorLucra float not null,
	percentualLucro integer not null,
	idFabricante  integer not null,
	foreign key (idFabricante) references fabricante(idFabricante)
);

INSERT INTO fabricante(marca, site, telefone, UF) VALUES 
	('Xiaomi','Xiaomi.com','(61)96199-9916','DF'),
	('SONY','Sony.com','(11)97793-9459','SP'),
	('Apple','Apple.com','(21)87459-9899','RJ'),
	('Microsoft','Microsoft.com','(84)99884-9945','RN'),
	('Samsung','Samsung.com','(62)99629-9978','GO'),
	('nintendo','nintendo.com','(63)93699-9639','TO'),
	('panasonic','panasonic.com','(83)97899-9569','CE'),
	('Canon','canon.com','(27)99779-9258','ES'),
	('nikon','nikon.com','(31)98799-9319','MG'),
	('JBL','jbl.com','(14)98299-9149','SP')

;

INSERT INTO produto(nome, valorCompra,valorVenda,valorLucra,percentualLucro,idFabricante) VALUES 
	('Redmi A1',1000,1200,200,20,1),
	('Redmi Note 11',2000,3000,1000,50,1),
	('Playstation 5',2500,5000,2500,100,2),
	('Playstation 4',1500,3000,1500,100,2)
	('iPhone 14',4000,8000,4000,100,3),
	('iPhone 14 Pro Max',5000,10000,5000,100,3),
	('Xbox Series S',1000,2000,1000,100,4),
	('Xbox Series X',2500,7500,5000,200,4),
	('Galaxy S20 ULTRA',1500,4500,3000,200,5),
	('Galaxy S23 ',3000,7500,4500,150,5),
	('Nintendo Switch',700,2100,1400,200,6),
	('Nintendo Switch Lite',600,1200,600,100,6),
	('home theater',1000,1500,500,50,7),
	('LUMIX',3500,7000,3500,100,7),
	('Filme fotografico',100,300,200,200,8),
	('EOS REBEL',2000,3500,1500,75,8),
	('NIKON Z7',20000,57000,37000,185,9),
	('NIKON MEMORY CARD 256GB',125,250,125,100,9),
	('boombox 3',1700,2500,800,47,10),
	('fone sem fio',70,200,130,185,10),

;