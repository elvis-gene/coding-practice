# Write your MySQL query statement below
# Write a SQL query to find all duplicate emails in a table named Person.
# +----+---------+
# | Id | Email   |
# +----+---------+
# | 1  | a@b.com |
# | 2  | c@d.com |
# | 3  | a@b.com |
# +----+---------+

# For example, your query should return the following for the above table:

# +---------+
# | Email   |
# +---------+
# | a@b.com |
# +---------+
# Note: All emails are in lowercase.

SELECT P1.Email from Person as P1 JOIN Person as P2 WHERE P1.Email = P2.Email AND P1.Id <> P2.Id GROUP BY P1.Email;

# Another solution
select Email
from Person
group by Email
having count(Email) > 1;
