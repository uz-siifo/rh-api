-- Table: public.employee

-- DROP TABLE IF EXISTS public.employee;

create table if not exists public.employee
(
    id serial not null nextval('employee_id_seq'::regclass),
    position_at_work position_at_work_enum not null,
    nuit bigint not null,
    identity_card_bi character varying(255) COLLATE pg_catalog."default" not null,
    salary double precision not null default 0,
    date_admission timestamp without time zone not null,
    department_id bigint not null,
    academic_level character varying(255) COLLATE pg_catalog."default" not null,
    created_at timestamp with time zone default now(),
    updated_at timestamp with time zone,
    constraint employee_pkey primary key (id),
    constraint employee_department_id_fkey foreign key (department_id)
        references public.department (id) match simple
        on update no action
        on delete no action
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.employee
    OWNER to postgres;