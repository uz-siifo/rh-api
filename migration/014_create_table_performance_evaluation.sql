-- Table: public.performance_evaluation

-- DROP TABLE IF EXISTS public.performance_evaluation;

create table if not exists public.performance_evaluation
(
    id serial not null,
    employee_id bigint not null,
    employee_rating_id bigint not null,
    employee_goals_id bigint not null,
    feedback feedback_enum not null,
    created_at timestamp with time zone default now(),
    updated_at timestamp with time zone,
    constraint performance_evaluation_pkey primary key (id),
    constraint performance_evaluation_employee_goals_id_fkey foreign key (employee_goals_id)
        references public.goals (id) match simple
        on update no action
        on delete no action,
    constraint performance_evaluation_employee_id_fkey foreign key (employee_id)
        references public.employee (id) match simple
        on update no action
        on delete no action,
    constraint performance_evaluation_employee_rating_id_fkey foreign key (employee_rating_id)
        references public.employee_rating (id) match simple
        on update no action
        on delete no action
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.performance_evaluation
    OWNER to postgres;