-- Type: access_level

-- DROP TYPE IF EXISTS public.access_level;

CREATE TYPE public.access_level AS ENUM
    ('admin', 'employee');

ALTER TYPE public.access_level
    OWNER TO postgres;
