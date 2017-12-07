import random

hist = []
prediction_translate = {'r':'p', 'p':'s', 's':'r'}
ai_wins = 0
pc_wins = 0
ties = 0
predictions = 0
correct_predictions = 0

def load_hist():
    global hist
    h = open('history.txt', 'r')
    for a in h:
        s = list(a)
        for i in s:
            if i in ['r','p','s']:
                hist.append(i)
    h.close()


def get_player_guess():
    guess = input("Guess:  ")
    if guess not in ['r', 'p', 's']:
        if guess != 'exit':
            return 'r'
        else:
            h = open('history.txt',mode='a')
            for letter in hist:
                h.write(letter)
            h.close()
            exit()
    return guess


def get_hist_patt_freqs(history, depth=3):
    if len(history) > depth:
        index = -1
        pattern = []
        freq = {'r': 0, 'p': 0, 's': 0, 'n': 0, 'depth': depth}
        for i in range(depth):
            pattern.append(history[index])
            index = index - 1
        pattern.reverse()
        # count frequency of pattern matches
        if len(pattern) > 0:
            print(pattern)
            for i in range(len(history)):
                if history[i] == pattern[0]:
                    full_match = True
                    if i + len(pattern) < len(hist):
                        for j in range(len(pattern)):
                            if not history[i + j] == pattern[j]:
                                full_match = False
                                break
                        if full_match:
                            if (i + len(pattern)) < len(history):
                                freq[history[i + len(pattern)]] = freq[history[i + len(pattern)]] + 1
                                freq['n'] = freq['n'] + 1
        print(freq)
        return freq


def combine_freqs(a, b):
    return {'r': (a['r'] + b['r']) / 2,
            'p': (a['p'] + b['p']) / 2,
            's': (a['s'] + b['s']) / 2,
            'n': (a['n'] + b['n']) / 2,
            'depth': (a['depth'] + b['depth']) / 2}


def get_pick(scoring):
    r = scoring['r']
    p = scoring['p']
    s = scoring['s']
    if r >= p and r >= s:
        return 'r'
    elif p >= r and p >= s:
        return 'p'
    elif s >= r and s >= p:
        return 's'
    else:
        return 's'
    return 's'


def get_random_choice():
    ret = random.choice(['r', 'p', 's'])
    return ret

def score_item(freq, pick):
    try:
        ret = (freq[pick] / freq['n']) * freq['depth']
    except:
        ret = 0
    return ret

def score_freqs(freqs_list):
    scores = {'r':0,'p':0,'s':0}
    for freq in freqs_list:
        scores['r'] += score_item(freq,'r')
        scores['p'] += score_item(freq,'p')
        scores['s'] += score_item(freq,'s')
    print(scores)
    return scores

def get_player_prediction(diff=10):
    if len(hist) < 3:
        return get_random_choice()
    freq_dict = []
    for i in range(diff):
        freq_dict.append(get_hist_patt_freqs(hist,i))
    return get_pick(score_freqs(freq_dict))


def score_game(ai_pick, pc_pick, ai_predict):
    global predictions
    global ai_wins
    global pc_wins
    global ties
    global predictions
    global correct_predictions
    predictions += 1
    if pc_pick == ai_predict:
        correct_predictions += 1
    if pc_pick == 'r':
        if ai_pick == 'r':
            ties += 1
        elif ai_pick == 'p':
            ai_wins += 1
            print('AI wins!')
        elif ai_pick == 's':
            pc_wins += 1
            print('Player wins!')
    elif pc_pick == 'p':
        if ai_pick == 'r':
            pc_wins += 1
            print('Player wins!')
        elif ai_pick == 'p':
            ties += 1
        elif ai_pick == 's':
            ai_wins += 1
            print('AI wins!')
    elif pc_pick == 's':
        if ai_pick == 'r':
            ai_wins += 1
            print('AI wins!')
        elif ai_pick == 'p':
            pc_wins += 1
            print('Player wins!')
        elif ai_pick == 's':
            ties += 1
    print('player wins: ', pc_wins, 
            'ai wins: ', ai_wins, 
            'ties: ', ties, 
            'accuracy: ', correct_predictions / predictions,
            'AI Win/Loss ratio: ', (ai_wins + 1) / (pc_wins + 1))

def play_round():
    prediction = get_player_prediction()
    translated = prediction_translate[prediction]
    pg = get_player_guess()
    hist.append(pg)
    print('AI pick: ', translated)
    score_game(translated, pg, prediction)

def main():
    load_hist()
    
    while True:
        play_round()
main()


