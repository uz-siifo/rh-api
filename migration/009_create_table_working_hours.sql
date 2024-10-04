-- Table: public.working_hours

-- DROP TABLE IF EXISTS public.working_hours;

CREATE TABLE IF NOT EXISTS public.working_hours
(
    id integer NOT NULL DEFAULT nextval('working_hours_id_seq'::regclass),
    normal_hours integer NOT NULL DEFAULT 0,
    overtime integer NOT NULL DEFAULT 0,
    employee_id bigint NOT NULL,
    CONSTRAINT working_hours_pkey PRIMARY KEY (id),
    CONSTRAINT working_hours_employee_id_fkey FOREIGN KEY (employee_id)
        REFERENCES public.employee (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.working_hours
    OWNER to postgres;