def solution(genres, plays):
    genres_cnt = len(set(genres))
    genres_dict = {} # 장르별 (재생수, idx) 리스트
    genres_sum = {} # 장르별 총 재생횟수
    ans = []
    for i in set(genres):
        genres_sum[i] = 0
    for i in range(len(genres)):
        if genres[i] in genres_dict:
            genres_dict[genres[i]].append((plays[i], i))
        else:
            genres_dict[genres[i]] = [(plays[i], i)]
        genres_sum[genres[i]] += plays[i]
    sort_sum = sorted(list(genres_sum.items()), key = lambda x: -x[1])
    for i in range(genres_cnt):
        tmp_dict = sorted(genres_dict[sort_sum[i][0]], key = lambda x: -x[0])
        if len(tmp_dict) < 2:
            ans.append(tmp_dict[0][1])
        else:
            ans.append(tmp_dict[0][1])
            ans.append(tmp_dict[1][1])
    return ans