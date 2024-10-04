-- Table: public.employee

-- DROP TABLE IF EXISTS public.employee;

CREATE TABLE IF NOT EXISTS public.employee
(
    id integer NOT NULL DEFAULT nextval('employee_id_seq'::regclass),
    user_id bigint NOT NULL,
    position_at_work position_at_work NOT NULL,
    nuit bigint NOT NULL,
    identity_card_bi character varying(255) COLLATE pg_catalog."default" NOT NULL,
    salary double precision NOT NULL DEFAULT 0,
    date_admission timestamp without time zone NOT NULL,
    department_id bigint NOT NULL,
    academic_level character varying(255) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT employee_pkey PRIMARY KEY (id),
    CONSTRAINT employee_department_id_fkey FOREIGN KEY (department_id)
        REFERENCES public.department (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT employee_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public."user" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.employee
    OWNER to postgres;