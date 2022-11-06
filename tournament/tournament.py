def tally(rows):
    table = [f"{'Team':<31}| MP |  W |  D |  L |  P"]
    if not rows:
        return table
    
    db = {}
    for row in rows:
        team_1, team_2, match_result = row.split(';')
        for team in [team_1, team_2]:
            if not team in db:
                db[team] = {k:0 for k in ['MP', 'W', 'D', 'L', 'P']}
        # matches played
        db[team_1]['MP'] += 1
        db[team_2]['MP'] += 1
        # matches won/drawn/lost + points
        if match_result == 'win':
            db[team_1]['W'] += 1
            db[team_2]['L'] += 1
            db[team_1]['P'] += 3
        if match_result == 'draw':
            db[team_1]['D'] += 1
            db[team_2]['D'] += 1
            db[team_1]['P'] += 1
            db[team_2]['P'] += 1
        if match_result == 'loss':
            db[team_1]['L'] += 1
            db[team_2]['W'] += 1
            db[team_2]['P'] += 3

    db = dict(sorted(db.items())) # sort dict by key
    teams_sorted = sorted(db, key=lambda x: db[x]['P'], reverse=True)

    for team in teams_sorted:
        nums = list(db[team].values()) # mp, w, d, l, p
        mp, w, d, l, p = [f'{n:>2}' for n in nums]
        
        table += [f"{team:<31}| {mp} | {w} | {d} | {l} | {p}"]

    return table
