import random
import json
def get_all():
    ret = []
    for i in xrange(10, 20+1):
        m = {}
        m['mid'] = i
        m['title'] = 'Pokemon %d' % i
        m['img_url'] = 'https://raw.githubusercontent.com/LeoHung/linkedin_hack/master/pseudo_api/img/%d.png' %(i)
        m['lat'] = 37.4253498 + (random.random() / 10.0)
        m['lng'] = -122.0765002 + (random.random() / 10.0)
        if i > 15:
            m['lock'] = True
            m['unlock_type'] = 'upload_pic'
        else:
            m['lock'] = False
            m['unlock_type'] = None
        m['category'] = 'pokemon'
        m['message_type'] = 'pokemon'
        m['desc'] = """Extremely we promotion remainder eagerness enjoyment an. Ham her demands removal brought minuter raising invited gay. Contented consisted continual curiosity contained get sex. Forth child dried in in aware do. You had met they song how feel lain evil near. Small she avoid six yet table china. And bed make say been then dine mrs. To household rapturous fulfilled attempted on so. """
        ret.append(m)
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
if __name__ == "__main__":
    gen_search_js("search.js")
    gen_message("message")
