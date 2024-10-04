-- Table: public.month_records

-- DROP TABLE IF EXISTS public.month_records;

CREATE TABLE IF NOT EXISTS public.month_records
(
    id bigint NOT NULL DEFAULT nextval('month_records_id_seq'::regclass),
    month character varying(255) COLLATE pg_catalog."default" NOT NULL,
    year integer NOT NULL,
    presences integer NOT NULL DEFAULT 0,
    absences integer NOT NULL DEFAULT 0,
    CONSTRAINT month_records_pkey PRIMARY KEY (id),
    CONSTRAINT month_records_month_year_key UNIQUE (month, year)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.month_records
    OWNER to postgres;