import random
import json
import time


def get_lat():
    return 37.4253498 + ((random.random() - 0.5) * 0.01 * (1/0.7))

def get_lng():
    return -122.0765002 + ((random.random() - 0.5) * 0.01 * (1/0.7))


def get_all():
    pokemon_docs = [
        """Speaking of cute things that come bundled with heartbreaking tragedy, we have Spoink, who appears to have been scientifically designed to have an Adorability Index of over 3,000 kilobuttons.""",
        """Right about here is where things start to get weird, and yes: I say that knowing full well that I just discussed a psychic pig that bounces on a spring made from its tail to keep from going into cardiac arrest.""",
    ]

    ret = []
    # add pokemon
    for i in xrange(10, 20+1):
        m = {}
        # m['id'] = i
        m['msg_type'] = 'pokemon'
        m['title'] = 'Pokemon %d' % i
        m['doc'] = random.choice(pokemon_docs)
        m['url'] = 'https://raw.githubusercontent.com/LeoHung/linkedin_hack/master/pseudo_api/img/%d.png' %(i)
        m['img_url'] = 'https://raw.githubusercontent.com/LeoHung/linkedin_hack/master/pseudo_api/img/%d.png' %(i)
        m['start_time'] = time.time()
        m['end_time'] = time.time() + 100000000
        m['category'] = 'pokemon'
        m['lat'] = get_lat()
        m['lng'] = get_lng()
        if i > 15:
            m['lock'] = True
            m['unlock_type'] = 'upload_pic'
        else:
            m['lock'] = False
            m['unlock_type'] = None
        ret.append(m)

    # add linkedin hr_contact
    hr_m = {}
    hr_m['msg_type'] = 'hr_contact'
    hr_m['title'] = 'LinkedIn is Here!'
    hr_m['doc'] = 'LinkedIn is hiring!'
    hr_m['url'] ='https://www.linkedin.com/profile/view?id=22330283'
    hr_m['img_url'] = 'https://media.licdn.com/media/p/6/005/07c/31e/153cdd3.jpg'
    hr_m['start_time'] = time.time()
    hr_m['end_time'] = time.time() + 100000000
    hr_m['category'] = 'hr'
    hr_m['lat'] = 37.4233439
    hr_m['lng'] = -122.0706904
    hr_m['lock'] = False
    hr_m['unlock_type'] = None
    ret.append(hr_m)

    # add National Geoagraphy hr_contact
    hr_2_m = {}
    hr_2_m['msg_type'] = 'hr_contact'
    hr_2_m['title'] = 'National Geographic is HERE!'
    hr_2_m['doc'] = 'National Geographic is hiring. Linkedin me!'
    hr_2_m['url'] = 'https://www.linkedin.com/company/national-geographic-society?trk=company_logo'
    hr_2_m['img_url'] = 'https://media.licdn.com/media/p/2/000/023/1f4/15aab3b.png'
    hr_2_m['start_time'] = time.time()
    hr_2_m['end_time'] = time.time() + 100000000
    hr_2_m['category'] = 'hr'
    hr_2_m['lat'] = 37.4584803
    hr_2_m['lng'] = -122.130129
    hr_2_m['lock'] = False
    hr_2_m['unlock_type'] = None
    ret.append(hr_2_m)

    # add match_day
    match_m = {}
    match_m['msg_type'] = 'match_day'
    match_m['title'] = 'Giant GO GO!'
    match_m['doc'] = 'Giant so awesome! Join us!'
    match_m['url'] = 'https://www.youtube.com/watch?v=C4wRgE7njjU'
    match_m['img_url'] = 'http://sanfrancisco.giants.mlb.com/mlb/images/team_logos/social_media/og_1200x630_image/sf_1200x630.jpg'
    match_m['start_time'] = time.time()
    match_m['end_time'] = time.time() + 100000000
    match_m['category'] = 'match_day'
    match_m['lat'] = 37.4247649
    match_m['lng'] = -122.0781952
    match_m['lock'] = False
    match_m['unlock_type'] = None
    ret.append(match_m)

    # add spam
    spam_m = {}
    spam_m['msg_type'] = 'spam'
    spam_m['title'] = 'Come to Starbucks!'
    spam_m['doc'] = ' Buy 1 get 1 free!'
    spam_m['url'] = 'http://www.starbucks.com/menu'
    spam_m['img_url'] = 'https://pbs.twimg.com/profile_images/553626039570530304/C1WMCw87.png'
    spam_m['start_time'] = time.time()
    spam_m['end_time'] = time.time() + 100000000
    spam_m['category'] = 'match_day'
    spam_m['lat'] = 37.416000
    spam_m['lng'] = -122.07713
    spam_m['lock'] = False
    spam_m['unlock_type'] = None
    ret.append(spam_m)

    return ret

def gen_search_js(filename):
    all_pokemon = get_all()
    outf = open(filename, "w")
    print >> outf, json.dumps(all_pokemon, indent=2)
    outf.close()

def gen_message(dir_path):
    all_pokemon = get_all()
    for pokemon in all_pokemon:
        filename = "%s/%d" % (dir_path, pokemon['mid'])
        outf = open(filename, "w")
        print >> outf, json.dumps(pokemon, indent=2)
        outf.close()