-- Table: public.performance_evaluation

-- DROP TABLE IF EXISTS public.performance_evaluation;

CREATE TABLE IF NOT EXISTS public.performance_evaluation
(
    id integer NOT NULL DEFAULT nextval('performance_evaluation_id_seq'::regclass),
    employee_id bigint NOT NULL,
    employee_rating_id bigint NOT NULL,
    employee_goals_id bigint NOT NULL,
    feedback feedback NOT NULL,
    CONSTRAINT performance_evaluation_pkey PRIMARY KEY (id),
    CONSTRAINT performance_evaluation_employee_goals_id_fkey FOREIGN KEY (employee_goals_id)
        REFERENCES public.goals (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT performance_evaluation_employee_id_fkey FOREIGN KEY (employee_id)
        REFERENCES public.employee (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT performance_evaluation_employee_rating_id_fkey FOREIGN KEY (employee_rating_id)
        REFERENCES public.employee_rating (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.performance_evaluation
    OWNER to postgres;