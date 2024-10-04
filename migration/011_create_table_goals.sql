-- Table: public.goals

-- DROP TABLE IF EXISTS public.goals;

create table if not exists public.goals
(
    id serial not null,
    description text COLLATE pg_catalog."default" not null,
    start_date timestamp without time zone not null,
    conclusion_date timestamp without time zone not null,
    end_date timestamp without time zone not null,
    employee_id bigint not null,
    created_at timestamp with time zone default now(),
    updated_at timestamp with time zone,
    constraint goals_pkey primary key (id),
    constraint goals_employee_id_fkey foreign key (employee_id)
        references public.employee (id) match simple
        on update no action
        on delete no action
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.goals
    OWNER to postgres;