-- Table: public.user_contact

-- DROP TABLE IF EXISTS public.user_contact;

CREATE TABLE IF NOT EXISTS public.user_contact
(
    id integer NOT NULL DEFAULT nextval('user_contact_id_seq'::regclass),
    user_id bigint NOT NULL,
    contact character varying(255) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT user_contact_pkey PRIMARY KEY (id),
    CONSTRAINT user_contact_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public."user" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.user_contact
    OWNER to postgres;