def format_time(seconds):
    seconds = int(seconds)
    minutes = seconds // 60
    seconds = seconds % 60
    if minutes == 0:
        return f"{seconds} сек"
    return f"{minutes} мин {seconds} сек"

