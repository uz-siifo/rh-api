-- Type: feedback

-- DROP TYPE IF EXISTS public.feedback;

CREATE TYPE public.feedback AS ENUM
    ('bom', 'satisfatorio', 'nao satisfatorio', 'excelente', 'razoavel');

ALTER TYPE public.feedback
    OWNER TO postgres;
