from src.fortnite import get_squad_stats, build_string_for_squad_stats

username = '' # Here your username.
platform = '' # Here your platform: psn, xbox, pc.

squad_data = get_squad_stats(username, platform)[0]
print(build_string_for_squad_stats(squad_data))
