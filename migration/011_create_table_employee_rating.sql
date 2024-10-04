-- Table: public.employee_rating

-- DROP TABLE IF EXISTS public.employee_rating;

CREATE TABLE IF NOT EXISTS public.employee_rating
(
    id integer NOT NULL DEFAULT nextval('employee_rating_id_seq'::regclass),
    is_assiduous boolean NOT NULL DEFAULT false,
    is_collaborative boolean NOT NULL DEFAULT false,
    -- more parameters...
    completed_goals integer NOT NULL DEFAULT 0,
    employee_id bigint NOT NULL,
    CONSTRAINT employee_rating_pkey PRIMARY KEY (id),
    CONSTRAINT employee_rating_employee_id_fkey FOREIGN KEY (employee_id)
        REFERENCES public.employee (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.employee_rating
    OWNER to postgres;