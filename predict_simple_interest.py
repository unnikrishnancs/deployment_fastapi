import pickle # to save and load model

def predict_si(p,r,t):
	# load model
	filename="model/model_simpleinterest.sav"
	load_model=pickle.load(open(filename,'rb'))
	si=load_model.predict([[p,r,t]])
	return si[0]

if __name__=="__main__":
	si=predict_si(1000,5,1)
	print("si=",si)
	
