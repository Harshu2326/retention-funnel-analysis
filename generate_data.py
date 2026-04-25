import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

# ---------------- USERS ----------------
users = []

for i in range(1000):
    users.append([
        i,
        fake.date_between(start_date='-60d', end_date='today'),
        random.choice(['ads', 'organic', 'referral'])
    ])

users_df = pd.DataFrame(users, columns=['user_id', 'signup_date', 'channel'])

# ---------------- EVENTS ----------------
event_types = [
    "signup", "login", "create_project",
    "invite_user", "upgrade_plan"
]

events = []

for i in range(5000):
    events.append([
        random.randint(0, 999),
        random.choice(event_types),
        fake.date_time_between(start_date='-60d', end_date='now')
    ])

events_df = pd.DataFrame(events, columns=['user_id', 'event_type', 'timestamp'])

# ---------------- SAVE FILES ----------------
import os
os.makedirs("data", exist_ok=True)

users_df.to_csv("data/users.csv", index=False)
events_df.to_csv("data/events.csv", index=False)

print("Dataset created successfully!")
