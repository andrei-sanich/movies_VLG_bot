def get_info(user_sets, info):
    
    result = []
    for x, y, z in [(x, y['genres'], z) for x in user_sets for y in info for z in info]:
        if set(x).issubset(set(y)) and y == z['genres']:
            info = ("{}\n{}\n "
            "{}\n"
            "режиссер(ы): {}\n"
            "сценарист(ы): {}\n"
            "произведено в: {}\n"
            "премьера в РФ: {} ".format(
                        z['name_rus'],
                        z['name_eng'],
                        ', '.join(z['genres']),
                        ', '.join(z['directors']),
                        ', '.join(z['writers']),
                        ', '.join(z['countries']),
                        z['rus_prem']                                                   
                                          )
          )
            result.append(info)                     
    return set(result)