-- Table: public.department

-- DROP TABLE IF EXISTS public.department;

CREATE TABLE IF NOT EXISTS public.department
(
    id integer NOT NULL DEFAULT nextval('department_id_seq'::regclass),
    name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    employee_nums bigint NOT NULL DEFAULT 0,
    min_salary double precision NOT NULL DEFAULT 0,
    max_salary double precision NOT NULL DEFAULT 0,
    CONSTRAINT department_pkey PRIMARY KEY (id),
    CONSTRAINT department_name_key UNIQUE (name)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.department
    OWNER to postgres;