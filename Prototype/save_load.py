# code piece to save and load random forest model
import cPickle

rf = RandomForestRegresor()
rf.fit(X, y)

with open('path/to/file', 'wb') as f:
    cPickle.dump(rf, f)


# in your prediction file                                                                                                                                                                                                           

with open('path/to/file', 'rb') as f:
    rf = cPickle.load(f)


preds = rf.predict(new_X)