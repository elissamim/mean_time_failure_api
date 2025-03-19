from datetime import datetime, timedelta
import random

def random_timestamp(start : datetime,
                     end: datetime) -> datetime:
    """
    Generate a random timestamp between two datetime objects.

    Args:
        start (datetime): Start datetime.
        end (datetime): End datetime.
        
    Returns:
        datetime: A random datetime between start and end
    """
    delta = end - start
    random_seconds = random.uniform(0, delta.total_seconds())
    random_time = start + timedelta(seconds=random_seconds)
    return random_time.strftime("%Y-%m-%d %H-%M-%S")