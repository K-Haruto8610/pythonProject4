from gensim.models import word2vec
#word2vecモデルの読み込み
MODEL_PATH = "wiki.model"
model = word2vec.Word2Vec.load(MODEL_PATH)

#word2vecの辞書に含まれていればtrueを返す。
def in_w2v(word):
  return word in model.wv.vocab

#word2vecの辞書に含まれている単語だけを返す。
def remove_unknown_w2v_word(words):
  return [v for v in words if in_w2v(v)]

#word2vecのvocabに含まれるかどうかは事前にチェックしておき、この関数の中ではチェックしない
#w1、words2はローマ字ではなく漢字かな交じりを使うことに注意
def get_w2v_based_correct_word(w1, words2, threshold=0.8):
  word = []
  max_sim = threshold
  for w2 in words2:
    sim = model.wv.similarity(w1=w1,w2=w2)
    if sim < max_sim: continue
    if sim > max_sim:
      max_sim = sim
      word = [w2]
    elif dist == max_sim:
      word.append(w2)
  return word