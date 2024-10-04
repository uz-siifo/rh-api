-- Table: public.presences

-- DROP TABLE IF EXISTS public.presences;

create table if not exists public.presences
(
    id serial not null,
    employee_id bigint not null,
    month_records_id bigint not null,
    created_at timestamp with time zone default now(),
    updated_at timestamp with time zone,
    constraint presences_pkey primary key (id),
    constraint presences_employee_id_fkey foreign key (employee_id)
        references public.employee (id) match simple
        on update no action
        on delete no action,
    constraint presences_month_records_id_fkey foreign key (month_records_id)
        references public.month_records (id) match simple
        on update no action
        on delete no action
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.presences
    OWNER to postgres;