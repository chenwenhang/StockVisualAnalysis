create table block
(
    id     int auto_increment
        primary key,
    code   int                                 not null,
    name   varchar(10)                         not null,
    RPS250 float                               null,
    RPS120 float                               null,
    RPS60  float                               null,
    RPS30  float                               null,
    RPS10  float                               null,
    date   timestamp default CURRENT_TIMESTAMP not null,
    grade  float                               null
);