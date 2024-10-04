-- Table: public.user_contact

-- DROP TABLE IF EXISTS public.user_contact;

create table if not exists public.user_contact
(
    id serial not null,
    user_id bigint not null,
    contact character varying(255) COLLATE pg_catalog."default" not null,
    created_at timestamp with time zone default now(),
    updated_at timestamp with time zone,
    constraint user_contact_pkey primary key (id),
    constraint user_contact_user_id_fkey foreign key (user_id)
        references public."user" (id) match simple
        on update no action
        on delete no action
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.user_contact
    OWNER to postgres;