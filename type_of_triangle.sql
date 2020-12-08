SELECT CASE
    WHEN A+B > C THEN ( CASE
        WHEN A = B THEN ( CASE 
            WHEN B != C THEN 'Isosceles'
            ELSE 'Equilateral'
            END )
        ELSE ( CASE
            WHEN A = C THEN 'Isosceles'
            ELSE 'Scalene'
            END )
        END
        )
    ELSE 'Not A Triangle'
    END
    FROM TRIANGLES;