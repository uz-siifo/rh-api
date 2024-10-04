-- Table: public.goals

-- DROP TABLE IF EXISTS public.goals;

CREATE TABLE IF NOT EXISTS public.goals
(
    id integer NOT NULL DEFAULT nextval('goals_id_seq'::regclass),
    description text COLLATE pg_catalog."default" NOT NULL,
    start_date timestamp without time zone NOT NULL,
    conclusion_date timestamp without time zone NOT NULL,
    end_date timestamp without time zone NOT NULL,
    employee_id bigint NOT NULL,
    CONSTRAINT goals_pkey PRIMARY KEY (id),
    CONSTRAINT goals_employee_id_fkey FOREIGN KEY (employee_id)
        REFERENCES public.employee (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.goals
    OWNER to postgres;