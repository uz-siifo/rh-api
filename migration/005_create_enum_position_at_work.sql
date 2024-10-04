-- Type: position_at_work

-- DROP TYPE IF EXISTS public.position_at_work_enum;

CREATE TYPE public.position_at_work_enum AS ENUM
    ('technical', 'enginneer', 'secretary', 'other');

ALTER TYPE public.position_at_work_enum
    OWNER TO postgres;
