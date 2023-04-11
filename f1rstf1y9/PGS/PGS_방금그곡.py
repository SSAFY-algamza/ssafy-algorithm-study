def change_code(code):
    return code.replace('C#', 'H').replace('D#', 'I').replace('F#', 'J').replace('G#', 'K').replace('A#', 'L')

def solution(m, musicinfos):
    ans_play_len = 0
    answer = ''
    m = change_code(m)

    for music in musicinfos:
        music = music.split(',')
        start_h, start_m, end_h, end_m = int(music[0][:2]), int(music[0][3:]), int(music[1][:2]), int(music[1][3:])
        play_len = (end_h * 60 + end_m) - (start_h * 60 + start_m)

        if play_len <= ans_play_len:
            continue

        main_code = change_code(music[3])
        play_code = main_code
        while play_len > len(play_code):
            play_code += main_code

        play_code = play_code[:play_len]
        if m in play_code:
            ans_play_len, answer = play_len, music[2]

    return answer if answer else "(None)"