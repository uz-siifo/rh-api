-- Table: public.user_employee

-- DROP TABLE IF EXISTS public.user_employee;

create table if not exists public.user_employee
(
    id serial not null,
    user_id bigint not null,
    employee_id bigint not null,
    created_at timestamp with time zone not null default now(),
    updated_at timestamp without time zone,
    constraint user_employee_pkey primary key (id),
    constraint user_employee_user_id_employee_id_key UNIQUE (user_id, employee_id),
    constraint user_employee_employee_id_fkey foreign key (employee_id)
        references public.employee (id) match simple
        on update no action
        on delete no action,
    constraint user_employee_user_id_fkey foreign key (user_id)
        references public."user" (id) match simple
        on update no action
        on delete no action
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.user_employee
    OWNER to postgres;