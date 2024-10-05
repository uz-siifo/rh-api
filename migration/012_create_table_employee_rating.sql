create table if not exists public.employee_rating
(
    id serial not null,
    is_assiduous boolean not null default false,
    is_collaborative boolean not null default false,
    completed_goals integer not null default 0,
    is_punctual boolean not null default false,
    work_quality_rating integer not null default 0,
    problem_solving_skills_rating integer not null default 0,
    communication_skills_rating integer not null default 0,
    time_management_skills_rating integer not null default 0,
    leadership_skills_rating integer not null default 0,
    employee_id bigint not null,
    created_at timestamp with time zone default now(),
    updated_at timestamp with time zone,
    constraint employee_rating_pkey primary key (id),
    constraint employee_rating_employee_id_fkey foreign key (employee_id)
        references public.employee (id) match simple
        on update no action
        on delete no action
)
