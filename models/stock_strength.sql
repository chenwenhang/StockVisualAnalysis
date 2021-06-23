create table strength
(
    id       int auto_increment
        primary key,
    count    int       default 0                 not null,
    grade    float     default 0                 not null,
    date     timestamp default CURRENT_TIMESTAMP not null,
    industry varchar(10)                         null
);
