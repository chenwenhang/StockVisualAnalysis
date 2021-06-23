create table stock
(
    id                      int auto_increment
        primary key,
    name                    varchar(10) not null,
    industry                varchar(10) not null,
    price                   float       null,
    marcket_value           int         null,
    rise_and_fall           float       null,
    turnover                float       null,
    region                  varchar(10) null,
    quantity_relative_ratio float       null,
    amplitude               float       null
);

