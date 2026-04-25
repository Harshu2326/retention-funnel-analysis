-- =========================
-- 1. FUNNEL ANALYSIS
-- =========================

SELECT event_type, COUNT(DISTINCT user_id) AS users
FROM events
GROUP BY event_type
ORDER BY users DESC;

-- =========================
-- 2. USER JOURNEY EVENTS
-- =========================

SELECT *
FROM events
WHERE event_type IN (
    'signup',
    'login',
    'create_project',
    'invite_user',
    'upgrade_plan'
);

-- =========================
-- 3. COHORT ANALYSIS
-- =========================

SELECT
    user_id,
    signup_date,
    DATE_TRUNC('week', signup_date) AS cohort_week
FROM users;
