from itertools import chain
import cdifflib
import random


def form_reply(message):
    phrases = {"greets": ["прив", "дарова", "хай"],
               "hau": ["че как", "как дела", "как жизнь", "что нового"]}
    replies = {"greets": ["привет", "здравствуй", ],
               "hau": ["вполне", "нормально", "хорошо", "замечательно"]}
    need_apply = {"greets": False,
                  "hau": False}
    output = list()
    for i in message.split():
        chances = list(map(lambda x: cdifflib.CSequenceMatcher(None, x, i).ratio(), list(chain.from_iterable(list(phrases.values())))))
        current_word = list(chain.from_iterable(list(phrases.values())))[chances.index(max(chances))]
        if current_word in phrases["greets"]:
            need_apply["greets"] = True
        elif current_word in phrases["hau"]:
            need_apply["hau"] = True

    if need_apply["greets"]:
        output.append(random.choice(replies["greets"]))
        need_apply["greets"] = False
    if need_apply["hau"]:
        output.append(random.choice(replies["hau"]))
        need_apply["hau"] = False
    try:
        return ", ".join(output)
    except:
        return "даже не знаю, что и сказать"
