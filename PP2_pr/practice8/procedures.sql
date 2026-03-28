-- 1. Upsert: Insert or Update if exists (Task 2)
CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name VARCHAR,
    p_surname VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE first_name = p_name AND last_name = p_surname) THEN
        UPDATE contacts SET phone_number = p_phone 
        WHERE first_name = p_name AND last_name = p_surname;
    ELSE
        INSERT INTO contacts (first_name, last_name, phone_number) 
        VALUES (p_name, p_surname, p_phone);
    END IF;
END;
$$;

-- 2. Bulk Insert with validation (Task 3)
-- This procedure takes arrays of data and checks if the phone is 11 digits
CREATE OR REPLACE PROCEDURE bulk_insert_contacts(
    p_names VARCHAR[],
    p_surnames VARCHAR[],
    p_phones VARCHAR[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INTEGER;
BEGIN
    FOR i IN 1..array_length(p_names, 1) LOOP
        -- Simple validation: check if phone length is exactly 11
        IF length(p_phones[i]) = 11 THEN
            INSERT INTO contacts (first_name, last_name, phone_number)
            VALUES (p_names[i], p_surnames[i], p_phones[i]);
        ELSE
            RAISE NOTICE 'Invalid phone for %: %', p_names[i], p_phones[i];
        END IF;
    END LOOP;
END;
$$;

-- 3. Delete by name or phone (Task 5)
CREATE OR REPLACE PROCEDURE delete_contact(p_search VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts 
    WHERE first_name = p_search OR phone_number = p_search;
END;
$$;