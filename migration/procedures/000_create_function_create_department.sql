-- FUNCTION: public.create_department

-- DROP FUNCTION IF EXISTS public.create_department;

CREATE OR REPLACE FUNCTION public.create_department(
	__department jsonb)
    RETURNS TABLE(department_name character varying, employee_nums bigint, min_salary double precision, max_salary double precision, created_at timestamp with time zone) 
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
    ROWS 1000

AS $BODY$
DECLARE
    __id BIGINT;
BEGIN

    INSERT INTO department(name, employee_nums, min_salary, max_salary) 
    VALUES (
        (__department->>'name')::text, 
        (__department->>'employee_nums')::INTEGER,
        (__department->>'min_salary')::FLOAT,
        (__department->>'max_salary')::FLOAT
    ) RETURNING id INTO __id;

    RETURN QUERY 
    SELECT 
        d.name,               
        d.employee_nums,
        d.min_salary,
        d.max_salary,
        d.created_at 
    FROM 
        public.department d   
    WHERE 
        d.id = __id;
END;
$BODY$;

ALTER FUNCTION public.create_department(jsonb)
    OWNER TO postgres;
