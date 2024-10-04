-- Table: public.user

-- DROP TABLE IF EXISTS public."user";

create table if not exists public."user"
(
    id serial not null,
    name character varying(255) COLLATE pg_catalog."default" not null,
    nickname character varying(255) COLLATE pg_catalog."default" not null,
    email character varying(255) COLLATE pg_catalog."default" not null,
    passwd character varying(255) COLLATE pg_catalog."default" not null,
    access_level access_level_enum not null,
    created_at timestamp with time zone default now(),
    updated_at timestamp with time zone,
    constraint user_pkey primary key (id),
    constraint user_email_key UNIQUE (email)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."user"
    OWNER to postgres;