-- Write your PostgreSQL query statement below
SELECT score,
Dense_RANK() OVER( ORDER BY score desc)as rank
from Scores