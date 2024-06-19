from joblib import dump, load
import sklearn
import numpy as np
def predict(Sadness, Euphoric, Exhausted, Sleepdissorder, MoodSwing, Suicidalthoughts, Anorxia, AuthorityRespect, 
            TryExplanation, AggressiveResponse, IgnoreMoveOn, NervousBreakdown, AdmitMistakes, Overthinking, SexualActivity,
              Concentration, Optimisim):
  model_path = "./model.joblib"
  clf = load(model_path)
  list = [[Sadness, Euphoric, Exhausted, Sleepdissorder, 
            MoodSwing, Suicidalthoughts, Anorxia, AuthorityRespect,TryExplanation, AggressiveResponse, IgnoreMoveOn,
            NervousBreakdown, AdmitMistakes, Overthinking, SexualActivity, Concentration, Optimisim]]
  input = np.array(list)
  preds = clf.predict(input)
  print(preds[0])
  return int(preds[0])