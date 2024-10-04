-- Table: public.working_hours

-- DROP TABLE IF EXISTS public.working_hours;

create table if not exists public.working_hours
(
    id serial not null,
    normal_hours integer not null default 0,
    overtime integer not null default 0,
    employee_id bigint not null,
    created_at time without time zone default now(),
    updated_at timestamp with time zone,
    constraint working_hours_pkey primary key (id),
    constraint working_hours_employee_id_fkey foreign key (employee_id)
        references public.employee (id) match simple
        on update no action
        on delete no action
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.working_hours
    OWNER to postgres;