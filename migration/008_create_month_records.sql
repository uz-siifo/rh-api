-- Table: public.month_records

-- DROP TABLE IF EXISTS public.month_records;

create table if not exists public.month_records
(
    id serial not null,
    month character varying(255) COLLATE pg_catalog."default" not null,
    year integer not null,
    presences integer not null default 0,
    absences integer not null default 0,
    created_at timestamp with time zone default now(),
    updated_at timestamp with time zone,
    constraint month_records_pkey primary key (id),
    constraint month_records_month_year_key UNIQUE (month, year)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.month_records
    OWNER to postgres;