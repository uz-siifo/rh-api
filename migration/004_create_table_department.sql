-- Table: public.department

-- DROP TABLE IF EXISTS public.department;

create table if not exists public.department
(
    id serial not null
    name character varying(255) COLLATE pg_catalog."default" not null,
    employee_nums bigint not null default 0,
    min_salary double precision not null default 0,
    max_salary double precision not null default 0,
    created_at timestamp with time zone not null default now(),
    updated_at timestamp without time zone not null default now(),
    constraint department_pkey primary key (id),
    constraint department_name_key UNIQUE (name)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.department
    OWNER to postgres;