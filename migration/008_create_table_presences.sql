-- Table: public.presences

-- DROP TABLE IF EXISTS public.presences;

CREATE TABLE IF NOT EXISTS public.presences
(
    id integer NOT NULL DEFAULT nextval('presences_id_seq'::regclass),
    employee_id bigint NOT NULL,
    month_records_id bigint NOT NULL,
    CONSTRAINT presences_pkey PRIMARY KEY (id),
    CONSTRAINT presences_employee_id_fkey FOREIGN KEY (employee_id)
        REFERENCES public.employee (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT presences_month_records_id_fkey FOREIGN KEY (month_records_id)
        REFERENCES public.month_records (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.presences
    OWNER to postgres;