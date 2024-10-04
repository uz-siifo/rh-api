-- Type: access_level

-- DROP TYPE IF EXISTS public.access_level_enum;

CREATE TYPE public.access_level_enum AS ENUM
    ('admin', 'employee');

ALTER TYPE public.access_level_enum
    OWNER TO postgres;
