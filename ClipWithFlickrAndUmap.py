import torch #neural network library and runtime
import clip #The Model which extracts the image features
import os #Interacts with the system
from PIL import Image # The way you store images
import umap.umap_ as umap #Used to map images to x,y coordinates
import matplotlib.pyplot as plt #plotting graphs
import numpy #Using to save arrays
import json

device = "cuda" if torch.cuda.is_available() else "cpu" # taken from CLIP
model, preprocess = clip.load("ViT-B/32", device=device) #taken from clip

output = [] 

directory = "C:\Users\\dfaga\\Documents\\FYP2\filesForAppendix\\Image Browser Code\\Images" #Directory where 8k dataset is saved

files = [x for x in os.listdir(directory) if x.endswith(".jpg")]
for filename in files:
    print(filename)
    image = preprocess(Image.open(directory+"\\"+filename)).unsqueeze(0).to(device) #Using CLIP to pre process image

    with torch.no_grad(): #Taken from clip. No Gradiants because I'm not training anything
        image_features = model.encode_image(image) #Clip extracting the image features
        output.append(image_features) # Appending those features to the list
       

output = torch.vstack(output) #Converts the list to a torch matrix
output = umap.UMAP(n_neighbors=10,min_dist=0.1,n_components=2,random_state=42).fit_transform(output) 
#### Neighbours decides how close clusters are. min_dist decides how close points are. 
#### Compononents is set to 2 as I only want 2D space. 3 would mean 3D.
#### Random State is set at 42 based off the UMAP examples. 
#### UMAP-Learn REFERENCE for these settings


#plt.scatter(output[:,0],output[:,1], s=0.1) # Plots the output
#plt.show()
        
output = output.tolist()
assert(len(output) == len(files))
jsonres = json.dumps({files[i]: output[i] for i in range(len(files))}, indent=4)
f = open("Flickr_withUMAP_2.json","w")
f.write(jsonres)   


 