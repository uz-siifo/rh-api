-- Type: position_at_work

-- DROP TYPE IF EXISTS public.position_at_work;

CREATE TYPE public.position_at_work AS ENUM
    ('technical', 'enginneer', 'secretary', 'other');

ALTER TYPE public.position_at_work
    OWNER TO postgres;
